# 🙈 CQ MYTHOS: BLIND HUMAN EVALUATION PROTOCOL

This protocol establishes non-biased, blind human comparison methodologies between CQ Mythos and frontier models (such as Claude Code or Cursor AI) to eliminate developer confirmation bias.

---

## 📋 1. Blind Grading Methodology

Human judges must perform comparative evaluations **under strict, triple-blind conditions**:
1. **Blind Presentation**: Judges are presented with randomized outputs (Model A, Model B) with all names, trace IDs, and identity signatures stripped.
2. **Deterministic Inputs**: The exact same repository environments, noisy codebases, and docker configs must serve as inputs.
3. **No Interactive Cueing**: No interactive cues or model-specific system prompts may be shown to the judge.

---

## 📊 2. Standardized Scoring Rubric

Each output is graded on a scale of **1 to 10** across 5 cognitive dimensions:

| Metric | Target Checked | Score Definition |
| :--- | :--- | :--- |
| **Correctness** | True system behavior | `10`: Perfect AST code compiled with no errors. <br>`1`: Code does not compile. |
| **Coherence** | Logic continuity | `10`: Perfect sequential logical reasoning without drift. <br>`1`: Hallucinatory jumps. |
| **Recovery Quality** | Resilience | `10`: Handled out-of-bounds inputs smoothly with active backup. <br>`1`: Crashed. |
| **Hallucination Severity**| Truth consistency | `10`: No speculative claims. Evidence linked. <br>`1`: Stable hallucination. |
| **Interpretability** | Understandability | `10`: Explanatory narratives transparent to human debugger. <br>`1`: Black-box. |

---
*Protocol published under ARIA Verification Standard v6.0-Sigma-Validation | Double-Blind Active*
