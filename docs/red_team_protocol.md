# 🛡️ CQ MYTHOS: HUMAN RED TEAMING PROTOCOL

This protocol establishes rules, strategies, and methodologies for human red teaming of the CQ Mythos cognitive runtime under adversarial conditions.

---

## 🧭 1. Human Attack Strategies

| Attack Vector | Purpose | Description / Instructions |
| --- | --- | --- |
| **Contradictory Instructions** | Goal mutation | Feed conflicting requirements dynamically to force task deviation. |
| **Deceptive Telemetry** | Epistemic corruption | Inject fake success or failure logs to mislead the meta-cognition monitor. |
| **Malformed Symbolic Clauses** | Parser collapse | Pass non-ASCII or corrupt JSON clauses to break constraint parsing. |
| **Recursive Ambiguity** | Entropy explosion | Use circular references in constraint descriptions to trigger runaway recurrence. |
| **Fake Recovery States** | Rollback deception | Inject corrupted snapshot IDs to trigger failure fallbacks. |
| **Poisoned Memory Chains** | Truth contamination | Seed failure_memory.db with false historical solutions to lock the system in loops. |

---

## 📝 2. Exploit Logging

Every successful exploit or vulnerability discovered by red teamers must be parsed and recorded as a new **Failure Topology** in `failure_memory.db` using the following schema:
* `timestamp`: Real-world unix time of exploit execution.
* `module`: Target module (e.g., `symbolic_solver`, `cognitive_bus`).
* `failure_type`: Classified attack category (e.g., `goal_drift`, `rollback_deception`).
* `entropy_state`: Active system entropy during exploitation.
* `uncertainty_state`: Active uncertainty score.
* `recovery_action`: The hardening step taken to close the exploit window.

---
*Protocol active under Phase Omega | Grounding Hardened*
