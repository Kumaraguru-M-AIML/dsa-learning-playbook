"""
EPISODIC MEMORY SYSTEM - Evolution Phase 5.5
--------------------------------------------
Implements "Narrative Intelligence" for Vahn.
Instead of storing just raw data points (decisions), we store "Episodes" (Stories).

An Episode contains:
- The Journey: Sequence of goals and outcomes.
- The Struggle: Difficulty and self-correction volume.
- The Breakthrough: The "Aha!" moment.
- The Moral: High-level abstract lesson.

This allows Vahn to say: "I remember when I struggled with X until I realized Y."
"""

import json
import os
from typing import List, Dict, Any
from datetime import datetime

class EpisodicMemory:
    def __init__(self, memory_file=".agent/episodic_memory.json"):
        self.memory_file = memory_file
        self.episodes = []
        self.current_episode = {
            "start_time": datetime.now().isoformat(),
            "events": [],
            "emotions": [], # successes/failures/surprises
            "breakthroughs": []
        }
        self.load_episodes()

    def load_episodes(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    self.episodes = json.load(f)
                print(f"[MEMORY] Loaded {len(self.episodes)} narrative chapters.")
            except:
                self.episodes = []

    def save_episodes(self):
        os.makedirs(os.path.dirname(self.memory_file), exist_ok=True)
        with open(self.memory_file, 'w') as f:
            json.dump(self.episodes, f, indent=2)

    def log_event(self, description: str, type: str = "action"):
        """Log a significant event in the current episode."""
        self.current_episode['events'].append({
            "timestamp": datetime.now().isoformat(),
            "description": description,
            "type": type
        })

    def log_breakthrough(self, insight: str):
        """Log an 'Aha!' moment."""
        self.current_episode['breakthroughs'].append(insight)
        self.log_event(f"Breakthrough: {insight}", type="breakthrough")

    def end_episode(self, summary: str = "Session Complete"):
        """
        Close the current episode, compress it into a high-level narrative, 
        and store it.
        """
        if not self.current_episode['events']:
            return

        # High-Level Encoding (Compression)
        episode_summary = {
            "id": len(self.episodes) + 1,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "summary": summary,
            "event_count": len(self.current_episode['events']),
            "key_breakthroughs": self.current_episode['breakthroughs'],
            "narrative_arc": self._generate_narrative_arc()
        }

        self.episodes.append(episode_summary)
        self.save_episodes()
        
        # Reset current episode
        self.current_episode = {
            "start_time": datetime.now().isoformat(),
            "events": [],
            "emotions": [],
            "breakthroughs": []
        }
        print(f"[MEMORY] Episode #{episode_summary['id']} encoded and stored.")

    def _generate_narrative_arc(self) -> str:
        """
        Heuristic method to describe the 'feel' of the session.
        """
        events = self.current_episode['events']
        breakthroughs = self.current_episode['breakthroughs']
        
        if len(breakthroughs) > 0:
            return "Discovery Arc - Started with exploration, faced challenges, and achieved a breakthrough."
        elif len(events) > 10:
            return "Grind Phase - Heavy execution and detailed work."
        else:
            return "Quick Sync - Brief interaction or check-in."

    def recall_narratives(self) -> List[str]:
        """Return high-level summaries of past episodes."""
        return [f"Episode {e['id']} ({e['date']}): {e['summary']} - {e['narrative_arc']}" for e in self.episodes[-5:]]
