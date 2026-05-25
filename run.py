import sys
import os
import subprocess

def setup_environment():
    """Injects the custom hierarchical workspace into Python path natively."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sub_dirs = ["engine", "cognitive_tools", "memory", "cq_bench"]
    
    for folder in sub_dirs:
        full_path = os.path.join(base_dir, folder)
        if full_path not in sys.path:
            sys.path.insert(0, full_path)
    
    print(f"[*] Apex Environment Verified. Path vectors set to {len(sub_dirs)} local packages.\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python run.py [module_name] [arguments...]")
        print("Examples:")
        print("  python run.py cq_mythos_v2")
        print("  python run.py ablation_engine")
        sys.exit(1)
    
    target = sys.argv[1]
    args = sys.argv[2:]
    
    # Attempt automatic resolution across the smart architecture
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sub_dirs = ["engine", "cognitive_tools", "memory", "cq_bench"]
    
    found_path = None
    for folder in sub_dirs:
        test_path = os.path.join(base_dir, folder, f"{target}.py")
        if os.path.exists(test_path):
            found_path = test_path
            break
            
    if found_path:
        print(f"[+] Found module at: {found_path}")
        print(f"[+] Launching executing pipeline...\n")
        # Execute while preserving the adjusted PYTHONPATH
        env = os.environ.copy()
        paths_to_add = [os.path.join(base_dir, f) for f in sub_dirs]
        env["PYTHONPATH"] = os.pathsep.join(paths_to_add) + os.pathsep + env.get("PYTHONPATH", "")
        
        subprocess.run([sys.executable, found_path] + args, env=env)
    else:
        print(f"[!] Error: Module '{target}' not found in standard architectural directories.")

if __name__ == "__main__":
    setup_environment()
    main()
