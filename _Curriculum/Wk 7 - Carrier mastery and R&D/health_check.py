import os, sys
si_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "system_intelligence")
if not os.path.exists(si_path):
    print("[CRITICAL] system_intelligence folder MISSING!")
    print("  Fix: mklink /J system_intelligence \"E:\\1  Mastery DB\\SYSTEM\\system_intelligence\"")
    sys.exit(1)
files = os.listdir(si_path)
if not files or "sol_agent.py" not in files:
    print("[CRITICAL] system_intelligence junction is BROKEN (empty or missing sol_agent.py)!")
    print("  Fix: Remove junction and re-create with mklink /J")
    sys.exit(1)
print(f"[OK] system_intelligence healthy - {len(files)} files accessible")
