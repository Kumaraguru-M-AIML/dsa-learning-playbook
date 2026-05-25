# 🌌 OPENSPEC WORKFLOWS — DEFINITIVE REFERENCE GUIDE

**Date:** May 8, 2026  
**Compiled By:** ANTIGRAVITY / SYSTEM Co-Ordinator  
**Status:** WORKSPACE INTEGRATED  

---

> [!NOTE]
> **OpenSpec** is an elite, specification-driven development framework used in professional software engineering. It bridges the gap between raw user requests, formal requirements (specs), and actual code implementation by breaking down features into three distinct lifecycle phases.

---

## 🔄 The OpenSpec Lifecycle Flow

```text
[ 🚀 1. PROPOSAL ] ───► [ ⚙️ 2. APPLY ] ───► [ 📦 3. ARCHIVE ]
Scaffold & Design        Code & Implement         Merge & Permanent Spec
 (No Code Written)        (Task Checklist)          (Archive History)
```

---

## 🚀 1. `/openspec-proposal` (Scaffold and Plan)

* **What it is**: The **planning and architectural design** phase.
* **When to use it**: When you want to introduce a major new capability, refactor a large subsystem, or design a new feature from scratch before writing any code.
* **What it does**:
  1. Creates a dedicated folder at `openspec/changes/<change-id>/`.
  2. Scaffolds a `proposal.md` outlining the feature goals and acceptance criteria.
  3. Scaffolds a `design.md` detailing architectural trade-offs, system impact, and file dependencies.
  4. Scaffolds a `tasks.md` checklist containing small, verifiable, chronological steps.
  5. **No actual codebase files are modified yet**, ensuring absolute alignment on the design before writing code!

---

## ⚙️ 2. `/openspec-apply` (Code and Implement)

* **What it is**: The **active coding and execution** phase.
* **When to use it**: When the proposal has been reviewed and approved, and we are ready to write the actual code.
* **What it does**:
  1. Triggers the step-by-step execution of the `tasks.md` checklist.
  2. Implements the minimal, highly scoped code changes required to satisfy the design.
  3. Marks tasks as completed (`- [x]`) as we proceed.
  4. Verifies the code through tests and tooling to ensure stability.

---

## 📦 3. `/openspec-archive` (Merge and Deploy)

* **What it is**: The **finalization and permanent logging** phase.
* **When to use it**: When the code is fully implemented, tested, and validated, and we want to permanently merge it into the system's core specifications.
* **What it does**:
  1. Commits the temporary change proposal to history by moving it into `changes/archive/`.
  2. Automatically merges and updates your core permanent system requirements under the main `openspec/specs/` folder.
  3. Validates the final codebase state to ensure zero system conflicts or regressions.

---

## 📊 Summary Matrix

| Workflow Command | Primary Purpose | Code Modified? | Directory Impact |
| :--- | :--- | :--- | :--- |
| **`/openspec-proposal`** | **Design & Plan** | ❌ No | Creates `openspec/changes/<change-id>/` |
| **`/openspec-apply`** | **Code & Execute** | ✔️ Yes | Modifies codebase files + marks tasks as complete |
| **`/openspec-archive`** | **Log & Finalize** | ❌ No | Moves change folders into `/archive/` and updates `/specs/` |

---
> [!TIP]
> Having these workflows pre-configured in your workspace allows us to build extremely robust, production-grade systems with high rigor and zero architectural drift!

---
*OpenSpec Workflow Guide Compiled Under ARIA Operating Rules v2.7 | Persistent Tracking Enabled*
