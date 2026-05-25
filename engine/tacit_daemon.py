# C:\Master db\R&D workspace\NEW\engine\tacit_daemon.py
import os
import datetime

class TacitTranslationDaemon:
    """
    CQ Mythos v6.0 - Tacit Translation Daemon (B.L.U.E. System)
    Extracts successful workflows or tacit chat interactions and compiles them 
    into explicit B.L.U.E. Triad Skill files, perpetually expanding the exocortex.
    """
    def __init__(self, workspace_root="C:\\Master  db\\R&D workspace\\NEW"):
        self.skills_dir = os.path.join(workspace_root, "skills")
        os.makedirs(self.skills_dir, exist_ok=True)

    def extract_and_compile(self, skill_name, opportunity_framing, action_protocol):
        """
        Compiles raw interaction data into a rigid B.L.U.E. Triad Markdown file.
        """
        filename = skill_name.lower().replace(" ", "_").replace("-", "_") + ".md"
        filepath = os.path.join(self.skills_dir, filename)

        triad_template = f"""# SKILL: {skill_name.title()}
**Format:** B.L.U.E. System Triad Architecture v1.0
**Compiled via:** Tacit-Translation Daemon
**Date:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}

---

## 🔺 1. THE OPPORTUNITY FRAMING (Why this matters)
**Capability Unlocked:** {opportunity_framing.get('unlocked', 'Define what this skill allows the agent to do.')}
**Failure Cost:** {opportunity_framing.get('cost', 'Define the cost of failing to use this skill.')}

## 🔺 2. THE ACTION-BASED TASK (Execution Protocol)
{action_protocol}

## 🔺 3. THE FAILURE ARCHIVE (Immutable Ledger)
*System Directive: Do not repeat historical errors. Check this ledger before executing the action.*

| Timestamp | Failure Mode | Mitigation Graft |
| :--- | :--- | :--- |
| *[PENDING]* | *[AWAITING FIRST PHYSICAL FAILURE]* | *[N/A]* |
"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(triad_template)
            
        print(f"\n🧠 [Tacit-Translation] Neural Pathway Grafted.")
        print(f"  ├─ Skill: {skill_name.title()}")
        print(f"  └─ Destination: {filepath}")
        return filepath

if __name__ == "__main__":
    daemon = TacitTranslationDaemon()
    
    print("[Testing Tacit-Translation Daemon...]")
    daemon.extract_and_compile(
        skill_name="Auto-Heal Workflow",
        opportunity_framing={
            "unlocked": "Allows the agent to read stderr from a failed script and automatically execute a patch.",
            "cost": "Waiting for human intervention wastes momentum and fractures flow state."
        },
        action_protocol="1. Detect non-zero exit code.\n2. Pipe stderr to LLM context.\n3. Generate patch.\n4. Apply via `multi_replace_file_content`.\n5. Re-run."
    )
