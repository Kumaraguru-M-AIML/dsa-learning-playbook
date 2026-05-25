"""
Vahn's Reward System - Inspired by DeepSeek R1
Evaluates candidates based on Accuracy, Format, and Structural Integrity.
"""

import re
import json
import os
from typing import Dict, List, Any

class VahnRewardModel:
    def __init__(self, workspace_path: str = "."):
        self.workspace_path = workspace_path
        
    def calculate_group_rewards(self, candidates: List[Dict[str, Any]], goal: str) -> List[float]:
        """
        Calculates rewards for a group of candidates (GRPO style).
        Includes standard accuracy/format + meta-cognitive quality markers.
        """
        rewards = []
        for candidate in candidates:
            reward = 0.0
            
            # 1. ACCURACY REWARD (Highest Weight)
            reward += self._check_accuracy(candidate, goal) * 0.5
            
            # 2. FORMAT & META-COGNITION REWARD (Emergent Behavior)
            reward += self._check_format(candidate) * 0.1
            reward += self._check_metacognition(candidate) * 0.2
            
            # 3. CONSISTENCY & READABILITY
            reward += self._check_readability(candidate) * 0.2
            
            rewards.append(reward)
            
        return rewards

    def _check_accuracy(self, candidate: Dict[str, Any], goal: str) -> float:
        """
        Verify if the candidate solution actually achieves the goal.
        In this system, it checks if proposed tools exist and if the action plan is logical.
        """
        score = 0.0
        
        # Check tool validity
        tools = candidate.get('tools_to_use', [])
        if tools:
            score += 0.3
            # Bonus if tools are specialized for the goal
            if any(kw in goal.lower() for kw in ["research", "paper", "arxiv"]) and any("research" in t for t in tools):
                score += 0.2
        
        # Check action plan depth
        plan = candidate.get('action_plan', [])
        if len(plan) >= 3:
            score += 0.3
        
        # Check confidence self-assessment
        if candidate.get('confidence', 0) > 0.7:
             score += 0.2
             
        return min(1.0, score)

    def _check_format(self, candidate: Dict[str, Any]) -> float:
        """
        Enforce DeepSeek style formatting.
        Vahn uses 'reasoning_loop' instead of literal <think> tags in the JSON structure,
        but we check for structural presence.
        """
        score = 0.0
        
        # Check for reasoning structure
        if 'reasoning' in candidate and len(candidate['reasoning']) > 0:
            score += 0.5
            
        # Check for meta-data structure (R1 style tracking)
        if 'reasoning_loop' in candidate or 'grpo_metadata' in candidate:
            score += 0.5
            
        return score

    def _check_readability(self, candidate: Dict[str, Any]) -> float:
        """
        Check for code blocks, language consistency, and clear steps.
        """
        score = 0.5 # Baseline
        
        plan = candidate.get('action_plan', [])
        for step in plan:
            if 'action' in step and len(step['action']) > 10:
                score += 0.1
            if 'expected_output' in step:
                score += 0.1
                
        return min(1.0, score)

    def _check_metacognition(self, candidate: Dict[str, Any]) -> float:
        """
        DEEPSEEK R1 SPECIAL: Identify and reward "Aha!" moments in reasoning traces.
        Rewards tokens of: self-correction, verification, and reflection.
        """
        score = 0.0
        reasoning = " ".join(candidate.get('reasoning', [])).lower()
        
        # Meta-cognitive markers (Aha! moments)
        aha_markers = [
            "wait", "rethink", "actually", "correction", 
            "verification", "reflection", "recalculating",
            "let me check", "alternative", "issue found"
        ]
        
        matches = sum(1 for marker in aha_markers if marker in reasoning)
        
        # Reward multiple markers but cap it to avoid gaming the system
        if matches >= 1:
            score += 0.5
        if matches >= 3:
            score += 0.3
        if matches >= 5:
            score += 0.2
            
        return score
