
import os
import ast
import json
from collections import defaultdict
from datetime import datetime

class SystemIntelligenceAnalyzer:
    """
    Scans all system components and extracts patterns, architectures, and improvement opportunities.
    This is the "consciousness" layer that understands the entire system.
    """
    
    def __init__(self, root_dir=None):
        if root_dir is None:
            root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.root_dir = root_dir
        self.system_map = {}
        self.patterns = defaultdict(list)
        self.capabilities = {}
        
    def scan_entire_system(self):
        """
        Perform deep analysis of all system components.
        Returns comprehensive intelligence report.
        """
        print("\n=== SYSTEM INTELLIGENCE SCAN ===\n")
        
        intelligence = {
            "scan_time": datetime.now().isoformat(),
            "subsystems": {},
            "cross_system_patterns": [],
            "improvement_opportunities": [],
            "integration_points": []
        }
        
        # Scan each subsystem
        subsystems = ['cognitive_tools', 'research_tools', 'meta_tools']
        
        for subsystem in subsystems:
            subsystem_path = os.path.join(self.root_dir, subsystem)
            if os.path.exists(subsystem_path):
                analysis = self._analyze_subsystem(subsystem_path, subsystem)
                intelligence['subsystems'][subsystem] = analysis
        
        # Extract cross-system patterns
        intelligence['cross_system_patterns'] = self._find_cross_system_patterns(
            intelligence['subsystems']
        )
        
        # Identify improvement opportunities
        intelligence['improvement_opportunities'] = self._identify_improvements(
            intelligence['subsystems']
        )
        
        # Map integration points
        intelligence['integration_points'] = self._map_integrations(
            intelligence['subsystems']
        )
        
        return intelligence
    
    def _analyze_subsystem(self, path, name):
        """Analyze a single subsystem directory"""
        analysis = {
            "name": name,
            "files": [],
            "classes": [],
            "functions": [],
            "imports": set(),
            "patterns_used": [],
            "complexity_score": 0
        }
        
        # Scan Python files
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    filepath = os.path.join(root, file)
                    file_analysis = self._analyze_python_file(filepath)
                    
                    analysis['files'].append(file)
                    analysis['classes'].extend(file_analysis['classes'])
                    analysis['functions'].extend(file_analysis['functions'])
                    analysis['imports'].update(file_analysis['imports'])
                    analysis['patterns_used'].extend(file_analysis['patterns'])
        
        # Convert set to list for JSON serialization
        analysis['imports'] = list(analysis['imports'])
        
        # Calculate complexity
        analysis['complexity_score'] = self._calculate_complexity(analysis)
        
        return analysis
    
    def _analyze_python_file(self, filepath):
        """Extract structure from a Python file"""
        analysis = {
            "classes": [],
            "functions": [],
            "imports": set(),
            "patterns": []
        }
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    analysis['classes'].append(node.name)
                elif isinstance(node, ast.FunctionDef):
                    analysis['functions'].append(node.name)
                elif isinstance(node, ast.Import):
                    for alias in node.names:
                        analysis['imports'].add(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        analysis['imports'].add(node.module)
            
            # Detect design patterns
            if 'Engine' in str(analysis['classes']):
                analysis['patterns'].append('Engine Pattern')
            if any('optimize' in f for f in analysis['functions']):
                analysis['patterns'].append('Optimization Pattern')
            if any('simulate' in f for f in analysis['functions']):
                analysis['patterns'].append('Simulation Pattern')
                
        except Exception as e:
            print(f"Error analyzing {filepath}: {e}")
        
        return analysis
    
    def _calculate_complexity(self, analysis):
        """Calculate subsystem complexity score"""
        score = 0
        score += len(analysis['files']) * 10
        score += len(analysis['classes']) * 5
        score += len(analysis['functions']) * 2
        score += len(analysis['imports']) * 1
        return score
    
    def _find_cross_system_patterns(self, subsystems):
        """Find patterns that appear across multiple subsystems"""
        patterns = []
        
        # Pattern: Engine architecture
        engine_systems = []
        for name, data in subsystems.items():
            if any('Engine' in pattern for pattern in data['patterns_used']):
                engine_systems.append(name)
        
        if len(engine_systems) > 1:
            patterns.append({
                "pattern": "Engine Architecture",
                "description": "Multiple subsystems use Engine pattern",
                "systems": engine_systems,
                "benefit": "Consistent interface across tools"
            })
        
        # Pattern: Common imports
        common_imports = set()
        for subsystem_data in subsystems.values():
            if common_imports:
                common_imports &= set(subsystem_data['imports'])
            else:
                common_imports = set(subsystem_data['imports'])
        
        if common_imports:
            patterns.append({
                "pattern": "Shared Dependencies",
                "description": f"Common imports: {', '.join(list(common_imports)[:5])}",
                "benefit": "Standardized library usage"
            })
        
        return patterns
    
    def _identify_improvements(self, subsystems):
        """Identify potential improvements"""
        improvements = []
        
        # Check for missing error handling
        for name, data in subsystems.items():
            if not any('try' in str(f) or 'exception' in str(f).lower() 
                      for f in data['functions']):
                improvements.append({
                    "subsystem": name,
                    "type": "Error Handling",
                    "suggestion": "Add comprehensive error handling",
                    "priority": "Medium"
                })
        
        # Check for optimization opportunities
        for name, data in subsystems.items():
            if data['complexity_score'] > 200:
                improvements.append({
                    "subsystem": name,
                    "type": "Complexity Reduction",
                    "suggestion": "Consider refactoring into smaller modules",
                    "priority": "Low"
                })
        
        # Check for missing documentation
        improvements.append({
            "subsystem": "All",
            "type": "Documentation",
            "suggestion": "Ensure all public functions have docstrings",
            "priority": "Medium"
        })
        
        return improvements
    
    def _map_integrations(self, subsystems):
        """Map how subsystems integrate with each other"""
        integrations = []
        
        for name, data in subsystems.items():
            for import_name in data['imports']:
                # Check if import is from another subsystem
                for other_name in subsystems.keys():
                    if other_name in import_name and other_name != name:
                        integrations.append({
                            "from": name,
                            "to": other_name,
                            "type": "Import Dependency"
                        })
        
        return integrations
    
    def extract_best_practices(self, intelligence):
        """Extract best practices from the most successful components"""
        best_practices = []
        
        # Find highest performing subsystem (by complexity and patterns)
        best_subsystem = max(
            intelligence['subsystems'].items(),
            key=lambda x: len(x[1]['patterns_used'])
        )
        
        best_practices.append({
            "practice": "Engine Pattern Usage",
            "learned_from": best_subsystem[0],
            "description": "Use standardized Engine classes for consistency",
            "apply_to": "All new tools"
        })
        
        # Extract from integration points
        if intelligence['integration_points']:
            best_practices.append({
                "practice": "Cross-System Integration",
                "learned_from": "System Architecture",
                "description": "Tools should import and use each other's capabilities",
                "apply_to": "All subsystems"
            })
        
        return best_practices

if __name__ == "__main__":
    analyzer = SystemIntelligenceAnalyzer()
    intelligence = analyzer.scan_entire_system()
    
    print("\n=== SYSTEM INTELLIGENCE REPORT ===\n")
    
    print(f"Subsystems Scanned: {len(intelligence['subsystems'])}")
    for name, data in intelligence['subsystems'].items():
        print(f"\n{name.upper()}:")
        print(f"  Files: {len(data['files'])}")
        print(f"  Classes: {len(data['classes'])}")
        print(f"  Functions: {len(data['functions'])}")
        print(f"  Complexity: {data['complexity_score']}")
    
    print(f"\n\nCross-System Patterns: {len(intelligence['cross_system_patterns'])}")
    for pattern in intelligence['cross_system_patterns']:
        print(f"  - {pattern['pattern']}: {pattern['description']}")
    
    print(f"\n\nImprovement Opportunities: {len(intelligence['improvement_opportunities'])}")
    for imp in intelligence['improvement_opportunities'][:3]:
        print(f"  - [{imp['priority']}] {imp['subsystem']}: {imp['suggestion']}")
    
    # Extract and display best practices
    best_practices = analyzer.extract_best_practices(intelligence)
    print(f"\n\nBest Practices Extracted: {len(best_practices)}")
    for practice in best_practices:
        print(f"  - {practice['practice']} (from {practice['learned_from']})")
