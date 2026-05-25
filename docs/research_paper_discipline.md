# 📑 CQ MYTHOS: RESEARCH PAPER DISCIPLINE GUIDELINES

This document serves as our internal disciplinary standard to prevent "architecture marketing theater" and ensure that all empirical claims survive adversarial validation.

---

## 🚫 1. Essential Writing Standards

### 1.1 Threats to Validity
Every publication-grade report must explicitly list:
- **Synthetic Bias**: The risk that simulated environments yield overly optimistic results compared to physical production.
- **Evaluation Coupling**: The risk of circular validation when the system evaluates its own logic.
- **Benchmark Contamination**: The risk of testing on samples that were present in the model's training data.

### 1.2 Negative Results
- **Mandatory Reporting**: We must explicitly publish where our mechanisms fail (such as high-noise environments where symbolic solvers deadlock).
- **No Glossing**: If a component has an ROI under 0.20, its inclusion must be defended on compute efficiency grounds.

### 1.3 Failure Case Audits
- Maintain a running database of active failure traces, especially **Type-II (Stable Hallucinations)**, to prevent developer confirmation bias.

---
*Published under ARIA Research Group v6.0-Sigma-Validation | Bounded Cognition Active*
