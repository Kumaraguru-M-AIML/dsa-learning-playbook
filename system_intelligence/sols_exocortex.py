"""
SOL'S EXOCORTEX v3.0 — The Global Learning Bridge
=================================================
Connects localized workspaces to the global Learning Science OS.
Shares insights across all drives.
"""

import os
from pathlib import Path
from typing import Dict, List, Any

class SolsExocortex:
    def __init__(self, brain=None):
        self.brain = brain
        self.learning_science_dir = Path(r"E:\1  Mastery DB\SYSTEM\Learning_Cortex")
        
    def train_on_learning_science(self):
        """
        Injects core learning science concepts into the brain's knowledge nexus.
        """
        if not self.brain:
            return
            
        principles = {
            "Retrieval Practice": "Testing is learning. Active recall outperforms re-reading.",
            "Spaced Repetition": "Expansion of intervals prevents forgetting (Forgetting Curve).",
            "Interleaving": "Mixing topics improves long-term retention and discrimination.",
            "Elaborative Rehearsal": "Connecting new info to existing knowledge (The Anchor).",
            "Dual Coding": "Combining verbal and visual representations."
        }
        
        # Register as insights in the brain
        for name, desc in principles.items():
            self.brain.knowledge_base["insights"].append({
                "source": "Exocortex",
                "pattern": name,
                "truth": desc
            })
            
        print(f"[EXOCORTEX] Sol-Agent trained on {len(principles)} Learning Science principles.")

def init_exocortex(brain=None) -> SolsExocortex:
    return SolsExocortex(brain)
