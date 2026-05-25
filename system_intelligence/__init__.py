"""
System Intelligence Package - Sol-Agent

The unified intelligence. One agent. One purpose.
"""

import os
import sys
import io

# Primary import: Sol-Agent (the unified intelligence)
from .sol_agent import SolAgent, init_sol_agent

# Legacy compatibility: Try to import old interfaces if present
try:
    from .autonomous_brain import AutonomousSystemBrain
except ImportError:
    AutonomousSystemBrain = None

try:
    from .jepa_world_model import JEPAWorldModel
except ImportError:
    JEPAWorldModel = None


def init_agent_fast(workspace_path: str = "."):
    """
    Initialize Sol-Agent with all banners suppressed.
    """
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        agent = init_sol_agent(workspace_path)
    finally:
        sys.stdout = old_stdout

    print(f"[SOL-AGENT] v{agent.VERSION} READY | Brain:{'ON' if agent.brain else 'OFF'} | JEPA:{'ON' if agent.jepa else 'OFF'}")
    return agent


__all__ = [
    'SolAgent', 'init_sol_agent', 'init_agent_fast',
    'JEPAWorldModel',
]
__version__ = '2.0.0'
