# C:\Master db\R&D workspace\NEW\reproducibility_ledger.py
import os
import sys
import sqlite3
import time

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class ReproducibilityLedger:
    """
    CQ Mythos Phase Sigma Reproducibility Ledger.
    Maintains persistent SQLite records of every experimental run, seed state,
    ablation config, and system performance metrics.
    """
    def __init__(self, db_path="reproducibility_ledger.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS experiments (
                id TEXT PRIMARY KEY,
                mode TEXT,
                entropy_growth REAL,
                hallucination_rate REAL,
                rollback_freq REAL,
                task_success REAL,
                timestamp INTEGER
            )
        """)
        conn.commit()
        conn.close()

    def record_experiment_run(self, exp_id, mode, entropy, hallucination, rollback, success):
        print(f"\n📖 [Reproducibility Ledger] Writing scientific lineage record for experiment '{exp_id}'...")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO experiments (id, mode, entropy_growth, hallucination_rate, rollback_freq, task_success, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (exp_id, mode, entropy, hallucination, rollback, success, int(time.time())))
        conn.commit()
        
        # Verify write
        cursor.execute("SELECT * FROM experiments WHERE id = ?", (exp_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            print(f"  ✓ Saved State: Mode={row[1]} | Entropy={row[2]:.2f} | Hallucinations={row[3]*100:.1f}% | Success={row[5]*100:.1f}%")
        return row

if __name__ == "__main__":
    ledger = ReproducibilityLedger()
    ledger.record_experiment_run(
        exp_id="exp-001-baseline",
        mode="ENGINEERING",
        entropy=0.12,
        hallucination=0.05,
        rollback=1.2,
        success=0.95
    )
