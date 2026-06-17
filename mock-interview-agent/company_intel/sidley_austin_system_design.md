# System Design: Secure Legal Document Portal
**Sidley Austin — Client Document Upload/Download**

---

## Requirements

### Functional
- Clients authenticate and access a portal to upload/download their legal documents
- Attorneys can upload documents on behalf of clients
- Role-based access: clients see only their own documents; attorneys scoped to their matters
- Full audit trail of all access events
- Geo-based access controls: US-stored data must not be served from or cached in unauthorized regions

### Non-Functional
- Law firm compliance: data residency (US), encryption at rest/in transit, audit logging
- High availability (99.9%+), disaster recovery across paired US regions
- No document accessible via public URL — all access through authenticated, time-limited signed URLs
- Cross-border access detection, alerting, and enforcement

---

## High-Level Architecture

```
┌──────────────────────────────────────────────────────────┐
│                      CLIENT BROWSER                       │
│                     (HTTPS only)                         │
└──────────────────────────┬───────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────┐
│            Azure Front Door                               │
│      WAF · DDoS Protection · SSL Offload · CDN           │
│      Geo-filtering · No document caching                 │
└──────────┬───────────────────────────────────────────────┘
           │
    ┌──────┴──────┐
    ▼             ▼
┌────────────┐  ┌──────────────────────────────────┐
│ Static Web │  │     Azure API Management         │
│ App (SPA)  │  │  Rate limiting · Auth · Routing  │
│ React/Vue  │  │  Request logging · Policy        │
└────────────┘  └────────────────┬─────────────────┘
                                  │
                 ┌────────────────┼────────────────┐
                 ▼                ▼                 ▼
         ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
         │  Azure AD   │  │  Document   │  │  Admin API  │
         │    B2C      │  │    API      │  │  (attorney  │
         │  MFA · OIDC │  │ App Service │  │   portal)   │
         │  Conditional│  └──────┬──────┘  └─────────────┘
         │  Access     │         │
         └─────────────┘         │
                                  │
               ┌──────────────────┼──────────────────┐
               ▼                  ▼                   ▼
    ┌──────────────────┐  ┌───────────────┐  ┌──────────────┐
    │  Azure Blob      │  │  Azure SQL    │  │ Azure Service│
    │  Storage         │  │  Database     │  │    Bus       │
    │  (documents)     │  │  (metadata,   │  │  (async scan │
    │  US regions only │  │   audit log,  │  │   queue)     │
    │  Private EP only │  │   permissions,│  └──────┬───────┘
    │  CMK encryption  │  │   geo-except) │         │
    └──────────────────┘  └───────────────┘         ▼
                                           ┌──────────────────┐
                                           │ Azure Functions  │
                                           │  Virus scan ·    │
                                           │  metadata tag ·  │
                                           │  quarantine      │
                                           └──────────────────┘

────────────── CROSS-CUTTING ──────────────────────────────────
  Key Vault          → CMK for Blob, secrets, TLS certs
  Managed Identity   → Service-to-service auth (no credentials in code)
  VNet + Private EP  → Blob and SQL never on public internet
  Azure Monitor      → App Insights, Log Analytics, alerting
  Azure Policy       → Enforce data residency (US only), encryption, tagging
  GeoIP Service      → IP-to-country resolution at API layer (Azure Maps)
───────────────────────────────────────────────────────────────
```

---

## Key Component Decisions

| Component | Choice | Why |
|---|---|---|
| Auth | Azure AD B2C | Client-facing IdP, MFA, OIDC/OAuth2, integrates with firm's Azure AD |
| Document storage | Blob Storage (private, CMK) | Scalable, law-firm-grade encryption, no public access |
| URL generation | SAS tokens (short TTL) | Time-limited, signed, per-document — no permanent public URLs |
| API gateway | API Management | Centralized auth enforcement, rate limiting, audit logging |
| Async processing | Service Bus → Functions | Decouples virus scan from upload response; quarantines bad files |
| Metadata/Audit | Azure SQL | Relational model for permissions, structured audit queries |
| Geo detection | Azure Maps GeoIP | IP-to-country resolution before SAS token issuance |

---

## Upload Flow

1. Client authenticates via Azure AD B2C → receives JWT
2. SPA calls Document API with JWT
3. API validates token, checks client's matter/case permissions in SQL
4. API generates a short-lived SAS upload URL (write-only, 15 min TTL) from Blob Storage via Managed Identity
5. Client uploads directly to Blob using SAS URL
6. Blob event triggers Service Bus → Functions runs virus scan
7. On clean: metadata record written to SQL, document marked available; audit log entry written
8. On infected: file moved to quarantine container, alert fired to security team

---

## Download Flow

1. Client authenticates, requests document
2. API checks SQL: does this client have read permission on this matter?
3. **Geo-check:** API resolves caller IP to country; compares against user's registered geography (see Cross-Border Controls)
4. If geo check passes: API generates read-only SAS token (5–15 min TTL) for specific blob
5. SAS URL returned to client; download audit log entry written
6. Client downloads directly from Blob — API never proxies file bytes

