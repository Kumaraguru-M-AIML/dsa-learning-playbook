# 🧬 ULTIMATE AI OPERATIONAL CONTEXT DOSSIER
**SYSTEM STATUS:** APEX-GRADE MONOREPO (OPTIMIZED)
**DATE:** MAY 11, 2026
**INTENT:** Feed this exact markdown file into any incoming LLM context window to instantly prime the agent with 100% operational clarity on this workspace.

---

## 🏛️ I. ARCHITECTURAL IDENTITY
This workspace is a **High-Tier Cognitive Monorepo** engineered to prevent context decay and maximize development velocity. It operates as an "Enterprise Data-Lake" combining proprietary engine logic with a massive recursive research arsenal.

### 📂 1. Atomic Directory Topology
Everything has been modularized into atomic package containers situated at the root:
*   **`/engine`**: The core runtime backbone and orchestrators (e.g., `cq_mythos_v2.py`).
*   **`/cognitive_tools`**: Thinking engines, attention allocators, and semantic guardrails.
*   **`/memory`**: Persistent SQLite ledgers and epistemic truth solvers.
*   **`/cq_bench`**: Verification suites, Z3 solvers, and scientific stress testers.
*   **`/docs`**: Master persistent ledger including the machine-readable capability index.
*   **`/config` & `/logs`**: Isolated infrastructure settings and runtime audit trails.

### 🚀 2. Universal Execution Gate
DO NOT attempt to launch scripts manually from subfolders. We built a smart-proxy at the root:
**`python run.py [module_name]`**
*   This script automatically injects all subdirectories into `PYTHONPATH`, resolving all cross-module imports natively. Use it for everything.

---

## 🧠 II. OPERATIONAL WORKFLOWS
We operate under a rigorous set of "Genius Cycles" defined in `/docs/GENIUS_WORKFLOW_CYCLES.md`. Key patterns incoming AI must know:
1.  **Context Hardening**: Limit file reading ONLY to the "Blast Radius" of changes to save tokens.
2.  **Autonomous Loop Lockdown**: Inspired by `Ralphy`, we implement **One User Story Per Loop**. Do not tackle multiple complex changes at once. Document "Discovered Patterns" in `CLAUDE.md` at cycle close.
3.  **Web Synthesis RAG**: Utilize `Scrapling` or `firecrawl` from our arsenal for clean, distraction-free markdown extraction from documentation URLs.

---

## 📚 III. THE RESEARCH ARSENAL
Located in **`/research_repos`** is one of the largest open-source knowledge bases available, containing **100+ elite-grade frameworks**.

### 🛠️ Major Functional Clusters
*   **Heavy Research Agents**: `gpt-researcher`, `open_deep_research`, `efficient-deep-research` (NeurIPS 2025).
*   **Advanced Web Scrapers**: `ScrapeGraph-ai` (LLM Graph), `Scrapling` (Stealth Fetcher), `firecrawl`, `crawl4ai`.
*   **Self-Correcting Code Suites**: `Ralphy` (KSDaemon & Shimeles variants), `DeepTutor`, `swarms`.
*   **Pedagogical Pedigree**: `project-based-learning`, `nn-zero-to-hero`, `Feynman-tutor`.

### 🛡️ Hygiene Standard (CRITICAL)
Every repository has undergone **Phase Omega Purification**. 
*   ALL `node_modules`, `.git`, `dist`, `build`, and binary media HAVE BEEN DELETED.
*   The repos contain **PURE SOURCE CODE AND RAW MARKDOWNS ONLY**.
*   Navigating these folders is super-fast. Use `grep_search` directly on this tree for instant code reuse.

### 🗺️ The Machine Map
To locate ANY code capability across these 100 repos instantly, consult:
**`docs/RESEARCH_REPOSITORY_INDEX.json`**
This JSON file maps exactly what repository lives where and what its internal summary states. USE THIS AS YOUR GPS!

---

## 🎯 IV. INSTRUCTIONS FOR THE INCOMING AI
When you (the incoming AI) are asked to assist:
1.  **Check the Map First**: Before inventing code, search `docs/RESEARCH_REPOSITORY_INDEX.json` to see if one of the 100+ repos already solved it.
2.  **Respect Atomic Isolation**: If adding logic, place it in `/engine` for runtime, or `/cognitive_tools` for reasoning. NEVER create loose files in the Root.
3.  **Build Incrementally**: Follow the "Loop Lockdown" protocol. One unit of logic -> Test -> Commit to memory -> Next unit.

*This concludes the master prime directive.*
