# C:\Master db\R&D workspace\NEW\failure_memory.py
import os
import sys
import json
import sqlite3
import time

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class FailureMemoryEngine:
    """
    CQ Mythos v6.0 Failure Memory Engine.
    Stores and retrieves historical cognitive failure topologies (rollbacks, entropy load)
    to enable proactive similarity-based preventive stabilization.
    """
    def __init__(self, db_path="failure_memory.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Initializes the sqlite failure memory schema safely."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS failure_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL,
                module TEXT,
                failure_type TEXT,
                entropy_state REAL,
                uncertainty_state REAL,
                recovery_action TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log_failure(self, module, failure_type, entropy, uncertainty, action):
        """Records a new failure event into the database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO failure_records (timestamp, module, failure_type, entropy_state, uncertainty_state, recovery_action)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (time.time(), module, failure_type, entropy, uncertainty, action))
        conn.commit()
        conn.close()
        print(f"  💾 [Failure Memory] Logged historical failure topology: '{failure_type}' in '{module}'")

    def retrieve_similar_failures(self, target_type):
        """Retrieves past similar failure events to prevent recurrent cognitive loops."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT module, entropy_state, recovery_action FROM failure_records
            WHERE failure_type = ? ORDER BY timestamp DESC LIMIT 3
        ''', (target_type,))
        results = cursor.fetchall()
        conn.close()
        
        print(f"\n🔍 [Failure Memory Retrieval] Fetching similar historical profiles for '{target_type}':")
        if not results:
            print("  ✓ No past matching failure topologies found.")
        for idx, row in enumerate(results, 1):
            print(f"  ├─ Past Match {idx}: Module: '{row[0]}' | Active Entropy: {row[1]:.4f} | Recovery Taken: '{row[2]}'")
        return results

if __name__ == "__main__":
    engine = FailureMemoryEngine()
    
    # Logging a series of sample failures
    engine.log_failure("symbolic_solver", "unresolved_constraint", 0.78, 0.4, "temporal_rollback_v4")
    engine.log_failure("parsing_guard", "json_corruption", 0.82, 0.6, "regex_partial_fallback")
    
    # Retrieving matching failure profiles
    engine.retrieve_similar_failures("unresolved_constraint")