---

## Data Residency & Cross-Border Access Controls

### The Scenario
A US-based attorney travels to Germany and attempts to open a client document. The data must never be stored or cached in the EU, and the access must be detected, flagged, and blocked unless a pre-approved exception is in place.

### Enforcement Layers (Defense in Depth)

**1. Azure AD Conditional Access (identity layer)**
- Attorneys' accounts tagged with registered home geography (e.g., `location: US`)
- Policy: if sign-in IP resolves to non-US country → require step-up MFA + generate risk signal
- High-risk sign-ins (impossible travel, unfamiliar location) → block or require manager approval

**2. API Layer — Geo-check before SAS token issuance**
- Before generating any SAS URL, Document API resolves caller IP via Azure Maps GeoIP
- If resolved country ≠ user's registered country → deny SAS issuance, return `403 Forbidden`
- Audit log entry written with full geo detail on every denial
- Legitimate travelers request a temporary geo-exception via admin workflow (logged, time-bounded, stored in SQL)

**3. Azure Front Door WAF — Geo-filtering**
- WAF policy flags or blocks requests from countries outside the firm's operating footprint
- For Sidley Austin (global firm): detection and alerting rather than blanket block; WAF is first line of detection

**4. No CDN Caching of Documents**
- Front Door configured with `Cache-Control: no-store` on all document API responses
- SAS URLs point directly to US-region Blob Storage endpoint — data always served from US, never cached at EU edge PoPs
- Static assets (SPA JS/CSS) can be cached globally; document bytes never are

**5. Data Never Leaves US Region**
- Blob Storage deployed to `East US` + `West US 2` (paired regions for HA/DR)
- Azure Policy `Allowed locations` scoped to US regions only — prevents accidental EU deployment
- VNet and Private Endpoints confined to US regions

### Cross-Border Access Flow

```
Attorney in Frankfurt opens document
        │
        ▼
Azure AD B2C sign-in
  → Conditional Access detects EU IP
  → Flags as risky sign-in
  → Requires MFA step-up
        │
        ▼
Document API receives request
  → Resolves IP: DE (Germany)
  → Checks attorney profile: registered US
  → GEO MISMATCH → 403 returned
  → Audit log: { user, doc_id, ip, geo: "DE", result: "denied", timestamp }
  → Azure Monitor alert fired → security team notified
        │
  [If geo-exception pre-approved by admin]
        ▼
  SAS token issued for US Blob endpoint
  Data flows: US East Blob → attorney laptop in Frankfurt
  (data transits internet but originates and is stored in US only)
  Audit log: { ..., geo: "DE", exception_ref: "EX-2026-041", result: "allowed" }
```

---

## Audit Log Schema

```sql
document_access_log (
  id            UNIQUEIDENTIFIER    PRIMARY KEY DEFAULT NEWID(),
  user_id       VARCHAR(100)        NOT NULL,   -- Azure AD object ID
  document_id   VARCHAR(100)        NOT NULL,
  action        VARCHAR(20)         NOT NULL,   -- UPLOAD | DOWNLOAD | DENIED | QUARANTINED
  ip_address    VARCHAR(45)         NOT NULL,
  geo_country   CHAR(2)             NOT NULL,   -- ISO 3166-1 alpha-2, resolved from IP
  user_geo_home CHAR(2)             NOT NULL,   -- attorney/client registered country
  geo_match     BIT                 NOT NULL,   -- 1 = matched, 0 = mismatch
  exception_ref VARCHAR(50)         NULL,       -- populated if geo-exception granted
  result        VARCHAR(20)         NOT NULL,   -- ALLOWED | DENIED | ESCALATED
  timestamp     DATETIMEOFFSET      NOT NULL    -- UTC
)
```

---

## Key Tradeoffs

**SAS tokens vs. streaming through API**
SAS tokens offload bandwidth from the API tier and are more scalable, but the API cannot enforce mid-stream revocation. Short TTLs (5–15 min) mitigate this. For law firm use this is acceptable — a revoked token simply expires quickly.

**Azure AD B2C vs. custom auth**
B2C handles MFA, password reset, and identity federation out of the box, reducing security liability. Tradeoff is less control over auth UX and dependency on Microsoft's B2C availability.

**Blob private endpoint vs. service endpoint**
Private endpoint keeps traffic fully off the public internet, which is the right call for client legal documents despite the added VNet complexity and cost.

**Geo-blocking vs. geo-alerting**
For a global firm like Sidley Austin, blanket blocking by country would disrupt legitimate international travel. The preferred model is: detect → alert → deny by default → allow via admin-approved exception workflow. This balances compliance with operational reality.

**VPN bypass risk**
An attorney on a VPN will present the VPN exit node's geo, potentially bypassing geo-checks. Policy should require attorneys to use firm-managed VPN (with known IP ranges allowlisted) rather than personal VPNs. Conditional Access can enforce compliant device + managed network requirements.
