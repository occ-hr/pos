# src/api/v1/routers/jobs.py
# router for job submission, streaming, and (maybe) status retrieval.

"""
Jobs API (v1)

Endpoints for submitting and running orchestrated POS jobs. The primary
endpoint streams progress via Server‑Sent Events (SSE), which clients can
consume with the browser `EventSource` API or an SSE library.

Conventions
-----------
- Mounted under `/api/v1` by the application entrypoint.
- Responses use `text/event-stream` for streaming output.
- Caching is disabled to prevent intermediaries from buffering the stream.
"""

from typing import Generator

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse

from ..schemas.job import JobSpecModel
from ..dependencies import get_orchestrator
from pos_extractor.container import Orchestrator

router = APIRouter(tags=["jobs"])

@router.post(
    "/jobs/run",
    summary="Run an orchestrated job (streamed)",
    description=(
        "Accepts a `JobSpec` payload and streams progress logs as "
        "Server‑Sent Events (SSE). Each event is formatted as `data: <line>\\n\\n`."
    ),
    responses={
        200: {"description": "SSE stream started (text/event-stream)"},
        422: {"description": "Invalid job spec (e.g., bad step names)"},
    },
)
def run_job(
    job: JobSpecModel,
    orch: Orchestrator = Depends(get_orchestrator),
) -> StreamingResponse:
    """
    Execute a POS job and stream progress lines as SSE.

    Parameters
    ----------
    job : JobSpecModel
        Incoming request body defining the job name, ordered steps, and params.
        Converted to a domain `JobSpec` via `job.to_domain()`.
    orch : Orchestrator
        Dependency-injected pipeline orchestrator.

    Returns
    -------
    StreamingResponse
        A live `text/event-stream` response. Each yielded chunk is framed as
        `data: <content>\\n\\n` per the SSE spec so that `EventSource` clients
        can consume updates incrementally.

    Raises
    ------
    HTTPException
        422 if the payload cannot be converted to a valid domain `JobSpec`.
    """
    try:
        job_spec = job.to_domain()
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))

    def gen() -> Generator[str, None, None]:
        # Optionally emit a heartbeat to keep idle connections alive:
        # yield ": ping\\n\\n"
        for chunk in orch.stream(job_spec):
            # Ensure proper SSE framing
            yield f"data: {chunk}\n\n"

    # Disable buffering/caching so events flush to the client promptly
    headers = {
        "Cache-Control": "no-cache",
        "X-Accel-Buffering": "no",  # helpful when behind nginx
    }
    return StreamingResponse(gen(), media_type="text/event-stream", headers=headers)
