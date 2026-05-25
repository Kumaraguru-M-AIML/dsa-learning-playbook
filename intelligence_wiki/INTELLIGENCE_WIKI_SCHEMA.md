# 📘 INTELLIGENCE WIKI SCHEMA & PROTOCOLS

## 🎯 Core Directive
Maintain a structured, interlinked, self-compounding Markdown knowledge base. Unlike RAG, where knowledge is re-derived every query, this Wiki stores synthesized permanent knowledge.

## 📂 Directory Structure
* `/raw_sources/`: Read-only storage for external PDFs, articles, notes.
* `/wiki_entries/`: The synthesized interlinked markdown files.
* `index.md`: Main entry catalog mapped by topic.
* `log.md`: Strict chronological audit ledger of edits/ingestions.

## 🔄 Maintenance Workflows

### 1. INGEST Protocol
When new information arrives:
1. Save source to `/raw_sources/`.
2. Create a Summary Page inside `/wiki_entries/`.
3. Scan current `/wiki_entries/` for overlap. Update existing pages with new contradictions or confirmations.
4. Log the ingestion in `log.md`.

### 2. QUERY Synthesis
When asked complex cross-domain questions:
1. Consult `index.md` to find relevant entry files.
2. Construct answer by fusing valid entries.
3. *CRITICAL*: If the answer generates useful new connective insight, write that answer back to `/wiki_entries/` as a new permanent synthesis page.

### 3. LINTING Procedure
Once per interval, the agent reviews the wiki to:
* Fix dead internal wiki links `[[Link]]`.
* Identify concept gaps that need further research.
* Reconcile contradictory statements across different summaries.

## 📜 Notation Standards
Use traditional internal link formatting for automated compatibility with Obsidian graph view:
* Usage: `See [[Memory Architecture]] for structural detail.`

## 📡 External Bridge Integration
*   **Primary Connector**: `research_repos/AgriciDaniel-claude-obsidian`
*   **Operational Duty**: Use this bridge to synchronize our local `/wiki_entries/` directly into a functioning Obsidian graph visualization.


---
*Initialized: May 11, 2026 | Concept Ingested from External Payload.*
