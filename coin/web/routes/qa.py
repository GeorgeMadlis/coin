"""Streaming Q&A route."""

from __future__ import annotations

import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from coin.pipeline.step7_qa import run_agent


router = APIRouter()


class QuestionPayload(BaseModel):
    question: str


@router.post("")
async def ask(payload: QuestionPayload) -> StreamingResponse:
    """Stream a single JSON answer event."""

    answer = await run_agent(payload.question)

    async def event_stream() -> object:
        yield f"data: {json.dumps(answer, ensure_ascii=False)}\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
