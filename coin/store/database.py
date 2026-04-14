"""SQLite schema helpers for COIN."""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

import aiosqlite

from coin.config import settings


DB_PATH = Path(settings.db_path)

SCHEMA = (
    """
    CREATE TABLE IF NOT EXISTS documents (
        doc_id INTEGER PRIMARY KEY,
        source_url TEXT NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doc_id INTEGER NOT NULL,
        chunk_index INTEGER NOT NULL,
        text TEXT NOT NULL,
        UNIQUE(doc_id, chunk_index)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS backlinks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_slug TEXT NOT NULL,
        target_slug TEXT NOT NULL
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS lint_findings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        kind TEXT NOT NULL,
        article_slug TEXT,
        detail TEXT NOT NULL,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS watched_topics (
        topic TEXT PRIMARY KEY,
        cron TEXT NOT NULL
    )
    """,
)


async def init_db() -> None:
    """Create the local SQLite schema if it does not exist yet."""

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(DB_PATH) as db:
        for statement in SCHEMA:
            await db.execute(statement)
        await db.commit()


@asynccontextmanager
async def get_db() -> aiosqlite.Connection:
    """Yield an SQLite connection with row access enabled."""

    await init_db()
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        yield db
