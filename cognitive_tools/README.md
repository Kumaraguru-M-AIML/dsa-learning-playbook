# Exocortex: Cognitive Tools Suite

This directory contains pure-logic engines to augment the Agent's neural networks.

## Components

### 1. `deduction.py` (The Logician)
*   **Type**: Deterministic / Forward-Chaining
*   **Use Case**: Solving dependencies, checking permissions, validating strict rules.
*   **Example**: "If A requires B, and B is missing, then A cannot run."

### 2. `inference.py` (The Bayesian)
*   **Type**: Probabilistic / Bayesian Update
*   **Use Case**: Diagnosing obscure bugs.
*   **Example**: "The server is slow. Is it the DB or the Network? New evidence updates the probability."

### 3. `reasoning.py` (The Strategist)
*   **Type**: Structured Chain-of-Thought
*   **Use Case**: Planning complex refactors or creating debugging strategies.
*   **Logic**: Forces `Observation -> Hypothesis -> Action` flow.

## Integration
These tools are designed to be imported by the main Agent (`research_tools/main.py`) to give it "Executive Function".
