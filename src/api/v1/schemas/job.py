# src/api/v1/schemas/job.py
# defines JobSpecModel and possibly validators to translate JSON → domain JobSpec.

from pydantic import BaseModel, Field, field_validator
from typing import Any, Dict, List, Optional
from pos_extractor.entities.job_spec import Component, JobSpec

class JobSpecModel(BaseModel):
    name: str = ""
    steps: Optional[List[Component]] = Field(default=None)
    params: Dict[str, Any] = Field(default_factory=dict)

    @field_validator("steps", mode="before")
    @classmethod
    def validate_steps(cls: type["JobSpecModel"], v: Any) -> Optional[List[Component]]:
        if v is None:
            return v
        try:
            return [Component[s] for s in v]
        except KeyError as exc:
            raise ValueError(f"Invalid step: {exc}") from exc

    def to_domain(self) -> JobSpec:
        steps = self.steps if self.steps is not None else [Component.PREPARING, Component.PROCESSING, Component.TRAINING]
        return JobSpec(name=self.name, steps=steps, params=self.params)