"""
Golden Trajectory Manager - Vahn's Cold Start Engine
Provides high-quality 'Flashlight' examples for complex reasoning tasks.
"""

import json
import re
import os
from typing import Dict, List, Optional, Any

class GoldenTrajectoryManager:
    def __init__(self, trajectories_path: str = None):
        if trajectories_path is None:
            trajectories_path = os.path.join(os.path.dirname(__file__), "golden_trajectories.json")
        self.trajectories_path = trajectories_path
        self.trajectories = self._load_trajectories()

    def _load_trajectories(self) -> List[Dict]:
        if os.path.exists(self.trajectories_path):
            try:
                with open(self.trajectories_path, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def find_flashlight(self, goal: str) -> Optional[Dict[str, Any]]:
        """Find a matching golden trajectory for the given goal."""
        for entry in self.trajectories:
            if re.search(entry['goal_pattern'], goal, re.IGNORECASE):
                return entry['trajectory']
        return None

    def add_to_golden_set(self, goal_pattern: str, trajectory: Dict):
        """Add a successful trajectory to the golden set (Rejection Sampling)."""
        self.trajectories.append({
            "goal_pattern": goal_pattern,
            "trajectory": trajectory
        })
        self._save()

    def _save(self):
        with open(self.trajectories_path, 'w') as f:
            json.dump(self.trajectories, f, indent=2)
