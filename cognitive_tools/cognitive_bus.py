# C:\Master db\R&D workspace\NEW\cognitive_bus.py
import os
import sys
import time
import uuid
import json

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

class CognitiveEvent:
    """Represents a unified, standardized event passing through the Cognitive Bus."""
    def __init__(self, source_module, event_type, payload, confidence=1.0, uncertainty=0.0, trace_id=None):
        self.event_id = str(uuid.uuid4())[:8]
        self.trace_id = trace_id or str(uuid.uuid4())[:8]
        self.timestamp = time.time()
        self.source_module = source_module
        self.event_type = event_type
        self.confidence = float(confidence)
        self.uncertainty = float(uncertainty)
        self.payload = payload
        self.rollback_safe = True

class UnifiedCognitiveBus:
    """
    CQ Mythos v6.0 Nervous System / Unified Cognitive Bus.
    Enforces standardized event schemas, supports Trace ID lineage,
    and implements priority interrupts (e.g. ROLLBACK_TRIGGERED overrides Normal).
    """
    def __init__(self):
        self.event_queue = []
        self.event_history = []
        self.priority_levels = {
            "ROLLBACK_TRIGGERED": 10,
            "ENTROPY_ALERT": 8,
            "BELIEF_UPDATE": 5,
            "NORMAL_REASONING": 1
        }

    def publish_event(self, source_module, event_type, payload, confidence=1.0, uncertainty=0.0, trace_id=None):
        """Standardizes and publishes an event to the unified bus."""
        event = CognitiveEvent(source_module, event_type, payload, confidence, uncertainty, trace_id)
        priority = self.priority_levels.get(event_type, 1)
        
        print(f"  ✉️ [Bus Publish] Source: '{source_module:18s}' | Event: '{event_type:18s}' | Priority: {priority:2d} | Trace: '{event.trace_id}'")
        
        # Enforce priority routing: Higher priority events are placed at the front of the queue
        if self.event_queue and priority > self.priority_levels.get(self.event_queue[0].event_type, 1):
            print(f"    🚨 [Priority Interrupt] High priority '{event_type}' interrupts the cognitive queue!")
            self.event_queue.insert(0, event)
        else:
            self.event_queue.append(event)
            
        self.event_history.append(event)
        return event

    def process_next_event(self):
        """Processes the next event in the queue."""
        if not self.event_queue:
            return None
        event = self.event_queue.pop(0)
        print(f"  ⚙️ [Bus Process] Handling Event '{event.event_id}' | Type: '{event.event_type}' | Payload: {json.dumps(event.payload)}")
        return event

if __name__ == "__main__":
    bus = UnifiedCognitiveBus()
    
    # Simulating standard reasoning followed by a sudden high-priority rollback interrupt
    trace = "TR-9042"
    bus.publish_event("neural_inference", "NORMAL_REASONING", {"thought": "Analyzing workspace configuration..."}, trace_id=trace)
    bus.publish_event("workspace_monitor", "BELIEF_UPDATE", {"path": "C:\\Master db"}, trace_id=trace)
    
    print("\n⚡ Sudden contradiction found! Publishing ROLLBACK_TRIGGERED...")
    bus.publish_event("symbolic_solver", "ROLLBACK_TRIGGERED", {"reason": "Contradiction found on node RTX 3050"}, trace_id=trace)
    
    print("\n📦 Processing the cognitive queue:")
    while bus.event_queue:
        bus.process_next_event()
