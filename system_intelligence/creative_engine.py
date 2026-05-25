"""
Vahn's Creative Intelligence Engine
Implements divergent and lateral thinking strategies to generate novel solutions.
"""

import random
from typing import List, Dict, Any

class CreativeThinkingEngine:
    def __init__(self, brain=None):
        self.brain = brain
        self.scamper_prompts = {
            "substitute": ["What can I substitute in this architecture?", "Can I use a different rule?", "What if I replaced the core algorithm?"],
            "combine": ["Can I combine two disparate tools?", "What if research and coding happened simultaneously?", "Can I merge this goal with a past success?"],
            "adapt": ["What else is like this?", "Does biology offer a parallel?", "How would a game engine handle this?"],
            "modify": ["Can I change the meaning?", "What if I exaggerate the constraint?", "Can I change the attributes?"],
            "put_to_other_use": ["Can this bug be a feature?", "Can I use the testing framework for exploration?"],
            "eliminate": ["What can I remove?", "What is strictly unnecessary?", "Can I simplify to the extreme?"],
            "reverse": ["What if I try the opposite?", "Can I work backwards from the result?", "What if the output becomes the input?"]
        }
        
    def generate_random_stimulus(self) -> str:
        """provides a random concept to force lateral connections."""
        concepts = ["Water", "Gravity", "Mirror", "Swarm", "Crystal", "Shadow", "Virus", "Clock", "Shield", "Bridge"]
        return random.choice(concepts)

    def scamper_technique(self, problem: str) -> List[str]:
        """
        Applies SCAMPER technique to a problem statement.
        Returns a list of provocative questions/ideas.
        """
        ideas = []
        for technique, prompts in self.scamper_prompts.items():
            prompt = random.choice(prompts)
            ideas.append(f"[{technique.upper()}] {prompt} -> regarding: {problem}")
        return ideas

    def lateral_shift(self, current_thought_process: List[str]) -> str:
        """
        Forces a lateral shift in thinking when stuck.
        Uses random stimulus or provocation.
        """
        stimulus = self.generate_random_stimulus()
        provocation = f"LATERAL PROVOCATION: Consider the concept of '{stimulus}'."
        connection = f"How does '{stimulus}' relate to the current logic chain?"
        
        return f"{provocation} {connection}"

    def six_hats_thinking(self, hat_color: str, context: str) -> str:
        """
        Applies de Bono's Six Thinking Hats.
        """
        hats = {
            "white": "Focus on available data and facts.",
            "red": "Focus on intuition and 'gut feeling' without justification.",
            "black": "Focus on risks, caution, and why it might fail.",
            "yellow": "Focus on benefits, optimism, and value.",
            "green": "Focus on creativity, alternatives, and new ideas.",
            "blue": "Focus on process control and organization."
        }
        
        instruction = hats.get(hat_color.lower(), hats['blue'])
        return f"[{hat_color.upper()} HAT] {instruction} Context: {context}"
