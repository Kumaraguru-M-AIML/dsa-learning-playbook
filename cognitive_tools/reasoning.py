
class ThoughtStep:
    def __init__(self, step_type, content, confidence=1.0):
        self.step_type = step_type # "Observation", "Hypothesis", "Action", "Conclusion"
        self.content = content
        self.confidence = confidence

    def __repr__(self):
        return f"[{self.step_type.upper()}] {self.content} (Conf: {self.confidence})"

class ReasoningEngine:
    def __init__(self):
        self.trace = []

    def observe(self, observation):
        self.trace.append(ThoughtStep("Observation", observation))
        print(f"[*] OBSERVE: {observation}")

    def hypothesize(self, hypothesis, confidence=0.5):
        self.trace.append(ThoughtStep("Hypothesis", hypothesis, confidence))
        print(f"[?] HYPOTHESIS: {hypothesis} ({confidence*100}%)")

    def deduce_action(self, logic):
        self.trace.append(ThoughtStep("Action", logic))
        print(f"[!] ACTION: {logic}")

    def conclude(self, conclusion):
        self.trace.append(ThoughtStep("Conclusion", conclusion))
        print(f"[=] CONCLUSION: {conclusion}")

    def generate_summary(self):
        summary = "\n--- [COGNITIVE TRACE] ---\n"
        for t in self.trace:
            summary += f"- {t}\n"
        return summary

if __name__ == "__main__":
    # Test: Debugging a crash
    brain = ReasoningEngine()
    
    brain.observe("The script Main.py crashed with Exit Code 1.")
    brain.observe("No error output was printed to stdout.")
    
    brain.hypothesize("Maybe the error happened before the logging system initialized.", 0.7)
    brain.hypothesize("Maybe it's a silent syntax error.", 0.3)
    
    brain.deduce_action("I should run with 'python -u' to unbuffer output.")
    brain.deduce_action("I should inspect imports for circular dependencies.")
    
    brain.conclude("The next logical step is to disable buffering to catch the early crash signature.")
    
    print(brain.generate_summary())
