
import sys
import os
from datetime import datetime

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

try:
    from cognitive_tools.inference import InferenceEngine
except ImportError:
    InferenceEngine = None

class TacticalOptimizer:
    """
    Prioritizes and optimizes short-term actions for maximum impact.
    Implements TDS Tactical Layer - execution intelligence.
    """
    
    def __init__(self):
        self.bayesian = InferenceEngine() if InferenceEngine else None
        
    def prioritize_tasks(self, tasks, context=None):
        """
        Rank tasks by impact, effort, and urgency using multi-factor analysis.
        
        Args:
            tasks: List of task dictionaries with 'name', 'impact', 'effort', 'urgency'
            context: Current state/constraints
            
        Returns:
            Prioritized task list with scores
        """
        print("\n=== TACTICAL OPTIMIZATION ===\n")
        
        scored_tasks = []
        for task in tasks:
            score = self._calculate_priority_score(task)
            task['priority_score'] = score
            task['recommendation'] = self._generate_recommendation(task, score)
            scored_tasks.append(task)
        
        # Sort by priority score (highest first)
        scored_tasks.sort(key=lambda x: x['priority_score'], reverse=True)
        
        print(f"Optimized {len(scored_tasks)} tasks")
        return scored_tasks
    
    def _calculate_priority_score(self, task):
        """
        Calculate priority using weighted factors:
        - Impact (40%)
        - Urgency (30%)
        - Inverse Effort (20%)
        - Dependencies (10%)
        """
        impact = task.get('impact', 5)  # 1-10 scale
        urgency = task.get('urgency', 5)  # 1-10 scale  
        effort = task.get('effort', 5)  # 1-10 scale (higher = more effort)
        
        # Normalize to 0-1 scale
        impact_norm = impact / 10.0
        urgency_norm = urgency / 10.0
        effort_inverse = (10 - effort) / 10.0  # Invert so lower effort = higher score
        
        # Weighted score
        score = (
            impact_norm * 0.4 +
            urgency_norm * 0.3 +
            effort_inverse * 0.2 +
            0.1  # Base dependency factor
        )
        
        return round(score * 100, 2)  # Scale to 0-100
    
    def _generate_recommendation(self, task, score):
        """Generate action recommendation based on score"""
        if score >= 70:
            return "DO NOW - High priority"
        elif score >= 50:
            return "SCHEDULE SOON - Medium priority"
        elif score >= 30:
            return "DEFER - Low priority"
        else:
            return "ELIMINATE - Not worth doing"
    
    def optimize_daily_schedule(self, available_hours, energy_curve):
        """
        Create optimal daily schedule based on energy levels and task requirements.
        
        Args:
            available_hours: Hours available for work
            energy_curve: Dict mapping hour->energy_level (1-10)
            
        Returns:
            Optimized schedule
        """
        schedule = []
        
        # Map task types to optimal energy levels
        task_types = {
            "Creative Work": {"min_energy": 7, "duration": 2},
            "Deep Focus": {"min_energy": 6, "duration": 1.5},
            "Communication": {"min_energy": 5, "duration": 1},
            "Admin Tasks": {"min_energy": 3, "duration": 0.5},
            "Learning": {"min_energy": 6, "duration": 1}
        }
        
        for task_type, requirements in task_types.items():
            # Find time slots matching energy requirements
            best_time = self._find_optimal_time_slot(energy_curve, requirements['min_energy'])
            if best_time:
                schedule.append({
                    "task": task_type,
                    "start_time": best_time,
                    "duration": requirements['duration'],
                    "energy_match": "Optimal"
                })
        
        return schedule
    
    def _find_optimal_time_slot(self, energy_curve, min_energy):
        """Find time with sufficient energy level"""
        for hour, energy in energy_curve.items():
            if energy >= min_energy:
                return hour
        return None

if __name__ == "__main__":
    optimizer = TacticalOptimizer()
    
    # Example tasks
    tasks = [
        {"name": "Build new feature", "impact": 8, "urgency": 6, "effort": 7},
        {"name": "Fix critical bug", "impact": 9, "urgency": 10, "effort": 4},
        {"name": "Update documentation", "impact": 4, "urgency": 3, "effort": 2},
        {"name": "Research new library", "impact": 6, "urgency": 4, "effort": 5}
    ]
    
    prioritized = optimizer.prioritize_tasks(tasks)
    
    print("\n=== PRIORITIZED TASKS ===")
    for task in prioritized:
        print(f"{task['priority_score']}% - {task['name']} ({task['recommendation']})")
