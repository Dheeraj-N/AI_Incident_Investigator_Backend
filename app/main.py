from fastapi import FastAPI
from fastapi import Request

from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import investigate
from app.api.routes import incidents
from app.api.routes import timeline

from app.core.exceptions import (
    IncidentNotFoundError,
    CoralQueryFailedError,
    TimelineBuildFailedError,
    GeminiRateLimitError,
)

tags_metadata = [
    {
        "name": "Investigations",
        "description":
            "Run incident investigations"
    },
    {
        "name": "Incidents",
        "description":
            "Browse incident records"
    },
    {
        "name": "Timeline",
        "description":
            "Retrieve incident timelines"
    }
]

app = FastAPI(
    title="AI Incident War Room Investigator",

    description="""
AI-powered incident investigation platform.

Features:

- Evidence Collection
- Root Cause Analysis
- Timeline Generation
- Recommendations Engine
- AI Investigation Summary
""",

    version="1.0.0",

    openapi_tags=tags_metadata,

)


app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:5173"],
      allow_methods=["*"],
      allow_headers=["*"],
  )


# -------------------------
# Routers
# -------------------------

app.include_router(
    investigate.router, prefix="/api"
)

app.include_router(
    incidents.router, prefix="/api"
)

app.include_router(
    timeline.router, prefix="/api"
)

# -------------------------
# Exception Handlers
# -------------------------


@app.exception_handler(
    IncidentNotFoundError
)
async def incident_not_found_handler(
    request: Request,
    exc: IncidentNotFoundError
):

    return JSONResponse(
        status_code=404,
        content={
            "error":
                "incident_not_found",

            "message":
                exc.message
        }
    )


@app.exception_handler(
    CoralQueryFailedError
)
async def coral_query_failed_handler(
    request: Request,
    exc: CoralQueryFailedError
):

    return JSONResponse(
        status_code=503,
        content={
            "error":
                "coral_query_failed",

            "message":
                exc.message
        }
    )


@app.exception_handler(
    TimelineBuildFailedError
)
async def timeline_build_failed_handler(
    request: Request,
    exc: TimelineBuildFailedError
):

    return JSONResponse(
        status_code=500,
        content={
            "error":
                "timeline_build_failed",

            "message":
                exc.message
        }
    )


@app.exception_handler(
    GeminiRateLimitError
)
async def gemini_rate_limit_handler(
    request: Request,
    exc: GeminiRateLimitError
):

    return JSONResponse(
        status_code=429,
        content={
            "error":
                "rate_limit_exceeded",

            "message":
                exc.message
        }
    )




"""from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.core.exceptions import IncidentNotFoundError

from app.api.routes import investigate
from app.api.routes import incidents
from app.api.routes import timeline


app = FastAPI(title="AI Incident War Room Investigator")


@app.exception_handler(IncidentNotFoundError)
async def incident_not_found_handler(request: Request, exc: IncidentNotFoundError):

    logger.error(str(exc))

    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(Exception)
async def generic_handler(request: Request, exc: Exception):

    logger.exception("Unhandled exception")

    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})


app.include_router(investigate.router)

app.include_router(incidents.router)

app.include_router(timeline.router)
"""