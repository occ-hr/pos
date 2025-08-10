from dataclasses import dataclass
from typing import Dict, Protocol, Any

from .entities.job_spec import JobSpec, Component

class Runner(Protocol):
    def run(self, params: Dict[str, Any]) -> None: ...

@dataclass
class Orchestrator:
    components: Dict[Component, Runner]

    def execute(self, job: JobSpec) -> None:
        for step in job.steps:
            runner = self.components.get(step)
            if runner is None:
                raise KeyError(f"No runner registered for step: {step}")
            print(f"[orchestrator] -> {step.name}")
            runner.run(job.params)
            print(f"[orchestrator] <- {step.name} done\n")
