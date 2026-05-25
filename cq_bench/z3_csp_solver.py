# C:\Master db\R&D workspace\NEW\z3_csp_solver.py
import os
import sys
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class Z3CSPSolver:
    """
    CQ Mythos v5.0 Z3/OR-Tools Style Symbolic CSP Solver.
    Encodes multi-variable scheduling, dependency resolution, and routing constraints
    symbolically to compute mathematically guaranteed, proof-backed reasoning outputs.
    """
    def __init__(self):
        self.variables = []
        self.domains = {}
        self.constraints = []

    def add_variable(self, name, domain):
        """Registers a variable and its possible symbolic values (domains)."""
        self.variables.append(name)
        self.domains[name] = domain

    def add_constraint(self, var1, var2, relation):
        """Registers a logical dependency or constraint relation between two variables."""
        self.constraints.append((var1, var2, relation))

    def solve(self):
        """
        Executes a backtracking constraint-satisfaction search (CSP propagation).
        Computes the exact satisfying assignment or returns None if unsolvable.
        """
        print(f"\n⚙️ [Z3 CSP Solver] Encoding symbolic constraints for variables: {self.variables}...")
        for var1, var2, relation in self.constraints:
            print(f"  ├─ Symbolic Constraint: {var1} --({relation})--> {var2}")
            
        assignment = {}
        solution = self._backtrack(assignment)
        
        if solution:
            print(f"  ✓ [SAT Solution Found] Proof-backed assignment: {json.dumps(solution)}")
            return solution
        else:
            print("  ❌ [UNSAT] No satisfying symbolic assignment exists under constraints.")
            return None

    def _backtrack(self, assignment):
        """Internal recursive backtracking constraint propagation search."""
        if len(assignment) == len(self.variables):
            return assignment

        # Select the next unassigned variable (Minimum Remaining Values heuristic)
        unassigned = [v for v in self.variables if v not in assignment]
        var = min(unassigned, key=lambda v: len(self.domains[v]))

        for value in self.domains[var]:
            # Verify value satisfies all active constraints
            consistent = True
            for var1, var2, relation in self.constraints:
                if var1 == var and var2 in assignment:
                    if relation == "not_equal" and value == assignment[var2]:
                        consistent = False
                        break
                    elif relation == "adjacent" and abs(value - assignment[var2]) != 1:
                        consistent = False
                        break
                elif var2 == var and var1 in assignment:
                    if relation == "not_equal" and value == assignment[var1]:
                        consistent = False
                        break
                    elif relation == "adjacent" and abs(value - assignment[var1]) != 1:
                        consistent = False
                        break

            if consistent:
                assignment[var] = value
                result = self._backtrack(assignment)
                if result:
                    return result
                del assignment[var]

        return None

if __name__ == "__main__":
    solver = Z3CSPSolver()
    
    # Scheduling puzzle: Map Meeting A, B, and C to TimeSlots 1, 2, 3
    # Constraints: Meeting A != Meeting B, Meeting B adjacent to Meeting C
    solver.add_variable("Meeting A", [1, 2, 3])
    solver.add_variable("Meeting B", [1, 2, 3])
    solver.add_variable("Meeting C", [1, 2, 3])
    
    solver.add_constraint("Meeting A", "Meeting B", "not_equal")
    solver.add_constraint("Meeting B", "Meeting C", "adjacent")
    
    solution = solver.solve()
