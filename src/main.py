from typing import Dict, Any

from pos_extractor.container import Orchestrator
from pos_extractor.entities.job_spec import JobSpec, Component
from pos_extractor.preparing.preparer import Preparer
from pos_extractor.processing.processor import Processor
from pos_extractor.training.trainer import Trainer

def build_orchestrator() -> Orchestrator:
    return Orchestrator(components={
        Component.PREPARING: Preparer(),
        Component.PROCESSING: Processor(),
        Component.TRAINING: Trainer(),
    })

def demo() -> Dict[str, Any]:
    job = JobSpec(name="demo")
    orch = build_orchestrator()
    orch.execute(job)
    return job.params

if __name__ == "__main__":
    params = demo()
    print("[main] final params:", params)
