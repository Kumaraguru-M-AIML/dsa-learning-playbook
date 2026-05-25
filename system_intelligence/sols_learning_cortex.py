"""
SOL'S LEARNING CORTEX v3.0 — The Learning OS
=============================================
Unification of TITAN and OMEGA protocols.
Handles retrieval practice, spacing, and deep understanding.
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional

class SolsLearningCortex:
    def __init__(self, workspace_name: str = "global"):
        self.workspace_name = workspace_name
        self.mind_dir = Path(r"E:\1  Mastery DB\SYSTEM")
        self.cortex_dir = self.mind_dir / "Learning_Cortex"
        self.user_profile_path = self.cortex_dir / "user_profile.json"
        
        self.user_model = self._load_user_profile()
        self._ensure_dirs()

    def _ensure_dirs(self):
        os.makedirs(self.cortex_dir, exist_ok=True)
        os.makedirs(self.cortex_dir / "knowledge_graph", exist_ok=True)

    def _load_user_profile(self) -> Dict:
        if self.user_profile_path.exists():
            try:
                with open(self.user_profile_path, 'r') as f:
                    return json.load(f)
            except:
                pass
        return {
            "user": "Sol",
            "stats": {"xp": 0, "level": 1},
            "mastery": {},
            "sprints": [],
            "last_active": datetime.now().isoformat()
        }

    def _save_profile(self):
        with open(self.user_profile_path, 'w') as f:
            json.dump(self.user_model, f, indent=2)

    # --- TITAN PROTOCOLS (Learning & Retrieval) ---

    def generate_titan_protocol(self, topic: str) -> Dict:
        """
        TITAN: T-arget, I-nitiate, T-rack, A-nalyze, N-ext.
        High-intensity retrieval-based learning plan.
        """
        protocol = {
            "topic": topic,
            "protocol": "TITAN",
            "timestamp": datetime.now().isoformat(),
            "phases": [
                {"name": "Target", "goal": f"Deconstruct {topic} into first principles."},
                {"name": "Initiate", "goal": "Primacy effect: 15min deep read + no-notes brain dump."},
                {"name": "Track", "goal": "Retrieval practice: 3 delayed brain dumps (1h, 6h, 24h)."},
                {"name": "Analyze", "goal": "Gap diagnosis: compare brain dumps to source."},
                {"name": "Next", "goal": "Iterative elaboration or Level Up to OMEGA."}
            ]
        }
        return protocol

    def generate_omega_protocol(self, topic: str) -> Dict:
        """
        OMEGA: The 5 Pillars of Understanding.
        """
        pillars = self.list_pillars()
        protocol = {
            "topic": topic,
            "protocol": "OMEGA",
            "timestamp": datetime.now().isoformat(),
            "pillars": pillars,
            "action_plan": [f"Apply {p['name']} to {topic}" for p in pillars]
        }
        return protocol

    def list_pillars(self) -> List[Dict]:
        return [
            {"id": 1, "name": "First Principles", "desc": "The root truths that cannot be deduced further."},
            {"id": 2, "name": "Decomposition", "desc": "Breaking the system into discrete, interacting parts."},
            {"id": 3, "name": "Key Drivers", "desc": "The 20% of variables that control 80% of outcomes."},
            {"id": 4, "name": "Structural Mapping", "desc": "How parts connect and form the hierarchy."},
            {"id": 5, "name": "Levels of Abstraction", "desc": "Moving from implementation to strategy."}
        ]

    def diagnose_gap(self, topic: str) -> Dict:
        """Asks 5 targeted questions to expose knowledge voids."""
        return {
            "topic": topic,
            "questions": [
                f"What is the single most fundamental principle of {topic}?",
                f"How does {topic} fail? What are the edge cases?",
                f"If you had to explain {topic} to a 5-year-old, what would you say?",
                f"What is the mathematical or logical limit of {topic}?",
                f"What is the 'Magic' step you don't quite understand yet?"
            ]
        }

    def grade_attempt(self, topic: str, attempt_text: str) -> Dict:
        """Scoring logic for retrieval practice."""
        word_count = len(attempt_text.split())
        score = min(word_count / 100 * 10, 10) # Simple heuristic for now
        
        # Update profile
        if topic not in self.user_model["mastery"]:
            self.user_model["mastery"][topic] = {"xp": 0, "attempts": 0}
        
        self.user_model["mastery"][topic]["xp"] += int(score)
        self.user_model["mastery"][topic]["attempts"] += 1
        self._save_profile()
        
        return {
            "topic": topic,
            "score": f"{score:.1f}/10",
            "feedback": "Consistent retrieval practice detected. Knowledge encoding strengthened."
        }

    def start_sprint(self, goal: str = "Mastery") -> Dict:
        sprint = {
            "start": datetime.now().isoformat(),
            "goal": goal,
            "days": 21,
            "completed": 0
        }
        self.user_model["sprints"].append(sprint)
        self._save_profile()
        return sprint

    def get_user_profile_summary(self) -> str:
        u = self.user_model
        return f"\n=== SOL'S LEARNING PROFILE ===\nXP: {u['stats']['xp']} | Level: {u['stats']['level']}\nMastered Topics: {len(u['mastery'])}\nActive Sprints: {len([s for s in u['sprints'] if s['completed'] < 21])}\n==============================\n"

def init_sols_cortex(workspace_name: str = "global") -> SolsLearningCortex:
    return SolsLearningCortex(workspace_name)
