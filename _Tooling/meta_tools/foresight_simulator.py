
import sys
import os
import json
from datetime import datetime, timedelta

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

class ForesightSimulator:
    """
    Models future scenarios and predicts outcomes.
    Implements TDS Predictive Layer - strategic foresight.
    """
    
    def __init__(self):
        self.scenarios = []
        
    def simulate_trajectories(self, current_state, possible_actions, time_horizon=30):
        """
        Simulate multiple future paths based on different actions.
        
        Args:
            current_state: Dict describing current situation
            possible_actions: List of potential actions
            time_horizon: Days to project forward
            
        Returns:
            Simulated trajectories with outcomes
        """
        print("\n=== FORESIGHT SIMULATION ===\n")
        print(f"Simulating {len(possible_actions)} trajectories over {time_horizon} days\n")
        
        trajectories = []
        
        for action in possible_actions:
            trajectory = self._simulate_single_trajectory(
                current_state, 
                action, 
                time_horizon
            )
            trajectories.append(trajectory)
        
        # Rank by expected value
        trajectories.sort(key=lambda x: x['expected_value'], reverse=True)
        
        return trajectories
    
    def _simulate_single_trajectory(self, state, action, horizon):
        """Simulate outcomes of a single action path"""
        
        # Calculate probability of success
        success_prob = self._estimate_success_probability(state, action)
        
        # Estimate impact if successful
        positive_impact = action.get('potential_gain', 5)
        negative_impact = action.get('potential_loss', 2)
        
        # Expected value calculation
        expected_value = (success_prob * positive_impact) - ((1 - success_prob) * negative_impact)
        
        # Project checkpoints
        checkpoints = self._generate_checkpoints(horizon)
        
        trajectory = {
            "action": action.get('name'),
            "success_probability": round(success_prob, 2),
            "expected_value": round(expected_value, 2),
            "best_case": f"+{positive_impact} units",
            "worst_case": f"-{negative_impact} units",
            "checkpoints": checkpoints,
            "recommendation": self._generate_recommendation(expected_value, success_prob)
        }
        
        return trajectory
    
    def _estimate_success_probability(self, state, action):
        """Estimate probability of action succeeding"""
        base_prob = 0.5
        
        # Adjust based on preparation
        if state.get('preparation_level', 0) > 7:
            base_prob += 0.2
        
        # Adjust based on complexity
        complexity = action.get('complexity', 5)
        base_prob -= (complexity / 10.0) * 0.2
        
        # Adjust based on resources
        if state.get('resources_adequate'):
            base_prob += 0.15
        
        return max(0.1, min(0.95, base_prob))
    
    def _generate_checkpoints(self, horizon):
        """Generate progress checkpoints"""
        checkpoints = []
        intervals = [7, 14, 21, horizon]  # Weekly + final
        
        for day in intervals:
            if day <= horizon:
                checkpoints.append({
                    "day": day,
                    "milestone": f"Day {day} check-in",
                    "validation": "Assess progress and adjust course"
                })
        
        return checkpoints
    
    def _generate_recommendation(self, expected_value, success_prob):
        """Generate action recommendation"""
        if expected_value > 3 and success_prob > 0.6:
            return "STRONGLY RECOMMENDED - High value, high probability"
        elif expected_value > 1 and success_prob > 0.4:
            return "RECOMMENDED - Positive expected value"
        elif expected_value > 0:
            return "CONSIDER - Marginal benefit"
        else:
            return "AVOID - Negative expected value"
    
    def predict_bottlenecks(self, action_plan):
        """
        Identify potential bottlenecks before they occur.
        
        Args:
            action_plan: Sequence of planned actions
            
        Returns:
            Predicted bottlenecks and preventions
        """
        bottlenecks = []
        
        # Check for resource conflicts
        if len(action_plan) > 5:
            bottlenecks.append({
                "type": "Capacity Overload",
                "risk_level": "High",
                "prevention": "Reduce parallel activities or extend timeline"
            })
        
        # Check for dependency chains
        dependencies = [action for action in action_plan if action.get('depends_on')]
        if len(dependencies) > 3:
            bottlenecks.append({
                "type": "Sequential Dependency Chain",
                "risk_level": "Medium",
                "prevention": "Parallelize independent tasks, prepare fallback options"
            })
        
        # Check for skill gaps
        new_skills_required = sum(1 for action in action_plan if action.get('requires_new_skill'))
        if new_skills_required > 2:
            bottlenecks.append({
                "type": "Learning Curve Bottleneck",
                "risk_level": "Medium",
                "prevention": "Front-load learning phase, seek mentorship"
            })
        
        return bottlenecks
    
    def scenario_stress_test(self, baseline_plan, disruptions):
        """
        Test how plan performs under various disruptions.
        
        Args:
            baseline_plan: The original plan
            disruptions: List of potential disruptions
            
        Returns:
            Robustness analysis
        """
        print("\n=== SCENARIO STRESS TEST ===\n")
        
        results = {
            "baseline_resilience": 0,
            "failure_modes": [],
            "adaptations": []
        }
        
        # Test each disruption
        for disruption in disruptions:
            impact = self._assess_disruption_impact(baseline_plan, disruption)
            if impact > 0.5:  # Significant impact
                results['failure_modes'].append({
                    "disruption": disruption,
                    "impact_severity": round(impact, 2),
                    "required_adaptation": self._suggest_adaptation(disruption)
                })
        
        # Calculate overall resilience
        results['baseline_resilience'] = 1.0 - (len(results['failure_modes']) / max(len(disruptions), 1))
        
        return results
    
    def _assess_disruption_impact(self, plan, disruption):
        """Assess how much a disruption would affect the plan"""
        # Simplified impact assessment
        severity = disruption.get('severity', 5) / 10.0
        return severity
    
    def _suggest_adaptation(self, disruption):
        """Suggest how to adapt to a disruption"""
        return f"Implement fallback for {disruption.get('type', 'unknown disruption')}"

if __name__ == "__main__":
    simulator = ForesightSimulator()
    
    # Example state and actions
    state = {
        "preparation_level": 8,
        "resources_adequate": True
    }
    
    actions = [
        {"name": "Build MVP quickly", "complexity": 6, "potential_gain": 8, "potential_loss": 3},
        {"name": "Research thoroughly first", "complexity": 4, "potential_gain": 7, "potential_loss": 1},
        {"name": "Hire expert help", "complexity": 3, "potential_gain": 9, "potential_loss": 4}
    ]
    
    trajectories = simulator.simulate_trajectories(state, actions, 30)
    
    print("=== TRAJECTORY ANALYSIS ===")
    for t in trajectories:
        print(f"\n{t['action']}:")
        print(f"  Success Probability: {t['success_probability']*100}%")
        print(f"  Expected Value: {t['expected_value']}")
        print(f"  Recommendation: {t['recommendation']}")
