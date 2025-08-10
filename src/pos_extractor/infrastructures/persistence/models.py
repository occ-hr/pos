# src/pos_extractor/infrastructures/persistence/models.py

from datetime import datetime
from enum import Enum
from typing import Optional
from sqlalchemy import String, DateTime, JSON, Integer, ForeignKey, Text, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class JobStatus(str, Enum):
    SUBMITTED = "SUBMITTED"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"

class Job(Base):
    __tablename__ = "jobs"
    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(200), default="", nullable=False)
    status: Mapped[JobStatus] = mapped_column(SAEnum(JobStatus), default=JobStatus.SUBMITTED, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    params_json: Mapped[dict] = mapped_column(JSON, default=dict)
    steps: Mapped[list["JobStep"]] = relationship(back_populates="job", cascade="all, delete-orphan")
    artifacts: Mapped[list["Artifact"]] = relationship(back_populates="job", cascade="all, delete-orphan")

class JobStep(Base):
    __tablename__ = "job_steps"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"))
    component: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(20), default="PENDING", nullable=False)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    metrics_json: Mapped[dict] = mapped_column(JSON, default=dict)
    error_json: Mapped[dict] = mapped_column(JSON, default=dict)
    job: Mapped["Job"] = relationship(back_populates="steps")

class Artifact(Base):
    __tablename__ = "artifacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    job_id: Mapped[str] = mapped_column(String(36), ForeignKey("jobs.id", ondelete="CASCADE"))
    kind: Mapped[str] = mapped_column(String(50), nullable=False)
    path: Mapped[str] = mapped_column(Text, nullable=False)
    meta_json: Mapped[dict] = mapped_column(JSON, default=dict)
    job: Mapped["Job"] = relationship(back_populates="artifacts")
