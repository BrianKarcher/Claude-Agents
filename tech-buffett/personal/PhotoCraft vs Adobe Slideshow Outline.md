# Is PhotoCraft a Threat to Adobe? — Slideshow Outline (YouTube)

Narrative walk-through: what PhotoCraft is → how it was built → the bug list → will pros switch → the rest of the "Craft" suite → is it legal → what Adobe & Microsoft can do → what it means for ADBE → verdict.

Research date: **Oct 22, 2026.** The project is about three weeks old and ships a new version every few days. Re-check the GitHub stats, version numbers and any Adobe/Microsoft response the day you record. Sources are listed at the bottom. Legal-precedent beats (Slides 22–24) are general-knowledge framing, not legal advice. Sanity-check case names and years before recording.

Anchors used throughout: PhotoCraft repo **~71k stars / ~12.6k forks / ~1.7k open issues / ~940 PRs** (mid-Oct 2026). First commit **Sept 30, 2026**. ADBE **~$238**, down ~30% YTD (mid-Oct).

---

## PART 1 — WHAT IS PHOTOCRAFT?

### Slide 1 — Title
- **Is PhotoCraft a Threat to Adobe?**
- Subtitle: One developer, a fleet of AI agents, and a free Photoshop clone in three weeks. Hype, or the start of something real?
- "As of Oct 22, 2026"

### Slide 2 — The 30-Second Version
- PhotoCraft is a **free, open-source rebuild of Adobe Photoshop**, written from scratch in Rust
- Built by **Brandon Thomas** (Atlanta; ex-Square, ex-Storyteller.ai) under his company **ArtCraft**
- Written largely by **parallel Claude Opus 5.5 agents**. Opus is listed as a co-author in the git history.
- First commit Sept 30 → **~71,000 GitHub stars** in about three weeks, among the fastest-rising repos of the year
- License: **MIT / Apache-2.0**. Anyone can use, fork, or sell it.

### Slide 3 — The Origin Story (the hook)
- Posted to Reddit under the handle **u/ai_art_is_art**; Thomas was identified a few days later
- Motivation in his own words: Adobe "charged me the 'cancellation fee' on multiple occasions and I've hated them ever since"
- Timing: Adobe is already under fire for those fees. Reporting cites a proposed **~$150M DOJ settlement** over hidden early-termination fees. *(Verify the current status before recording.)*
- Thomas's thesis, quoted widely: **"Software is over."** If AI agents can rebuild a $20B/yr product line in weeks, every software moat is in question.
- B-roll idea: the viral X post, "One guy just cloned $100 billion worth of Adobe software in about a week"

### Slide 4 — What It Actually Does (README claims)
- **67 tools, 500+ commands**, every Photoshop menu item wired to a command
- Layers, groups, clipping masks, pixel + vector masks, **smart objects**, **16 adjustment layers**, layer styles, **27 blend modes**
- Type engine with on-canvas editing, vector shapes, brush engine, live filter previews
- RGB / Grayscale / **CMYK / Lab** at 8/16/32-bit, ICC color management
- Opens & saves **PSD/PSB**, layered TIFF, GIMP .xcf, Krita .kra, OpenRaster, PNG/JPEG/WebP/EXR
- **307 of 309** files in the public psd-tools test set re-save with identical rendering
- Photoshop-style menus and shortcuts (⌘J, ⇧⌘D, …) so muscle memory carries over

### Slide 5 — How It Runs
- Native on **macOS, Windows, Linux, FreeBSD**, plus **in the browser** via WebAssembly (no login)
- Fully offline, no account, no subscription
- **Every action is a command**, so it can be driven from a CLI, JSON scripts, or an **MCP server**. That means *AI agents can operate PhotoCraft directly*. Photoshop has no real equivalent of this.
- GPU-accelerated Rust + egui UI. Reviewers consistently call it lightweight and fast.

### Slide 6 — The Fine Print: How ArtCraft Makes Money
- The apps are free. ArtCraft sells **AI-credit plans at $10 / $35 / $60 per month** for its generative image/video studio
- Critics (e.g., photographer Glyn Dewis) point out the irony: an anti-subscription pitch funded by… a subscription
- The AI features route to **Google and OpenAI models**, so files used with those features may leave your machine
- The ArtCraft contact email still points to **Storyteller.ai**, makers of FakeYou (celebrity voice generation, subject of a 2022 Italian data-protection inquiry). This is a trust question raised by reviewers; no wrongdoing is alleged.

