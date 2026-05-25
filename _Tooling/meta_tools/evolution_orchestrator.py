
import sys
import os
import json
import argparse
from datetime import datetime

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

try:
    from meta_tools.strategic_planner import StrategicPlanner
    from meta_tools.tactical_optimizer import TacticalOptimizer
    from meta_tools.learning_engine import LearningEngine
    from meta_tools.insight_generator import InsightGenerator
    from meta_tools.foresight_simulator import ForesightSimulator
    from meta_tools.self_diagnostic import SelfDiagnostic
    from cognitive_tools.reasoning import ReasoningEngine
except ImportError as e:
    print(f"Import Error: {e}")
    sys.exit(1)

class EvolutionOrchestrator:
    """
    Master controller that orchestrates all meta-tools for systematic self-improvement.
    Implements the complete TDS Recursive Improvement Cycle.
    
    This is the "brain" that continuously upgrades the entire system.
    """
    
    def __init__(self):
        # Initialize all meta-tools
        self.strategic_planner = StrategicPlanner()
        self.tactical_optimizer = TacticalOptimizer()
        self.learning_engine = LearningEngine()
        self.insight_generator = InsightGenerator()
        self.foresight = ForesightSimulator()
        self.diagnostic = SelfDiagnostic()
        self.reasoning = ReasoningEngine() if ReasoningEngine else None
        
        print("\n" + "="*60)
        print("  EVOLUTION ORCHESTRATOR v1.0 - TDS-X META-SYSTEM")
        print("="*60)
        
    def execute_improvement_cycle(self, goal, context=None):
        """
        Execute a complete improvement cycle:
        1. Diagnose current state
        2. Strategic planning
        3. Tactical optimization
        4. Generate insights
        5. Simulate outcomes
        6. Learn and upgrade
        
        Args:
            goal: High-level improvement goal
            context: Current context/constraints
            
        Returns:
            Complete improvement plan with actionable steps
        """
        print(f"\n>>> IMPROVEMENT CYCLE: {goal}\n")
        
        cycle_report = {
            "goal": goal,
            "started_at": datetime.now().isoformat(),
            "phases": {}
        }
        
        # PHASE 1: DIAGNOSE
        print("\n[1/6] DIAGNOSTIC PHASE")
        diagnostic_report = self.diagnostic.run_full_diagnostic()
        cycle_report['phases']['diagnostic'] = {
            "health": diagnostic_report['overall_health'],
            "issues": len(diagnostic_report['identified_issues']),
            "opportunities": len(diagnostic_report['optimization_opportunities'])
        }
        
        # PHASE 2: STRATEGIC PLANNING
        print("\n[2/6] STRATEGIC PLANNING PHASE")
        strategic_roadmap = self.strategic_planner.decompose_goal(goal, 90)
        cycle_report['phases']['strategic'] = {
            "phases": len(strategic_roadmap['phases']),
            "milestones": len(strategic_roadmap['milestones'])
        }
        
        # PHASE 3: TACTICAL OPTIMIZATION  
        print("\n[3/6] TACTICAL OPTIMIZATION PHASE")
        # Generate tasks from strategic phases
        tasks = self._generate_tasks_from_roadmap(strategic_roadmap)
        prioritized_tasks = self.tactical_optimizer.prioritize_tasks(tasks)
        cycle_report['phases']['tactical'] = {
            "total_tasks": len(prioritized_tasks),
            "high_priority": sum(1 for t in prioritized_tasks if t['priority_score'] >= 70)
        }
        
        # PHASE 4: INSIGHT GENERATION
        print("\n[4/6] INSIGHT GENERATION PHASE")
        # Gather data from diagnostic and planning
        data_sources = [
            {
                "source": "System Diagnostic",
                "domain": "System Health",
                "data": json.dumps(diagnostic_report['subsystems'])
            },
            {
                "source": "Strategic Plan",
                "domain": "Planning",
                "data": json.dumps(strategic_roadmap)
            }
        ]
        insights = self.insight_generator.generate_insights(data_sources)
        cycle_report['phases']['insights'] = {
            "cross_domain_patterns": len(insights['cross_domain_patterns']),
            "actionable_syntheses": len(insights['actionable_syntheses'])
        }
        
        # PHASE 5: FORESIGHT SIMULATION
        print("\n[5/6] FORESIGHT SIMULATION PHASE")
        # Simulate top 3 priority actions
        top_actions = prioritized_tasks[:3]
        current_state = {
            "preparation_level": int(diagnostic_report['overall_health'] / 10),
            "resources_adequate": diagnostic_report['overall_health'] > 75
        }
        trajectories = self.foresight.simulate_trajectories(current_state, top_actions, 30)
        cycle_report['phases']['foresight'] = {
            "trajectories_simulated": len(trajectories),
            "recommended_path": trajectories[0]['action'] if trajectories else None
        }
        
        # PHASE 6: LEARNING & SYNTHESIS
        print("\n[6/6] LEARNING & SYNTHESIS PHASE")
        if self.reasoning:
            self.reasoning.observe(f"Completed improvement cycle for: {goal}")
            self.reasoning.hypothesize("System now has actionable roadmap for improvement", 1.0)
            self.reasoning.deduce_action("Execute high-priority tasks from tactical optimization")
            self.reasoning.conclude("Continuous monitoring and adjustment required")
        
        # Create final action plan
        action_plan = self._synthesize_action_plan(
            prioritized_tasks,
            insights,
            trajectories,
            diagnostic_report
        )
        
        cycle_report['action_plan'] = action_plan
        cycle_report['completed_at'] = datetime.now().isoformat()
        
        return cycle_report
    
    def _generate_tasks_from_roadmap(self, roadmap):
        """Convert strategic phases into specific tasks"""
        tasks = []
        
        for phase in roadmap['phases']:
            # Create task for each phase
            task = {
                "name": f"Complete {phase['name']} Phase",
                "impact": 8,  # High impact for strategic phases
                "urgency": 7,
                "effort": 6,
                "complexity": 6,
                "potential_gain": 8,
                "potential_loss": 2
            }
            tasks.append(task)
        
        # Add diagnostic improvement tasks
        task = {
            "name": "Implement optimization opportunities",
            "impact": 7,
            "urgency": 6,
            "effort": 5,
            "complexity": 5,
            "potential_gain": 7,
            "potential_loss": 1
        }
        tasks.append(task)
        
        return tasks
    
    def _synthesize_action_plan(self, tasks, insights, trajectories, diagnostic):
        """Create final synthesized action plan"""
        plan = {
            "immediate_actions": [],
            "short_term": [],
            "long_term": [],
            "key_insights": [],
            "success_metrics": []
        }
        
        # Immediate actions (top 2 priority tasks)
        for task in tasks[:2]:
            if task['priority_score'] >= 70:
                plan['immediate_actions'].append({
                    "action": task['name'],
                    "priority": task['priority_score'],
                    "recommendation": task['recommendation']
                })
        
        # Short-term (next 3-5 tasks)
        for task in tasks[2:5]:
            plan['short_term'].append(task['name'])
        
        # Long-term (remaining tasks)
        plan['long_term'] = [t['name'] for t in tasks[5:]]
        
        # Key insights
        for synthesis in insights.get('actionable_syntheses', []):
            plan['key_insights'].append(synthesis['insight'])
        
        # Success metrics
        plan['success_metrics'] = [
            "System health > 90%",
            "All high-priority tasks completed",
            "Measurable improvement in performance metrics"
        ]
        
        return plan
    
    def weekly_upgrade_protocol(self):
        """
        Execute the TDS Weekly Upgrade Protocol.
        This implements the recursive self-improvement cycle.
        """
        print("\n" + "="*60)
        print("  WEEKLY UPGRADE PROTOCOL - TDS Recursive Improvement")
        print("="*60 + "\n")
        
        # Run diagnostic
        print(">>> MONDAY: System Analysis")
        diagnostic = self.diagnostic.run_full_diagnostic()
        
        # Identify upgrade targets
        print("\n>>> TUESDAY: Upgrade Planning")
        upgrades = diagnostic['upgrade_suggestions']
        
        # Execute top upgrade
        print("\n>>> WEDNESDAY: Implementation")
        if upgrades:
            top_upgrade = upgrades[0]
            print(f"Implementing: {top_upgrade['upgrade']}")
            print(f"Priority: {top_upgrade['priority']}")
            print("Steps:")
            for i, step in enumerate(top_upgrade['steps'], 1):
                print(f"  {i}. {step}")
        
        # Validate improvements
        print("\n>>> SUNDAY: Impact Assessment")
        print("Re-running diagnostics to measure improvement...")
        new_diagnostic = self.diagnostic.run_full_diagnostic()
        improvement = new_diagnostic['overall_health'] - diagnostic['overall_health']
        print(f"Health improvement: {improvement:+.1f}%")
        
        return {
            "before_health": diagnostic['overall_health'],
            "after_health": new_diagnostic['overall_health'],
            "improvement": improvement,
            "upgrades_implemented": len(upgrades)
        }

