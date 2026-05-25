"""
SOL-AGENT: JEPA-INSPIRED WORLD MODEL ENGINE
=============================================
Phase 8.5: The Latent Prediction Layer

This module implements a JEPA-inspired architecture for Sol-Agent.
Instead of VL-JEPA's vision encoders, this adapts the core JEPA principles
to an AUTONOMOUS AGENT context:

    VL-JEPA Concept          -> Sol-Agent Adaptation
    -----------------------------------------------
    X-Encoder (Vision)       -> Context Encoder (goal + environment state)
    Y-Encoder (Target Text)  -> Outcome Encoder (desired end-state)
    Predictor (Core)         -> Latent Predictor (predicts outcome embedding from context)
    Y-Decoder (Inference)    -> Action Decoder (converts latent prediction to executable plan)

Key Principle:
    Instead of predicting tokens (slow, wasteful), we predict
    ABSTRACT REPRESENTATIONS of outcomes in a latent space.
    Only decode to text/actions when needed (Selective Decoding).
"""

import json
import os
import math
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple


class LatentEmbedding:
    """
    A lightweight representation of a concept in latent space.
    This is NOT a neural tensor - it's a structured semantic vector
    that captures the *meaning* of a goal/action/outcome.
    """

    def __init__(self, concepts: List[str], constraints: List[str] = None,
                 confidence: float = 0.5):
        self.concepts = concepts
        self.constraints = constraints or []
        self.confidence = confidence
        self.timestamp = datetime.now().isoformat()

        # Generate a deterministic hash as the "embedding ID"
        raw = "|".join(sorted(concepts)) + "|" + "|".join(sorted(self.constraints))
        self.embedding_id = hashlib.sha256(raw.encode()).hexdigest()[:16]

    def distance(self, other: 'LatentEmbedding') -> float:
        """
        Compute semantic distance between two embeddings.
        Uses Jaccard similarity on concept sets.
        Lower = more similar.
        """
        set_a = set(self.concepts)
        set_b = set(other.concepts)

        if not set_a and not set_b:
            return 0.0

        intersection = set_a & set_b
        union = set_a | set_b
        jaccard = len(intersection) / len(union) if union else 0.0

        return 1.0 - jaccard  # Distance = 1 - similarity

    def similarity(self, other: 'LatentEmbedding') -> float:
        """Higher = more similar."""
        return 1.0 - self.distance(other)

    def to_dict(self) -> Dict:
        return {
            "embedding_id": self.embedding_id,
            "concepts": self.concepts,
            "constraints": self.constraints,
            "confidence": self.confidence,
            "timestamp": self.timestamp
        }


