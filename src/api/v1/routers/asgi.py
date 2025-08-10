# src/api.py

"""
Application entrypoint (source-folder style).

- Creates the FastAPI app.
- Wires versioned routers under `/api/v1`.
- Provides `/health` for liveness.
- Silences `/favicon.ico` during development.

Run with:
    uvicorn api.v1.routers.asgi:app --app-dir src --reload
"""

from typing import Dict

from fastapi import FastAPI
from fastapi.responses import Response

# Absolute imports from inside the source folder.
# Because src/ is NOT a package, we import from `api...` and pass --app-dir src to uvicorn.
from api.v1.routers import categories, jobs, training # pyright: ignore[reportUnknownVariableType, reportMissingImports]

def create_app() -> FastAPI:
    app = FastAPI(
        title="POS Orchestrator API",
        description="Run orchestrated POS jobs and stream progress via SSE.",
        version="1.0.0",
    )

    @app.get("/health", include_in_schema=False)
    def health() -> Dict[str, str]:
        """Simple liveness probe; returns 200 when the service is up."""
        return {"status": "ok"}

    @app.get("/favicon.ico", include_in_schema=False)
    def favicon() -> Response:
        """
        Silence automatic browser favicon requests during early development.

        Replace with a real static file (or StaticFiles mount) when UI hosting is added.
        """
        return Response(status_code=204)

    # Wire v1 routers
    PREFIX = "/api/v1"
    app.include_router(categories.router, prefix=PREFIX, tags=["categories"])
    app.include_router(jobs.router,        prefix=PREFIX, tags=["jobs"])
    app.include_router(training.router,    prefix=PREFIX, tags=["training"])

    return app

app = create_app()