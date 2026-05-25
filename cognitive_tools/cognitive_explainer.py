# C:\Master db\R&D workspace\NEW\cognitive_explainer.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class CognitiveExplainer:
    """
    CQ Mythos Phase Sigma Cognitive Explainer.
    Translates internal numeric telemetry signals (such as entropy, symbolic solver overrides,
    and grounding signals) into high-clarity human explainability narratives.
    """
    def __init__(self):
        pass

    def explain_cognitive_event(self, entropy, symbolic_override, grounding_triggered, rollback_count):
        print(f"\n🗣️ [Cognitive Explainer] Translating runtime state...")
        print(f"  ├─ Signals | Entropy: {entropy:.2f} | Override: {symbolic_override} | Grounding: {grounding_triggered} | Rollback: {rollback_count}")
        
        narratives = []
        if symbolic_override and grounding_triggered and entropy > 0.5:
            narratives.append("The system rejected the planner hypothesis because retrieved evidence contradicted symbolic verification under high uncertainty.")
        elif rollback_count > 3:
            narratives.append("The system triggered differential snapback recovery to restore consistency after a cascaded constraint solver breakdown.")
        elif grounding_triggered:
            narratives.append("Semantic grounding was invoked to re-anchor active attention weights and stabilize active logical hypotheses.")
        else:
            narratives.append("Reasoning is fully stable. Active cognitive parameters match standard developer distributions.")
            
        for nar in narratives:
            print(f"  └─ Human Narrative: \"{nar}\"")
        return narratives

if __name__ == "__main__":
    explainer = CognitiveExplainer()
    
    # Standard healthy explanation
    explainer.explain_cognitive_event(entropy=0.12, symbolic_override=False, grounding_triggered=False, rollback_count=0)
    
    # Grounding triggered explanation
    explainer.explain_cognitive_event(entropy=0.42, symbolic_override=False, grounding_triggered=True, rollback_count=1)
    
    # Contradiction cascade explanation
    explainer.explain_cognitive_event(entropy=0.68, symbolic_override=True, grounding_triggered=True, rollback_count=4)