---

## PART 2 — THE BUG LIST

### Slide 7 — By ArtCraft's Own Admission
- README: **"early alpha — not yet a Photoshop replacement for daily professional work"**
- Self-assessed parity for daily professional work: roughly **25–45%**, depending on which roadmap page you read. One estimate: "maybe a third of pro workflows."
- Every menu item is wired, but the README admits this **"measures wiring, not behaviour"**
- Original promise of "complete parity within a month" has been walked back to "99% within months"

### Slide 8 — Known Bugs (from reviews + the GitHub tracker)
| Area | Problem |
|---|---|
| **Layers** | Adding an effect (e.g., drop shadow) to a small object expands the layer to the full canvas size |
| **Brushes** | Severe lag and stuttering with large brush sizes; high CPU usage |
| **Large files** | Failures opening big TIFF / PSB documents; slow on complex layered files |
| **Selections** | Selection tools noticeably weaker than Photoshop's |
| **Paths / Pen** | Paths behave differently from Photoshop, which breaks precision-cutout muscle memory |
| **Background removal** | Reported as not working |
| **Fonts** | Some font previews render as solid red boxes |
| **Layer styles** | Controls incomplete |
| **UI** | Minor display glitches; "Show in Explorer" on tab right-click broken |
| **Linux** | Drag-and-drop broken on Wayland; blurry UI with fractional scaling on XWayland |
- **~1,700 open issues**, and **8+ releases between Oct 5 and Oct 18**. Bugs are being fixed fast, and new ones are arriving just as fast.

