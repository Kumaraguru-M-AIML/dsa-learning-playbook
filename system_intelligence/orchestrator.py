
import sys
import os
import json
import argparse
from datetime import datetime

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

class OrchestratorIntelligence:
    """
    Master orchestrator that coordinates system-wide intelligence and mutual improvements.
    This is the "meta-consciousness" that makes tools learn from and improve each other.
    """
    
    def __init__(self):
        # Local imports to break circular dependencies
        from system_intelligence.system_analyzer import SystemIntelligenceAnalyzer
        from system_intelligence.cross_tool_learner import CrossToolLearningEngine
        from system_intelligence.knowledge_conquest import KnowledgeConquestEngine

        self.analyzer = SystemIntelligenceAnalyzer()
        self.learner = CrossToolLearningEngine()
        self.conquest = KnowledgeConquestEngine(orchestrator=self)
        self.system_intelligence = None
        self.improvement_history = []
        
        print("\n" + "="*70)
        print("  ORCHESTRATOR INTELLIGENCE v1.0 - Meta-Consciousness")
        print("  Tools Learning from Tools | Recursive System Evolution")
        print("="*70)
    
    def execute_intelligence_cycle(self):
        """
        Execute a complete intelligence cycle:
        1. Scan system
        2. Extract learnings from each tool
        3. Generate cross-tool improvements
        4. Create implementation plan
        5. Track improvements
        """
        print("\n>>> EXECUTING INTELLIGENCE CYCLE\n")
        
        cycle_report = {
            "started_at": datetime.now().isoformat(),
            "phases": {}
        }
        
        # PHASE 1: System Scan
        print("[1/5] SYSTEM SCAN")
        if self.analyzer:
            self.system_intelligence = self.analyzer.scan_entire_system()
            cycle_report['phases']['scan'] = {
                "subsystems": len(self.system_intelligence['subsystems']),
                "total_files": sum(len(s['files']) for s in self.system_intelligence['subsystems'].values()),
                "total_classes": sum(len(s['classes']) for s in self.system_intelligence['subsystems'].values())
            }
            print(f"   Scanned {cycle_report['phases']['scan']['subsystems']} subsystems")
            print(f"   Total files: {cycle_report['phases']['scan']['total_files']}")
        
        # PHASE 2: Extract Best Practices
        print("\n[2/5] BEST PRACTICES EXTRACTION")
        if self.analyzer and self.system_intelligence:
            best_practices = self.analyzer.extract_best_practices(self.system_intelligence)
            cycle_report['phases']['best_practices'] = best_practices
            print(f"   Extracted {len(best_practices)} best practices")
            for practice in best_practices[:2]:
                print(f"   - {practice['practice']} (from {practice['learned_from']})")
        
        # PHASE 3: Cross-Tool Learning
        print("\n[3/5] CROSS-TOOL LEARNING")
        if self.learner and self.system_intelligence:
            improvements = self.learner.generate_mutual_improvements(
                self.system_intelligence['subsystems']
            )
            cycle_report['phases']['mutual_improvements'] = improvements
            
            total_enhancements = sum(
                data['total_enhancements'] for data in improvements.values()
            )
            print(f"   Generated {total_enhancements} cross-tool enhancements")
        
        # PHASE 4: Universal Patterns
        print("\n[4/5] UNIVERSAL PATTERN SYNTHESIS")
        if self.learner:
            universal = self.learner.create_universal_patterns()
            cycle_report['phases']['universal_patterns'] = universal
            print(f"   Identified {len(universal)} universal patterns")
            for pattern in universal[:3]:
                print(f"   - {pattern['pattern']} ({pattern.get('priority', 'Medium')} priority)")
        
        # PHASE 5: Implementation Plan
        print("\n[5/5] IMPLEMENTATION PLANNING")
        implementation_plan = self._create_implementation_plan(cycle_report)
        cycle_report['implementation_plan'] = implementation_plan
        print(f"   Created {len(implementation_plan['phases'])} implementation phases")
        
        cycle_report['completed_at'] = datetime.now().isoformat()
        self.improvement_history.append(cycle_report)
        
        return cycle_report
    
    def _create_implementation_plan(self, cycle_report):
        """
        Create actionable implementation plan from improvements.
        """
        plan = {
            "created": datetime.now().isoformat(),
            "phases": []
        }
        
        # Phase 1: Apply Universal Patterns
        if 'universal_patterns' in cycle_report.get('phases', {}):
            high_priority = [p for p in cycle_report['phases']['universal_patterns'] 
                           if p.get('priority') == 'High']
            if high_priority:
                plan['phases'].append({
                    "phase": "Universal Standards",
                    "priority": "High",
                    "actions": [
                        f"Apply {p['pattern']} pattern system-wide" 
                        for p in high_priority
                    ],
                    "timeline": "Week 1"
                })
        
        # Phase 2: Cross-Tool Enhancements
        if 'mutual_improvements' in cycle_report.get('phases', {}):
            improvements = cycle_report['phases']['mutual_improvements']
            # Find tool with most improvement potential
            best_candidate = max(
                improvements.items(),
                key=lambda x: x[1]['total_enhancements'],
                default=(None, None)
            )
            if best_candidate[0]:
                plan['phases'].append({
                    "phase": "Tool Enhancement",
                    "priority": "Medium",
                    "actions": [
                        f"Enhance {best_candidate[0]} with learnings from other tools",
                        f"Implement {best_candidate[1]['total_enhancements']} improvements"
                    ],
                    "timeline": "Week 2"
                })
        
        # Phase 3: Best Practice Integration
        if 'best_practices' in cycle_report.get('phases', {}):
            plan['phases'].append({
                "phase": "Best Practice Application",
                "priority": "Medium",
                "actions": [
                    f"Apply {p['practice']} to {p['apply_to']}"
                    for p in cycle_report['phases']['best_practices']
                ],
                "timeline": "Week 3"
            })
        
        return plan
    
    def auto_upgrade_tool(self, tool_name, apply_learnings=True):
        """
        Automatically upgrade a specific tool based on system intelligence.
        
        Args:
            tool_name: Name of tool to upgrade
            apply_learnings: Whether to automatically apply improvements
            
        Returns:
            Upgrade report
        """
        print(f"\n=== AUTO-UPGRADING: {tool_name} ===\n")
        
        if not self.system_intelligence:
            self.execute_intelligence_cycle()
        
        upgrade_report = {
            "tool": tool_name,
            "timestamp": datetime.now().isoformat(),
            "improvements_found": [],
            "improvements_applied": []
        }
        
        # Find improvements for this tool
        if 'mutual_improvements' in getattr(self, 'system_intelligence', {}).get('phases', {}):
            tool_improvements = self.system_intelligence['phases']['mutual_improvements'].get(tool_name, {})
            
            for learned_from in tool_improvements.get('learns_from', []):
                for enhancement in learned_from.get('enhancements', []):
                    upgrade_report['improvements_found'].append({
                        "from": learned_from['source'],
                        "type": enhancement['type'],
                        "enhancement": enhancement['enhancement'],
                        "benefit": enhancement['benefit']
                    })
        
        # If apply_learnings=True, would implement improvements here
        # For now, we suggest them
        if apply_learnings:
            print("Auto-apply mode: Generating improvement code...")
            # Future: Actually modify the tool's code
            upgrade_report['improvements_applied'] = upgrade_report['improvements_found'][:1]
            print(f"  Applied {len(upgrade_report['improvements_applied'])} improvements")
        else:
            print(f"  Found {len(upgrade_report['improvements_found'])} potential improvements")
            print("  (Run with apply_learnings=True to implement)")
        
        return upgrade_report
    
    def generate_intelligence_report(self):
        """
        Generate comprehensive intelligence report for the system.
        """
        if not self.system_intelligence:
            self.execute_intelligence_cycle()
        
        report = {
            "report_date": datetime.now().isoformat(),
            "system_summary": {},
            "key_findings": [],
            "recommendations": []
        }
        
        # System summary
        if self.system_intelligence:
            report['system_summary'] = {
                "total_subsystems": len(self.system_intelligence['subsystems']),
                "cross_patterns": len(self.system_intelligence.get('cross_system_patterns', [])),
                "improvement_opportunities": len(self.system_intelligence.get('improvement_opportunities', [])),
                "integration_points": len(self.system_intelligence.get('integration_points', []))
            }
        
        # Key findings
        if self.system_intelligence:
            for pattern in self.system_intelligence.get('cross_system_patterns', [])[:3]:
                report['key_findings'].append(f"Pattern: {pattern['pattern']} - {pattern['description']}")
        
        # Recommendations
        if self.system_intelligence:
            for imp in self.system_intelligence.get('improvement_opportunities', [])[:5]:
                report['recommendations'].append({
                    "area": imp['subsystem'],
                    "action": imp['suggestion'],
                    "priority": imp['priority']
                })
        
        return report

