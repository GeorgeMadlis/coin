"""FastAPI application for the COIN web interface."""

from __future__ import annotations

from fastapi import FastAPI

from coin.web.routes.articles import router as articles_router
from coin.web.routes.graph import router as graph_router
from coin.web.routes.qa import router as qa_router


app = FastAPI(title="COIN")
app.include_router(articles_router, prefix="/api/articles", tags=["articles"])
app.include_router(graph_router, prefix="/api/graph", tags=["graph"])
app.include_router(qa_router, prefix="/api/qa", tags=["qa"])


@app.get("/")
async def root() -> dict[str, str]:
    """Basic service status endpoint."""

    return {"name": "COIN", "status": "ok"}
