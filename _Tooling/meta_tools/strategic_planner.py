
import sys
import os
import json
from datetime import datetime, timedelta

# Add root to path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

try:
    from cognitive_tools.reasoning import ReasoningEngine
    from cognitive_tools.deduction import LogicEngine
except ImportError:
    ReasoningEngine = None
    LogicEngine = None

class StrategicPlanner:
    """
    Long-term goal decomposition and strategic thinking.
    Implements TDS Strategic Layer - translating vision into actionable roadmaps.
    """
    
    def __init__(self):
        self.brain = ReasoningEngine() if ReasoningEngine else None
        self.logic = LogicEngine() if LogicEngine else None
        
    def decompose_goal(self, ultimate_goal, time_horizon_days=90):
        """
        Breaks down a long-term goal into phases, milestones, and constraints.
        
        Args:
            ultimate_goal: The high-level objective
            time_horizon_days: Planning window
            
        Returns:
            Strategic roadmap with phases, milestones, dependencies
        """
        print(f"\n=== STRATEGIC PLANNING: {ultimate_goal} ===")
        print(f"Time Horizon: {time_horizon_days} days\n")
        
        if self.brain:
            self.brain.observe(f"Ultimate Goal: {ultimate_goal}")
            self.brain.hypothesize("This goal requires multiple phases with dependencies", 0.9)
            self.brain.deduce_action("Decompose into: Foundation -> Development -> Optimization -> Mastery")
        
        # Strategic decomposition logic
        phases = self._generate_phases(ultimate_goal, time_horizon_days)
        milestones = self._generate_milestones(phases)
        constraints = self._identify_constraints(ultimate_goal)
        critical_path = self._calculate_critical_path(phases, milestones)
        
        roadmap = {
            "goal": ultimate_goal,
            "created": datetime.now().isoformat(),
            "horizon_days": time_horizon_days,
            "phases": phases,
            "milestones": milestones,
            "constraints": constraints,
            "critical_path": critical_path
        }
        
        if self.brain:
            self.brain.conclude(f"Strategic roadmap generated with {len(phases)} phases and {len(milestones)} milestones")
            print(self.brain.generate_summary())
        
        return roadmap
    
    def _generate_phases(self, goal, horizon):
        """Generate strategic phases based on goal complexity"""
        # Split timeline into 4 quarters
        phase_duration = horizon // 4
        
        phases = [
            {
                "name": "Foundation",
                "duration_days": phase_duration,
                "focus": "Build core capabilities and infrastructure",
                "success_criteria": ["Basic competency established", "Tools acquired", "Environment prepared"]
            },
            {
                "name": "Development", 
                "duration_days": phase_duration,
                "focus": "Develop main skills and assets",
                "success_criteria": ["Core skills functional", "Primary systems operational", "Initial results visible"]
            },
            {
                "name": "Optimization",
                "duration_days": phase_duration,
                "focus": "Refine processes and improve efficiency",
                "success_criteria": ["Performance metrics improving", "Bottlenecks removed", "Automation implemented"]
            },
            {
                "name": "Mastery",
                "duration_days": phase_duration,
                "focus": "Achieve excellence and teach others",
                "success_criteria": ["Goal achieved", "Results reproducible", "Knowledge transferable"]
            }
        ]
        
        return phases
    
    def _generate_milestones(self, phases):
        """Generate checkpoints for each phase"""
        milestones = []
        for i, phase in enumerate(phases):
            milestones.append({
                "phase": phase["name"],
                "checkpoint": f"Phase {i+1} Complete",
                "validation": "All success criteria met"
            })
        return milestones
    
    def _identify_constraints(self, goal):
        """Identify potential blockers and resource requirements"""
        return {
            "resources": ["Time", "Tools", "Knowledge", "Environment"],
            "risks": ["Scope creep", "Motivation loss", "External dependencies"],
            "prerequisites": ["Clear definition of success", "Baseline metrics", "Feedback loop"]
        }
    
    def _calculate_critical_path(self, phases, milestones):
        """Determine the sequence of critical activities"""
        return [
            "Define success metrics",
            "Complete Foundation phase", 
            "Validate core capabilities",
            "Complete Development phase",
            "Measure improvement",
            "Complete Optimization phase",
            "Achieve mastery criteria"
        ]

if __name__ == "__main__":
    planner = StrategicPlanner()
    roadmap = planner.decompose_goal("Master Machine Learning Engineering", 90)
    
    print("\n=== STRATEGIC ROADMAP ===")
    print(json.dumps(roadmap, indent=2))
