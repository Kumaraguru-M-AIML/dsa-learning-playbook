# C:\Master db\R&D workspace\NEW\probabilistic_epistemics.py
import os
import sys
import math
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class ProbabilisticEpistemics:
    """
    CQ Mythos v4 Probabilistic Epistemics Engine.
    Eschews binary determinism by tracking continuous belief states,
    uncertainty masses, ambiguity scores, and semantic plausibility bounds.
    """
    def __init__(self):
        pass

    def compute_belief_state(self, candidate_nodes):
        """
        Maps continuous belief values [0.0 to 1.0] across multiple competing hypotheses,
        incorporating semantic plausibility and tracking overall uncertainty mass.
        """
        print(f"\n🔮 [Probabilistic Epistemics] Analyzing belief state for {len(candidate_nodes)} hypotheses...")
        
        belief_state = {}
        total_unnormalized_score = 0.0
        
        # Calculate raw belief scores incorporating confidence and plausibility
        for node in candidate_nodes:
            label = node.get("hypothesis_label", "Unknown")
            conf = float(node.get("confidence", 1.0))
            plausibility = float(node.get("plausibility", 1.0))
            
            # Belief is the product of probabilistic confidence and semantic plausibility
            raw_belief = conf * plausibility
            node["raw_belief"] = raw_belief
            total_unnormalized_score += raw_belief

        # Normalize belief scores to establish a proper probability distribution
        if total_unnormalized_score > 0.0:
            for node in candidate_nodes:
                label = node["hypothesis_label"]
                normalized_prob = node["raw_belief"] / total_unnormalized_score
                belief_state[label] = round(normalized_prob, 4)
        else:
            # All hypotheses are completely implausible/poisoned
            for node in candidate_nodes:
                belief_state[node["hypothesis_label"]] = 0.0

        # Calculate Ambiguity Score (Shannon Entropy of the probability distribution)
        entropy = 0.0
        for prob in belief_state.values():
            if prob > 0.0:
                entropy -= prob * math.log2(prob)
                
        # Uncertainty Mass is the remaining probability allocated to 'Unknown/Implausible' space
        uncertainty_mass = 1.0 - max(belief_state.values()) if belief_state else 1.0
        
        print(f"  ├─ Active Belief Distribution: {json.dumps(belief_state)}")
        print(f"  ├─ Ambiguity Score (Entropy): {entropy:.4f}")
        print(f"  └─ Uncertainty Mass: {uncertainty_mass:.4f}")
        
        return {
            "belief_distribution": belief_state,
            "ambiguity_score": round(entropy, 4),
            "uncertainty_mass": round(uncertainty_mass, 4)
        }

if __name__ == "__main__":
    epistemics = ProbabilisticEpistemics()
    
    # Simulating three competing hypotheses with different confidences and plausibilities
    hypotheses = [
        {"hypothesis_label": "Hypothesis A (RTX 3050 6GB)", "confidence": 0.9, "plausibility": 1.0},
        {"hypothesis_label": "Hypothesis B (RTX 4050)", "confidence": 0.8, "plausibility": 0.6},
        {"hypothesis_label": "Hypothesis C (Poisoned_Node)", "confidence": 1.0, "plausibility": 0.0} # Poisoned node filtered by Semantic Guard
    ]
    
    metrics = epistemics.compute_belief_state(hypotheses)
    print("\n🎯 Compiled Probabilistic Metrics:")
    print(json.dumps(metrics, indent=4))
