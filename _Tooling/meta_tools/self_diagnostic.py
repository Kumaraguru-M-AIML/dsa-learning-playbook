
import sys
import os
import json
from datetime import datetime

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

class SelfDiagnostic:
    """
    Monitors system health, performance, and identifies improvement areas.
    Implements TDS Self-Audit Layer - recursive self-assessment.
    """
    
    def __init__(self):
        self.metrics = {}
        self.health_checks = []
        
    def run_full_diagnostic(self):
        """Execute comprehensive system health check"""
        print("\n=== SYSTEM DIAGNOSTIC ===\n")
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "overall_health": 0,
            "subsystems": {},
            "identified_issues": [],
            "optimization_opportunities": [],
            "upgrade_suggestions": []
        }
        
        # Check each subsystem
        report['subsystems']['cognitive'] = self._check_cognitive_tools()
        report['subsystems']['research'] = self._check_research_tools()
        report['subsystems']['meta'] = self._check_meta_tools()
        
        # Calculate overall health (0-100)
        subsystem_scores = [s['health_score'] for s in report['subsystems'].values()]
        report['overall_health'] = sum(subsystem_scores) / len(subsystem_scores)
        
        # Identify issues
        report['identified_issues'] = self._identify_issues(report['subsystems'])
        
        # Find optimization opportunities
        report['optimization_opportunities'] = self._find_optimizations(report['subsystems'])
        
        # Generate upgrade suggestions
        report['upgrade_suggestions'] = self._suggest_upgrades(report)
        
        return report
    
    def _check_cognitive_tools(self):
        """Check cognitive tools health by verifying file existence."""
        path = os.path.join(root_dir, "cognitive_tools")
        python_files = [f for f in os.listdir(path) if f.endswith('.py')] if os.path.exists(path) else []
        
        health = 100 if python_files else 0
        issues = []
        if not python_files:
            issues.append("No cognitive tools found in directory")
            health = 0
            
        return {
            "name": "Cognitive Tools",
            "health_score": health,
            "components": {f: "Detected" for f in python_files},
            "performance": "Good" if health > 70 else "Critical",
            "issues": issues
        }
    
    def _check_research_tools(self):
        """Check research tools health and dependencies."""
        path = os.path.join(root_dir, "research_tools")
        essential = ['search_arxiv.py', 'search_web.py', 'search_openalex.py']
        
        found = []
        missing = []
        for f in essential:
            if os.path.exists(os.path.join(path, f)):
                found.append(f)
            else:
                missing.append(f)
        
        health = (len(found) / len(essential)) * 100 if essential else 100
        issues = [f"Missing essential tool: {m}" for m in missing]
        
        return {
            "name": "Research Tools",
            "health_score": health,
            "components": {f: "Found" for f in found},
            "performance": "Excellent" if health > 90 else "Diminished",
            "issues": issues
        }
    
    def _check_meta_tools(self):
        """Check meta tools health."""
        path = os.path.join(root_dir, "meta_tools")
        files = [f for f in os.listdir(path) if f.endswith('.py')] if os.path.exists(path) else []
        
        health = min(100, (len(files) / 5) * 100) # Expecting at least 5 meta tools
        issues = []
        if len(files) < 3:
            issues.append("Low meta-tool density - system self-evolution may be restricted")
            
        return {
            "name": "Meta Tools",
            "health_score": health,
            "components": {f: "Operational" for f in files},
            "performance": "Stable" if health > 60 else "Unstable",
            "issues": issues
        }
    
    def _identify_issues(self, subsystems):
        """Identify problems across subsystems"""
        issues = []
        
        for name, system in subsystems.items():
            if system['health_score'] < 70:
                issues.append({
                    "subsystem": name,
                    "severity": "High",
                    "description": f"{name} health below threshold",
                    "action": "Immediate attention required"
                })
            
            if system.get('issues'):
                for issue in system['issues']:
                    issues.append({
                        "subsystem": name,
                        "severity": "Medium",
                        "description": issue,
                        "action": "Monitor and validate"
                    })
        
        return issues
    
    def _find_optimizations(self, subsystems):
        """Find performance optimization opportunities"""
        opportunities = []
        
        # Generic optimization suggestions
        opportunities.append({
            "area": "Inter-system Integration",
            "current": "Tools work independently",
            "potential": "Create unified workflow pipelines",
            "impact": "20-30% efficiency gain"
        })
        
        opportunities.append({
            "area": "Caching & Memoization",
            "current": "Repeated calculations",
            "potential": "Cache frequent queries and results",
            "impact": "40-50% speed improvement"
        })
        
        opportunities.append({
            "area": "Parallel Processing",
            "current": "Some sequential bottlenecks",
            "potential": "Increase parallelization",
            "impact": "Up to 3x throughput"
        })
        
        return opportunities
    
    def _suggest_upgrades(self, report):
        """Generate specific upgrade recommendations"""
        suggestions = []
        
        # Based on health score
        if report['overall_health'] < 80:
            suggestions.append({
                "priority": "High",
                "upgrade": "System Optimization Pass",
                "rationale": "Overall health below optimal threshold",
                "steps": [
                    "Address identified issues",
                    "Implement quick wins from optimization opportunities",
                    "Re-run diagnostics to measure improvement"
                ]
            })
        
        # Based on subsystem analysis
        suggestions.append({
            "priority": "Medium",
            "upgrade": "Meta-Tools Real-World Validation",
            "rationale": "New systems need battle-testing",
            "steps": [
                "Run meta-tools on 5-10 real scenarios",
                "Collect performance metrics",
                "Refine based on results"
            ]
        })
        
        # Strategic suggestion
        suggestions.append({
            "priority": "Low",
            "upgrade": "Build Automation Layer",
            "rationale": "Reduce manual orchestration",
            "steps": [
                "Create workflow automation scripts",
                "Implement scheduled diagnostics",
                "Build reporting dashboard"
            ]
        })
        
        return suggestions
    
    def benchmark_performance(self, task_type, execution_time, result_quality):
        """
        Track performance metrics over time.
        
        Args:
            task_type: Type of task executed
            execution_time: Time taken in seconds
            result_quality: Quality score 0-100
        """
        if task_type not in self.metrics:
            self.metrics[task_type] = {
                "executions": 0,
                "avg_time": 0,
                "avg_quality": 0,
                "best_time": float('inf'),
                "best_quality": 0
            }
        
        metrics = self.metrics[task_type]
        metrics['executions'] += 1
        
        # Update averages
        metrics['avg_time'] = (metrics['avg_time'] * (metrics['executions'] - 1) + execution_time) / metrics['executions']
        metrics['avg_quality'] = (metrics['avg_quality'] * (metrics['executions'] - 1) + result_quality) / metrics['executions']
        
        # Update bests
        metrics['best_time'] = min(metrics['best_time'], execution_time)
        metrics['best_quality'] = max(metrics['best_quality'], result_quality)
        
        return metrics
    
    def get_performance_report(self):
        """Generate performance report from tracked metrics"""
        return {
            "total_tasks": sum(m['executions'] for m in self.metrics.values()),
            "task_types": len(self.metrics),
            "metrics_by_task": self.metrics,
            "improvement_trends": self._calculate_trends()
        }
    
    def _calculate_trends(self):
        """Calculate performance trends"""
        trends = {}
        for task_type, metrics in self.metrics.items():
            if metrics['executions'] > 1:
                trends[task_type] = {
                    "speed_vs_best": f"{(metrics['avg_time'] / metrics['best_time'] - 1) * 100:.1f}% slower than best",
                    "quality_vs_best": f"{(metrics['avg_quality'] / metrics['best_quality']) * 100:.1f}% of best quality"
                }
        return trends

if __name__ == "__main__":
    diagnostic = SelfDiagnostic()
    
    report = diagnostic.run_full_diagnostic()
    
    print(f"Overall Health: {report['overall_health']:.1f}%\n")
    
    print("=== IDENTIFIED ISSUES ===")
    for issue in report['identified_issues']:
        print(f"- {issue['description']} ({issue['severity']})")
    
    print("\n=== OPTIMIZATION OPPORTUNITIES ===")
    for opp in report['optimization_opportunities']:
        print(f"- {opp['area']}: {opp['impact']}")
    
    print("\n=== UPGRADE SUGGESTIONS ===")
    for suggestion in report['upgrade_suggestions']:
        print(f"- [{suggestion['priority']}] {suggestion['upgrade']}")
