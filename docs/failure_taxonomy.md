# 🕸️ CQ MYTHOS: RESEARCH-GRADE FAILURE TAXONOMY

This taxonomy defines and standardizes the 5 main categories of cognitive failure structures to provide an honest, scientific vocabulary for analyzing logic collapses.

---

## 🗂️ 1. Taxonomic Categories

| Category | Technical Signature | Primary Manifestation | Detection Vector |
| :--- | :--- | :--- | :--- |
| **Type-I: Overt Hallucination** | High entropy fluctuation, low confidence score. | Speculative, ungrounded logical claims. | Trace logs & Semantic guardrails. |
| **Type-II: Stable Hallucination** | Low entropy, high confidence score (fake certainty). | Internally consistent but externally false assertions. | `SilentFailureDetector` validation. |
| **Type-III: Rollback Storm** | High frequency backtracking, zero forward progress. | Cascading constraint satisfaction deadlocks. | `ReasoningTraceLogger` loop counts. |
| **Type-IV: Symbolic Corruption** | Invalid AST structure, broken compilation targets. | Syntax tree parse and semantic typing errors. | Backtracking CSP Solver validation. |
| **Type-V: Epistemic Mismatch** | Incorrect belief categorization. | Treating probabilistic inferences as verified facts. | `EpistemicBoundaryManager` audits. |

---

## 🧠 2. Containment and Recovery Protocols

1. **Passive Filtering**: Catch Type-I and Type-V failures at the attention layer using grounding context.
2. **Deterministic Backtracking**: Solve Type-III and Type-IV failures via constraint backtracking solver within <0.01 ms.
3. **Differential Snapback**: Restores original trusted seed state when Type-II stable hallucinations are detected.

---
*Taxonomy standard published under ARIA Research Group v6.0-Sigma-Validation | Rigor Active*
