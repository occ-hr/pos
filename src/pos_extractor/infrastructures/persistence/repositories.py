# src/pos_extractor/infrastructures/persistence/repositories.py

import uuid
from contextlib import contextmanager
from datetime import datetime
from typing import Iterator, Optional, Sequence
from sqlalchemy.orm import Session
from sqlalchemy import select
from .db import SessionLocal, engine, Base
from .models import Job, JobStep, Artifact, JobStatus

@contextmanager
def session_scope() -> Iterator[Session]:
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def init_db() -> None:
    Base.metadata.create_all(bind=engine)

def create_job(name: str, params: dict) -> Job:
    job = Job(id=str(uuid.uuid4()), name=name, status=JobStatus.SUBMITTED, params_json=params or {})
    with session_scope() as s:
        s.add(job)
    return job

def get_job(job_id: str) -> Optional[Job]:
    with session_scope() as s:
        return s.get(Job, job_id)

def list_jobs() -> Sequence[Job]:
    with session_scope() as s:
        return list(s.scalars(select(Job).order_by(Job.created_at.desc())).all())

def start_job(job_id: str, steps: list[str]) -> None:
    now = datetime.utcnow()
    with session_scope() as s:
        job = s.get(Job, job_id)
        if not job:
            raise ValueError("job not found")
        job.status = JobStatus.RUNNING
        for comp in steps:
            s.add(JobStep(job_id=job_id, component=comp, status="PENDING"))
        job.updated_at = now

def update_step(job_id: str, component: str, status: str, metrics: dict | None = None, error: dict | None = None) -> None:
    now = datetime.utcnow()
    with session_scope() as s:
        stmt = select(JobStep).where(JobStep.job_id == job_id, JobStep.component == component).order_by(JobStep.id.asc())
        step = s.scalars(stmt).first()
        if not step:
            step = JobStep(job_id=job_id, component=component, status=status, started_at=now if status=="STARTED" else None)
            s.add(step)
        if status == "STARTED":
            step.status = "RUNNING"
            step.started_at = now
        elif status == "DONE":
            step.status = "SUCCEEDED"
            step.finished_at = now
            if metrics:
                step.metrics_json = metrics
        elif status == "ERROR":
            step.status = "FAILED"
            step.finished_at = now
            if error:
                step.error_json = error

def finalize_job(job_id: str, succeeded: bool, artifacts: list[tuple[str, str]] | None = None) -> None:
    now = datetime.utcnow()
    with session_scope() as s:
        job = s.get(Job, job_id)
        if not job:
            return
        job.status = JobStatus.SUCCEEDED if succeeded else JobStatus.FAILED
        job.updated_at = now
        for kind, path in (artifacts or []):
            s.add(Artifact(job_id=job_id, kind=kind, path=path))