### Slide 9 — Missing Entirely
- **Generative AI**: no Generative Fill / Expand equivalent (Photoshop's headline feature of the last two years)
- ~**15 Photoshop tools** not yet implemented
- **No plug-in compatibility.** Nik, Topaz, Portraiture and the rest of the pro plug-in ecosystem don't load.
- Professional typography depth (OpenType features, paragraph composers)
- PSD re-saves aren't byte-identical. Formats: no JPEG XL, AVIF write-only, HEIC read-only, Affinity files read-only
- No cloud libraries, no team sharing, no Lightroom/Bridge-style integration with Adobe's ecosystem

### Slide 10 — The Fair Counterpoint
- For **~3 weeks old**, it's remarkable. Fekke's review: "many features work extremely well for a tool only a couple of weeks old"
- Levels, Curves, Vibrance, B&W, Gaussian Blur and Oil Paint all work fine for everyday edits
- Open source + 12,600 forks + 940 PRs = a rate of improvement no traditional product team matches
- **The bugs describe October 2026. The question for the video is what PhotoCraft looks like in October 2027.**

---

## PART 3 — WILL PROFESSIONALS SWITCH?

### Slide 11 — Short Answer: Not Now
- Every professional reviewer we found came to the same conclusion. Fekke: **"unusable for professional work"**. He's keeping his Creative Cloud subscription. Dewis: won't install it "as it stands."
- Pros don't pay for Photoshop for the brushes. They pay for **reliability on deadline**.

### Slide 12 — Why Pros Stay (the real moat)
1. **Reliability**: one corrupted PSD on a client job costs more than a decade of subscriptions
2. **Plug-ins & ecosystem**: Camera Raw, Lightroom ↔ Photoshop round-trips, Bridge, Libraries, Stock, Fonts
3. **Generative AI (Firefly)**: commercially "safe" generative fill with IP indemnification for enterprises
4. **Client & agency standards**: deliverables are specified as "PSD from Photoshop"; agencies standardize on CC
5. **Enterprise procurement**: security review, signed vendor contract, support SLA, SSO/admin console. An open-source project run by one person doesn't pass procurement.
6. **Training & hiring**: schools, courses and job listings say "Photoshop"
7. **Trust & security**: an unsigned or unfamiliar installer with full disk access is a hard sell (HSBC told clients *not* to download it)

### Slide 13 — Who *Will* Try It
- **Hobbyists, students, and lapsed subscribers.** This is the segment HSBC explicitly trimmed estimates for.
- People who want to **open a PSD someone sent them** without paying $23/month
- Developers & **AI-agent workflows** (MCP/CLI control is a genuine differentiator)
- Linux users, who have never had native Photoshop
- But this segment **already had options**: GIMP (free, decades old), Photopea (browser), Affinity (now free under Canva, *verify*), Krita. Adobe kept growing anyway.

### Slide 14 — What Would Change the Answer
- Plug-in compatibility (or a plug-in ecosystem of its own)
- Generative fill (easy to bolt on via third-party models, harder to make "commercially safe")
- A **funded, accountable entity** behind it, like Canva behind Affinity or Blackmagic behind DaVinci Resolve
- 12+ months of stability with no file-corruption horror stories
- **The DaVinci Resolve precedent**: a free tool *did* take real share from Premiere among pros, but it took **a decade** and a hardware company subsidizing it

---

## PART 4 — THE REST OF THE "CRAFT" SUITE

### Slide 15 — It's Not Just Photoshop
| Craft app | Clones | Company |
|---|---|---|
| **PhotoCraft** | Photoshop | Adobe |
| **LightCraft** | Lightroom (not Classic) | Adobe |
| **FilmCraft** | Premiere Pro | Adobe |
| **VectorCraft** | Illustrator | Adobe |
| **EffectCraft** | After Effects | Adobe |
| **DesignCraft** | InDesign | Adobe |
| **PdfCraft** (a.k.a. PrintCraft in early coverage) | Acrobat Pro | Adobe |
| **WordCraft** | Word | Microsoft |
| **GridCraft** | Excel | Microsoft |
| **DeckCraft** | PowerPoint | Microsoft |
| **SoundCraft** | Pro Tools | Avid |
| **CADCraft** | AutoCAD | Autodesk |
- **7 Adobe apps + 3 Microsoft Office apps**, plus Avid and Autodesk targets. Seven apps launched Oct 7, and the Office trio followed about a week later.
- *(SoundCraft / CADCraft appear in one secondary source; confirm on ArtCraft's site before recording.)*

### Slide 16 — The Microsoft Office Clones
- WordCraft, GridCraft and DeckCraft read and write **.docx / .xlsx / .pptx**
- Self-reported command coverage: **~88% of Word's ribbon, ~89% of Excel's, ~79% of PowerPoint's**, ~60% overall parity (single-source figures)
- Versions ~0.5–0.8; authors still call them alpha
- **Microsoft declined to comment**
- Key context: free Office alternatives (**LibreOffice / OpenOffice**) have existed for **20+ years**. Microsoft never sued them, and Office kept growing. That's the best evidence for how this plays out.

### Slide 17 — Why Microsoft Is Less Exposed Than Adobe
- Office is sold **bundled** into Microsoft 365 with Exchange, Teams, OneDrive, Entra ID and Copilot. Nobody buys M365 for Word alone.
- Enterprise lock-in comes from **identity, compliance, and collaboration**, not the editor
- Adobe sells the *app itself* as the product, so a free app that's "good enough" bites harder
- Irony to point out: the repos are hosted on **GitHub, which Microsoft owns**

---

## PART 5 — IS IT LEGAL?

### Slide 18 — The Claim: "Clean-Room Reimplementation"
- ArtCraft says the apps were built **from public file-format specs and observed behavior**, using no Adobe code, shaders, or assets
- The project reportedly **bans decompiled code** contributions; Thomas says nothing was decompiled
- The README disclaims affiliation: Adobe/Photoshop are Adobe trademarks, used only "to describe compatible workflows"
- Caveat: the clean-room claim is **unaudited**

### Slide 19 — Copyright: Probably Fine
- Copyright protects **code and expression, not functionality**. Ideas like "layers" or "curves" aren't protectable.
- **Lotus v. Borland (1995)**: menu command hierarchy held a non-copyrightable "method of operation"
- **Google v. Oracle (2021)**: reimplementing an interface for compatibility was fair use
- **Sega v. Accolade (1992)**: studying a product to achieve interoperability can be fair use
- **Apple v. Microsoft (1994)**: "look and feel" claims largely failed
- File-format compatibility (PSD, DOCX) is well-trodden ground: GIMP, Photopea, LibreOffice, Affinity
- Plagiarism Today's read: the apps are on **"decent footing"** against copyright claims

### Slide 20 — The Weird Twist: Can AI-Written Code Be Licensed?
- U.S. Copyright Office + **Thaler v. Perlmutter**: works with no human author aren't copyrightable
- If the code is mostly AI-generated, the **MIT/Apache license may rest on thin ground**. You can't license what you don't own.
- Practical effect: little for users (it's free either way); matters more for ArtCraft's ability to enforce anything, and for whoever forks it
- How much human authorship is needed is still unsettled. Flag this as open.

### Slide 21 — Where the Real Legal Risk Is
1. **Contract / EULA (strongest for Adobe)**: Adobe's terms reportedly bar reverse engineering and studying the software's inputs/outputs "in order to recreate that system." Thomas was a paying subscriber (that's where the fee grudge came from), so he likely agreed to them. *This targets the person, not the code.*
2. **Patents**: Adobe holds thousands. Content-Aware Fill, healing algorithms, and specific filters are candidates. Which ones read on ArtCraft is unknown.
3. **Trademark / trade dress**: names differ, but a stated "1-to-1 clone" invites a confusion argument; Photoshop-identical UI could be argued as trade dress
4. **AI-training angle**: Adobe's terms also bar using outputs to train AI/ML. Whether directing agents with Photoshop knowledge counts is untested.
- Not covered by any source: DMCA anti-circumvention. There's no indication any DRM was bypassed.

### Slide 22 — Legal Verdict
- **The software itself: likely legal** to build, distribute, and use
- **The builder: some contractual exposure** if Adobe chooses to pursue it
- **Users: essentially no risk** from using an independently written editor (the security risk of the installer is a separate question; see Slide 12)
- As of Oct 22: **no lawsuit, no cease-and-desist, no public Adobe statement**

---

## PART 6 — WHAT CAN ADOBE AND MICROSOFT DO?

### Slide 23 — Adobe's Legal Options (and Why They're Risky)
- Sue on **contract/EULA**, **patents**, or **trademark/trade dress**
- **DMCA takedown** to GitHub: weak without copied code, and likely to be challenged publicly
- The **threat alone** might work: one developer vs. a ~$100B company
- **Statute of limitations**: roughly three years, so Adobe can wait and watch
- **The catch, the Streisand effect**: suing makes ArtCraft famous, and open source **can't be un-released**. 12,600 forks already exist. Shutting down Thomas doesn't shut down the code.
- PR optics: Adobe is suing a customer it overcharged with cancellation fees, while its DOJ settlement is still in the news. That's a bad headline.

### Slide 24 — Adobe's Business Options (the smarter play)
1. **Fix the grievance**: friendlier cancellation, cheaper single-app / hobbyist tiers, a free "Photoshop Lite." Take away the origin story.
2. **Lean into what clones can't copy**: Firefly + commercially safe generative AI with IP indemnity, Creative Cloud libraries, collaboration, enterprise admin
3. **Lean into agents**: ship Photoshop's own MCP/agent API so AI workflows don't route around Adobe
4. **Ecosystem gravity**: plug-in partners, Stock, Fonts, Frame.io, Express, education deals
5. **Format moves**: extending PSD makes clones' compatibility harder, but it risks antitrust attention and angering users. Low odds.
6. **Co-opt**: hire, fund, or acquire. Adobe's Figma deal was blocked, but a tiny open-source acquisition faces no such hurdle (and does nothing to the forks).

### Slide 25 — Microsoft's Options
- **Do nothing**, the LibreOffice playbook. It's worked for 20 years. (Microsoft has already declined to comment.)
- Bundling: Office's value sits in M365 + Teams + Entra + Copilot, not the .docx editor
- Copilot integration deepens the gap a standalone editor can't easily close
- **GitHub problem**: a Microsoft-owned platform taking down a Microsoft-competing project would be a PR disaster. Expect Microsoft to leave it alone.
- Same EULA/patent theoretical levers as Adobe, with even less reason to pull them

---

## PART 7 — WHAT IT MEANS FOR ADOBE STOCK

### Slide 26 — Wall Street Already Reacted
- **Oct 13, 2026: HSBC downgrades ADBE Buy → Hold**, target **$310 → $267**, citing AI-built clones and trimming estimates for amateur-user churn. The analyst also advised clients *not* to download ArtCraft (security/legal).
- **Wells Fargo**: Underweight, **$225** target (Oct 12, single source; verify)
- Record short interest and record number of sell ratings (per Futu)
- Stock ~**$238**, down ~**30% YTD**. ArtCraft caused only a small premarket dip. The selloff was already underway.
- Background drag: Q3 **organic net new ARR reportedly down 40%+**, a CEO transition (Narayen reportedly stepping down to board chair; *verify*)

### Slide 27 — The Real Threat Isn't PhotoCraft
- PhotoCraft the product is **not** a threat to Adobe's pro business today
- What it proves is the threat: **the cost of rebuilding mature software has collapsed**. Three weeks and a few AI agents produced a credible alpha of seven Adobe apps.
- That hits the stock in three ways:
  1. **Pricing power**: Adobe's ability to raise prices erodes when "good enough" is free
  2. **Low-end churn**: hobbyists and students, the top of Adobe's funnel, now have more and better free options
  3. **Terminal value / multiple**: investors now ask whether *any* app-software moat lasts 10 years, which compresses the multiple even if revenue holds
- Counterpoint: GIMP has been free for 25+ years, Photopea for 10+, Affinity is now free, and Adobe compounded through all of it

---

## PART 8 — VERDICT

### Slide 28 — Bull vs. Bear for Adobe, Side by Side
| "It's a threat" | "It's not" |
|---|---|
| ~71k stars in 3 weeks; fastest-improving rival Adobe has ever faced | ~1,700 open issues; self-rated 25–45% of pro workflows |
| Free + open source + forks = can't be killed by a lawsuit | GIMP/Photopea/Affinity were already free; Adobe kept growing |
| AI agents make rebuilding *any* feature cheap | Pros pay for reliability, plug-ins, Firefly, ecosystem, support |
| Hits Adobe's funnel (students/hobbyists) and pricing power | Enterprise procurement won't touch a one-person project |
| Adobe's PR position (fees, DOJ) makes it hard to fight | No funded, accountable company behind it (yet) |

### Slide 29 — Bottom Line
- **Is PhotoCraft a threat to Adobe's professional business today?** No.
- **Is it a threat to the low end and to Adobe's pricing power?** Yes, at the margin, and it compounds.
- **Is it legal?** The software almost certainly is. The builder has some contract exposure. Adobe suing would likely backfire.
- **The big takeaway:** PhotoCraft matters less as a product than as a demonstration. Software that took 35 years to build can now be approximated in weeks. Adobe's moat has to be *everything around the app*, and that's what investors are now repricing.
- What to watch: v1.0 and plug-in support · a funded company or foundation forming around it · any Adobe legal move · Adobe pricing/tier changes · Q4 net new ARR

### Slide 30 — Disclosures & Sources
- Not investment or legal advice. Personal research.
- PhotoCraft/ArtCraft figures are **self-reported by the project** or by secondary outlets; parity percentages and Office command-coverage figures are not independently verified
- Fast-moving story: stats as of mid/late Oct 2026
- Sources:
  - PhotoCraft GitHub README & issues: github.com/storytold/photocraft
  - Fekke, "Is PhotoCraft by ArtCraft a Photoshop Killer": fek.io
  - Glyn Dewis, "ArtCraft: Free Adobe Alternative, But Can You Trust It?": glyndewis.com
  - Plagiarism Today, "Copyright and the Vibe-Coded Adobe Clones" (Oct 14, 2026)
  - ScaleUs, "PhotoCraft: The Free, Open-Source Photoshop Rebuild…" (Oct 12, 2026)
  - PetaPixel (Oct 7 & Oct 12, 2026); Al Jazeera (Oct 14, 2026); Futurism; Office Watch; madrobot.blog
  - HSBC downgrade coverage: Investing.com, Seeking Alpha, Yahoo Finance/Barchart, GuruFocus; TradingView weekly recap; Futu News

---

**Note:** All PhotoCraft/ArtCraft facts trace to the sources above; nothing was invented. Single-source or shaky items are marked *verify*: Wells Fargo target, CEO transition, DOJ settlement status, SoundCraft/CADCraft, Affinity-free status, Office parity %. Case-law slides are general-knowledge framing. Keep the "fair counterpoint" (Slide 10) and the "it's not a threat" column (Slide 28) prominent. A video that just dunks on either side is less credible.
