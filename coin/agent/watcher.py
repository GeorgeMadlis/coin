"""Watch-mode daemon utilities."""

from __future__ import annotations

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from coin.pipeline.step4_compile import run_agent as compile_run
from coin.store.database import get_db


class Watcher:
    """Minimal watch-mode scheduler wrapper."""

    def __init__(self) -> None:
        self.scheduler = AsyncIOScheduler()

    async def run_all(self) -> int:
        """Compile all watched topics immediately."""

        async with get_db() as db:
            rows = await db.execute_fetchall("SELECT topic FROM watched_topics ORDER BY topic")

        topics = [str(row["topic"]) for row in rows]
        for topic in topics:
            await compile_run(topic)
        return len(topics)

    async def start(self) -> None:
        """Register the current watched topics with APScheduler."""

        async with get_db() as db:
            rows = await db.execute_fetchall("SELECT topic, cron FROM watched_topics ORDER BY topic")

        for row in rows:
            topic = str(row["topic"])
            cron = str(row["cron"])
            minute, hour, day, month, day_of_week = cron.split()
            self.scheduler.add_job(
                compile_run,
                "cron",
                args=[topic],
                minute=minute,
                hour=hour,
                day=day,
                month=month,
                day_of_week=day_of_week,
                id=topic,
                replace_existing=True,
            )

        self.scheduler.start()
