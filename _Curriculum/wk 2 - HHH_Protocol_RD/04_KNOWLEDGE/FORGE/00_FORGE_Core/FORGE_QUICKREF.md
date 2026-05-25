---
tags: [forge, quickref, cheatsheet]
aliases: [FORGE Quickref, Cheat Sheet]
---

# ⚡ FORGE QUICK REFERENCE

## THE PROCESS
```
READ → CAPTURE → ATOMIC NOTE → CONNECT → MODEL → PLAYBOOK
           F         O            R          G        E
```

## WHICH TEMPLATE DO I USE?

| I have... | Use... | File |
|-----------|--------|------|
| One useful idea from a source | Atomic Note | `_TEMPLATE_Atomic.md` |
| 3+ related ideas forming a pattern | Mental Model | `_TEMPLATE_Model.md` |
| A model I want to act on | Playbook | `_TEMPLATE_Playbook.md` |
| An idea I want to test in real life | Experiment | `_TEMPLATE_Experiment.md` |
| A new book/source to process | Source Queue | `SOURCE_QUEUE.md` |

## THE ATOMIC NOTE CHECKLIST
- [ ] Title is a **claim** (not a topic)
- [ ] "So what?" is answered clearly
- [ ] "When to use" trigger condition is written
- [ ] At least **one link** to another note

## THE MENTAL MODEL CHECKLIST
- [ ] Built from **3+ Atomic Notes**
- [ ] Mechanism is clear (what causes what)
- [ ] Limitations are listed (when it breaks)
- [ ] Linked Atomic Notes are listed

## THE PLAYBOOK CHECKLIST
- [ ] Built from **at least 1 Mental Model**
- [ ] Every step has a **"Why"**
- [ ] Execution checklist is copyable
- [ ] Metrics are defined

## KEY RULES (NEVER BREAK THESE)
1. **"So What?" filter** — if you can't say why it matters, skip it
2. **Deploy condition** — every Atomic Note needs a trigger
3. **Connect or it dies** — every note must link to ≥1 other note
4. **Model before Playbook** — no shortcuts
5. **Log every change** to `FORGE_CHANGELOG.md`

## WHERE THINGS LIVE
```
FORGE_System/
├── 00_FORGE_Core/     ← Manual + Templates + Changelog
├── 01_Atomic_Notes/   ← Individual insights
├── 02_Mental_Models/  ← Frameworks + patterns
├── 03_Playbooks/      ← Action protocols
├── 04_Concept_Map/    ← Master web of connections
├── 05_Source_Queue/   ← What to read next
└── 06_Experiments/    ← Real-life tests
```

## THE WEEKLY REVIEW (10 minutes)
1. Review new Atomic Notes — any patterns?
2. Synthesize patterns → update or create a Mental Model
3. Update `FORGE_CONCEPT_MAP.md` with new connections
4. Pick next source from Queue
5. Update `FORGE_CHANGELOG.md` if you improved anything