def main():
    parser = argparse.ArgumentParser(description="Evolution Orchestrator - TDS-X Meta-System")
    parser.add_argument("goal", help="High-level improvement goal")
    parser.add_argument("--mode", choices=['cycle', 'weekly'], default='cycle',
                       help="Mode: 'cycle' for single improvement cycle, 'weekly' for protocol")
    
    args = parser.parse_args()
    
    orchestrator = EvolutionOrchestrator()
    
    if args.mode == 'weekly':
        result = orchestrator.weekly_upgrade_protocol()
        print("\n=== WEEKLY PROTOCOL COMPLETE ===")
        print(json.dumps(result, indent=2))
    else:
        result = orchestrator.execute_improvement_cycle(args.goal)
        
        print("\n" + "="*60)
        print("  IMPROVEMENT CYCLE COMPLETE")
        print("="*60)
        
        print("\n=== IMMEDIATE ACTIONS ===")
        for action in result['action_plan']['immediate_actions']:
            print(f"- [{action['priority']}%] {action['action']}")
        
        print("\n=== KEY INSIGHTS ===")
        for insight in result['action_plan']['key_insights']:
            print(f"- {insight}")
        
        print("\n=== SUCCESS METRICS ===")
        for metric in result['action_plan']['success_metrics']:
            print(f"- {metric}")

if __name__ == "__main__":
    main()
