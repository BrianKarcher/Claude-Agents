# Uber D&A Round — Optum Project Prep

> Project to reference in the ~15-minute Design & Architecture portion of the Coding + D&A phone screen.

---

## Project Overview

**Company:** Optum (01/2020 – 02/2026)
**Role:** Lead Software Engineer — Architect and technical lead
**Team size:** 5 engineers (people + technical lead)

**What it is:** Large-scale healthcare data matching and billing platform processing **billions of records** across insurers and providers.

**Business impact:**
- AI-assisted ETL pipeline improved data matching accuracy by **~90%**
- Contributed **tens of millions of dollars** in incremental annual revenue

---

## Architecture Summary

```
Airflow + Spark ETL Pipeline
        ↓
AI Matching Engine
        ↓
   [High confidence] → Automated billing workflows
   [Low confidence]  → React manual review portal
        ↓
Event-driven microservices backend
        ↓
AWS (EMR, DynamoDB, PostgreSQL, Snowflake)
```

**Key components:**
- **ETL Pipeline:** Airflow (orchestration) + Spark (distributed compute) on AWS EMR
- **Matching engine:** AI-assisted, produces confidence scores
- **Manual review portal:** React-based UI for human-in-the-loop review of low-confidence matches
- **Backend services:** Event-driven microservices (.NET, Docker, Kubernetes)
- **Storage:** DynamoDB, PostgreSQL, Snowflake
- **Infrastructure:** AWS, Terraform

---

## Architectural Decisions & Trade-offs

### Monolith → Microservices Decomposition
- **Decision:** Decomposed a legacy monolithic system into cloud-native, event-driven microservices
- **Why:** Independent scalability, deployability, and compliance isolation across services
- **Trade-off:** Added operational complexity (service discovery, distributed tracing, eventual consistency) — justified by scale and compliance requirements

### Airflow + Spark for ETL
- **Decision:** Airflow for orchestration, Spark on EMR for distributed compute
- **Why:** Billion-record scale requires distributed processing; Airflow provides robust DAG scheduling, retries, and observability
- **Trade-off:** Higher infrastructure cost and complexity vs. simpler batch jobs — justified by data volume

### Human-in-the-Loop for Low-Confidence Matches
- **Decision:** Route low-confidence AI matches to a React review portal instead of auto-rejecting or auto-approving
- **Why:** Healthcare billing errors are costly and legally significant; human review preserves accuracy at the margin
- **Trade-off:** Introduces latency and manual labor cost — acceptable given revenue and compliance stakes

### Healthcare Compliance
- Secure, auditable workflows throughout
- Data handling aligned with healthcare regulatory requirements
- Drove architecture decisions around access control, logging, and data residency

---

## Incident Response — Change Healthcare Cyberattack

- Played a central role in cross-functional recovery efforts
- Restored critical data pipelines and infrastructure
- Designed and implemented enhanced security and resiliency controls post-incident
- **Uber relevance:** Strong ownership-under-pressure story; maps directly to Uber's culture of accountability

---

## Scale-Up Questions — Be Ready

| Question | Answer |
|----------|--------|
| What would you change at 10x scale? | Evaluate DynamoDB partitioning limits; consider Kafka for event streaming at higher throughput; explore disaggregating Spark jobs for finer parallelism |
| How did you handle pipeline failures? | Airflow retry policies, dead-letter queues, alerting; post-incident: added circuit breakers and enhanced resiliency controls |
| How did you ensure data consistency across services? | Event-driven architecture with idempotent consumers; auditable workflows as a compliance requirement also enforced correctness |
| What was the hardest technical challenge? | Matching accuracy at billion-record scale across heterogeneous insurer/provider data schemas — required iterative model tuning and schema normalization |

---

## 2-Minute System Overview (Memorize This)

> "At Optum I was the architect and technical lead for a healthcare data matching and billing platform that processed billions of records across insurers and providers. The core was an AI-assisted ETL pipeline built on Airflow and Spark that matched patient and billing records with roughly 90% accuracy — contributing tens of millions in annual revenue. High-confidence matches flowed into automated billing workflows; low-confidence matches went to a React-based manual review portal for human adjudication. I led the decomposition of the legacy monolith into event-driven microservices on AWS, designed the pipeline architecture, set standards for the team, and also led incident response after the Change Healthcare cyberattack — restoring pipelines and redesigning our resiliency controls."