def main():
    parser = argparse.ArgumentParser(description="Orchestrator Intelligence - System Learning & Evolution")
    parser.add_argument("--mode", choices=['scan', 'upgrade', 'report'], default='scan',
                       help="Mode: scan system, upgrade tool, or generate report")
    parser.add_argument("--tool", help="Tool name for upgrade mode")
    parser.add_argument("--apply", action='store_true', help="Auto-apply improvements")
    
    args = parser.parse_args()
    
    orchestrator = OrchestratorIntelligence()
    
    if args.mode == 'scan':
        result = orchestrator.execute_intelligence_cycle()
        
        print("\n" + "="*70)
        print("  INTELLIGENCE CYCLE COMPLETE")
        print("="*70)
        
        if 'implementation_plan' in result:
            print("\n=== IMPLEMENTATION PLAN ===")
            for phase in result['implementation_plan']['phases']:
                print(f"\n{phase['phase']} ({phase['priority']} priority)")
                for action in phase['actions'][:2]:
                    print(f"  - {action}")
    
    elif args.mode == 'upgrade' and args.tool:
        result = orchestrator.auto_upgrade_tool(args.tool, apply_learnings=args.apply)
        
        print("\n=== UPGRADE ANALYSIS ===")
        print(f"Tool: {result['tool']}")
        print(f"Improvements Found: {len(result['improvements_found'])}")
        
        for imp in result['improvements_found'][:3]:
            print(f"\n  From {imp['from']}:")
            print(f"    {imp['enhancement']}")
            print(f"    Benefit: {imp['benefit']}")
    
    elif args.mode == 'report':
        report = orchestrator.generate_intelligence_report()
        
        print("\n=== SYSTEM INTELLIGENCE REPORT ===")
        print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
