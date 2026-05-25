# C:\Master db\R&D workspace\NEW\reasoning_narrator.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class ReasoningNarrator:
    """
    CQ Mythos v6.0 Reasoning Narrator.
    Translates internal numeric telemetry signals (entropy, contradictions, rollback events)
    into high-clarity, human-interpretable explanatory reasoning narratives and timelines.
    """
    def __init__(self):
        pass

    def narrate_cognitive_event(self, entropy, contradictions, rollback_occurred, source_module):
        """Generates a semantic narrative explanation of a specific cognitive event."""
        print(f"\n📖 [Reasoning Narrator] Generating semantic explanation trace...")
        
        narrative = ""
        if rollback_occurred:
            narrative = (
                f"Rollback triggered by '{source_module}' because contradiction density "
                f"or active entropy ({entropy:.4f}) exceeded hard safety thresholds after "
                f"unresolved symbolic constraints conflict."
            )
        else:
            if entropy < 0.2:
                narrative = (
                    f"System is executing stable, high-confidence processing in '{source_module}'. "
                    f"Belief state is fully anchored with low entropy ({entropy:.4f}) and zero contradiction density."
                )
            else:
                narrative = (
                    f"System is experiencing elevated cognitive load in '{source_module}' (Entropy: {entropy:.4f}). "
                    f"Dynamic re-grounding has been requested to stabilize active hypotheses."
                )
                
        print(f"  └─ Explanation: \"{narrative}\"")
        return narrative

if __name__ == "__main__":
    narrator = ReasoningNarrator()
    
    # Narrating a stable high-confidence event
    narrator.narrate_cognitive_event(entropy=0.12, contradictions=0, rollback_occurred=False, source_module="evidence_graph")
    
    # Narrating a high-load warning event
    narrator.narrate_cognitive_event(entropy=0.45, contradictions=1, rollback_occurred=False, source_module="meta_cognition")
    
    # Narrating a hard rollback event
    narrator.narrate_cognitive_event(entropy=0.78, contradictions=2, rollback_occurred=True, source_module="symbolic_solver")