class JEPAWorldModel:
    """
    The JEPA-Inspired World Model for Sol-Agent.

    Architecture:
        1. Context Encoder:  Goal + Environment -> Latent Embedding (S_context)
        2. Outcome Encoder:  Desired Result -> Latent Embedding (S_target)
        3. Predictor:        S_context -> S_predicted (predict outcome in latent space)
        4. Action Decoder:   S_predicted -> Executable Plan (only when needed)

    Training Signal:
        Minimize distance(S_predicted, S_target) across historical episodes.
        This is the InfoNCE-style objective adapted for agent decisions.
    """

    # Semantic concept vocabulary
    CONCEPT_MAP = {
        "RESEARCH":   ["find", "search", "lookup", "query", "investigate", "study", "explore", "read"],
        "PLANNING":   ["plan", "structure", "roadmap", "steps", "prepare", "organize", "design", "architect"],
        "CODING":     ["code", "write", "script", "refactor", "implement", "fix", "build", "debug", "deploy"],
        "ANALYSIS":   ["analyze", "check", "scan", "evaluate", "assess", "monitor", "review", "audit"],
        "SYNC":       ["sync", "update", "log", "align", "match", "bridge", "merge", "consolidate"],
        "LEARNING":   ["learn", "master", "practice", "drill", "absorb", "memorize", "understand"],
        "CREATION":   ["create", "generate", "produce", "construct", "compose", "design", "craft"],
        "EVOLUTION":  ["evolve", "upgrade", "improve", "enhance", "optimize", "refine", "advance"],
        "MEMORY":     ["remember", "recall", "persist", "store", "archive", "retrieve", "history"],
        "REASONING":  ["reason", "think", "deduce", "infer", "logic", "conclude", "solve"],
    }

    # Constraint vocabulary
    CONSTRAINT_MAP = {
        "DATA_INTEGRITY":         ["sync", "update", "data", "log", "record"],
        "ARCHITECTURAL_STABILITY": ["evolution", "phase", "upgrade", "refactor", "system"],
        "TIME_PRESSURE":          ["urgent", "now", "immediately", "fast", "quick", "asap"],
        "CROSS_DRIVE":            ["drive", "workspace", "global", "omnipresence", "portable"],
        "LEARNING_CONTINUITY":    ["lesson", "module", "mastery", "progress", "curriculum"],
    }

    def __init__(self, memory_path: str = None):
        self.memory_path = Path(memory_path) if memory_path else \
            Path(__file__).parent.parent / ".agent" / "jepa_world_model.json"

        # The learned causal graph: maps context embeddings to outcome embeddings
        self.causal_memory: List[Dict] = []
        self._load_memory()

    def _load_memory(self):
        """Load learned causal episodes from disk."""
        if self.memory_path.exists():
            try:
                with open(self.memory_path, 'r') as f:
                    data = json.load(f)
                self.causal_memory = data.get("episodes", [])
            except Exception:
                self.causal_memory = []

    def _save_memory(self):
        """Persist learned episodes."""
        os.makedirs(self.memory_path.parent, exist_ok=True)
        with open(self.memory_path, 'w') as f:
            json.dump({
                "model": "JEPA-WorldModel-v1",
                "last_updated": datetime.now().isoformat(),
                "total_episodes": len(self.causal_memory),
                "episodes": self.causal_memory
            }, f, indent=2)

    # ═══════════════════════════════════════════════════════
    #  ENCODER 1: CONTEXT ENCODER (X-Encoder analog)
    # ═══════════════════════════════════════════════════════

    def encode_context(self, goal: str, environment: Dict = None) -> LatentEmbedding:
        """
        Encode a goal + environment state into a latent embedding.
        This is the X-Encoder in VL-JEPA terms.
        """
        goal_lower = goal.lower()
        concepts = []
        constraints = []

        # Extract concepts
        for concept, keywords in self.CONCEPT_MAP.items():
            if concept.lower() in goal_lower or any(kw in goal_lower for kw in keywords):
                concepts.append(concept)

        # Extract constraints
        for constraint, keywords in self.CONSTRAINT_MAP.items():
            if any(kw in goal_lower for kw in keywords):
                constraints.append(constraint)

        # If no concepts detected, infer from general intent
        if not concepts:
            concepts.append("REASONING")  # Default: thinking

        # Factor in environment
        if environment:
            if environment.get("drives_online", 0) < 3:
                constraints.append("CROSS_DRIVE")
            if environment.get("brain_active") is False:
                constraints.append("ARCHITECTURAL_STABILITY")

        return LatentEmbedding(
            concepts=concepts,
            constraints=constraints,
            confidence=0.5 + (len(concepts) * 0.05)
        )

    # ═══════════════════════════════════════════════════════
    #  ENCODER 2: OUTCOME ENCODER (Y-Encoder analog)
    # ═══════════════════════════════════════════════════════

    def encode_outcome(self, outcome_description: str) -> LatentEmbedding:
        """
        Encode a desired outcome into latent space.
        This is the Y-Encoder in VL-JEPA terms.
        """
        return self.encode_context(outcome_description)

    # ═══════════════════════════════════════════════════════
    #  PREDICTOR: THE CORE (Predictor analog)
    # ═══════════════════════════════════════════════════════

    def predict(self, context_embedding: LatentEmbedding) -> LatentEmbedding:
        """
        Given a context embedding, predict the outcome embedding.
        This is the CORE of JEPA: prediction in latent space.

        Uses historical causal memory to find similar contexts
        and predict likely outcomes.
        """
        if not self.causal_memory:
            # Cold start: predict identity (outcome = context)
            return LatentEmbedding(
                concepts=context_embedding.concepts.copy(),
                constraints=context_embedding.constraints.copy(),
                confidence=0.4  # Low confidence on cold start
            )

        # Find most similar historical context
        best_match = None
        best_similarity = -1.0

        for episode in self.causal_memory:
            hist_context = LatentEmbedding(
                concepts=episode.get("context_concepts", []),
                constraints=episode.get("context_constraints", [])
            )

            sim = context_embedding.similarity(hist_context)
            if sim > best_similarity:
                best_similarity = sim
                best_match = episode

        if best_match and best_similarity > 0.3:
            # Predict based on historical outcome
            predicted = LatentEmbedding(
                concepts=best_match.get("outcome_concepts", context_embedding.concepts),
                constraints=best_match.get("outcome_constraints", []),
                confidence=best_similarity * best_match.get("success_rate", 0.5)
            )
            return predicted
        else:
            # No good match: return context as prediction with low confidence
            return LatentEmbedding(
                concepts=context_embedding.concepts.copy(),
                constraints=context_embedding.constraints.copy(),
                confidence=0.35
            )

    # ═══════════════════════════════════════════════════════
    #  DECODER: ACTION DECODER (Y-Decoder analog)
    # ═══════════════════════════════════════════════════════

    def decode_to_plan(self, predicted_embedding: LatentEmbedding) -> List[Dict]:
        """
        Selective Decoding: Convert a latent prediction into an executable plan.
        Only called when action is needed (not for pure simulation).

        This is the Y-Decoder in VL-JEPA terms.
        """
        plan = []

        for i, concept in enumerate(predicted_embedding.concepts, 1):
            step = {
                "step": i,
                "intent": concept,
                "confidence": predicted_embedding.confidence,
                "constraint_aware": predicted_embedding.constraints,
            }

            # Map concept to action template
            if concept == "RESEARCH":
                step["action"] = "Gather information and analyze sources"
            elif concept == "PLANNING":
                step["action"] = "Decompose goal into structured phases"
            elif concept == "CODING":
                step["action"] = "Write or modify code implementation"
            elif concept == "ANALYSIS":
                step["action"] = "Evaluate current state and identify gaps"
            elif concept == "SYNC":
                step["action"] = "Synchronize data across drives and memory"
            elif concept == "LEARNING":
                step["action"] = "Execute learning protocol with practice"
            elif concept == "CREATION":
                step["action"] = "Generate new artifact or resource"
            elif concept == "EVOLUTION":
                step["action"] = "Run self-improvement cycle"
            elif concept == "MEMORY":
                step["action"] = "Retrieve and consolidate historical data"
            elif concept == "REASONING":
                step["action"] = "Apply logical deduction to solve problem"
            else:
                step["action"] = f"Execute {concept} operation"

            plan.append(step)

        return plan

    # ═══════════════════════════════════════════════════════
    #  SIMULATION: RUN IN LATENT SPACE
    # ═══════════════════════════════════════════════════════

    def simulate(self, goal: str, environment: Dict = None) -> Dict:
        """
        Full JEPA cycle: Encode -> Predict -> Assess.
        Runs entirely in latent space. No tokens generated.

        Returns a simulation report with predicted success and risks.
        """
        # 1. Encode context
        context_emb = self.encode_context(goal, environment)

        # 2. Predict outcome in latent space
        predicted_emb = self.predict(context_emb)

        # 3. Assess prediction quality
        risk_factors = []
        if predicted_emb.confidence < 0.4:
            risk_factors.append("LOW_CONFIDENCE: Cold start or novel goal")
        if "ARCHITECTURAL_STABILITY" in predicted_emb.constraints:
            risk_factors.append("STABILITY_RISK: System architecture may be affected")
        if "CROSS_DRIVE" in predicted_emb.constraints:
            risk_factors.append("SYNC_RISK: Cross-drive operation required")
        if "TIME_PRESSURE" in predicted_emb.constraints:
            risk_factors.append("TIME_RISK: Urgency may compromise quality")

        return {
            "goal": goal,
            "context_embedding": context_emb.to_dict(),
            "predicted_embedding": predicted_emb.to_dict(),
            "predicted_success": predicted_emb.confidence,
            "risk_factors": risk_factors,
            "requires_decoding": predicted_emb.confidence >= 0.4,
            "recommendation": "PROCEED" if predicted_emb.confidence >= 0.4 else "RETHINK",
            "timestamp": datetime.now().isoformat()
        }

    # ═══════════════════════════════════════════════════════
    #  LEARNING: UPDATE CAUSAL MEMORY
    # ═══════════════════════════════════════════════════════

    def learn_episode(self, goal: str, outcome: str, success: bool,
                      confidence: float = 0.5):
        """
        Learn from a completed episode.
        Stores the context->outcome mapping in causal memory.
        This is the training signal for the predictor.
        """
        context_emb = self.encode_context(goal)
        outcome_emb = self.encode_outcome(outcome)

        episode = {
            "timestamp": datetime.now().isoformat(),
            "goal": goal,
            "outcome": outcome,
            "success": success,
            "success_rate": confidence if success else confidence * 0.5,
            "context_concepts": context_emb.concepts,
            "context_constraints": context_emb.constraints,
            "outcome_concepts": outcome_emb.concepts,
            "outcome_constraints": outcome_emb.constraints,
        }

        self.causal_memory.append(episode)

        # Keep memory bounded (last 500 episodes)
        if len(self.causal_memory) > 500:
            self.causal_memory = self.causal_memory[-500:]

        self._save_memory()

    def get_stats(self) -> Dict:
        """Return model statistics."""
        total = len(self.causal_memory)
        successes = sum(1 for e in self.causal_memory if e.get("success"))

        return {
            "model": "JEPA-WorldModel-v1",
            "total_episodes": total,
            "success_rate": successes / total if total > 0 else 0.0,
            "concept_vocabulary": len(self.CONCEPT_MAP),
            "constraint_vocabulary": len(self.CONSTRAINT_MAP),
        }


if __name__ == "__main__":
    # Test the JEPA World Model
    model = JEPAWorldModel()

    # Simulate a goal
    result = model.simulate("Learn SQL NULL handling and sync progress to E: drive")
    print(json.dumps(result, indent=2))

    # Learn from an episode
    model.learn_episode(
        goal="Research VL-JEPA architecture",
        outcome="Successfully gathered JEPA technical details",
        success=True,
        confidence=0.9
    )

    print(f"\nModel Stats: {json.dumps(model.get_stats(), indent=2)}")
