"""Run the full pipeline in agent mode."""

from __future__ import annotations

from coin.pipeline.step2_embed import run as embed_run
from coin.pipeline.step3_group import run_agent as group_run
from coin.pipeline.step4_compile import run_agent as compile_run
from coin.pipeline.step5_link import run as link_run
from coin.pipeline.step6_lint import run_agent as lint_run
from coin.store.database import init_db


async def run_pipeline() -> dict[str, int]:
    """Run the automated steps end-to-end."""

    await init_db()
    embedded_chunks = await embed_run()
    groups = await group_run()
    articles = await compile_run()
    backlinks = await link_run()
    findings = await lint_run()
    return {
        "embedded_chunks": embedded_chunks,
        "groups": len(groups.get("groups", [])),
        "articles": len(articles),
        "backlinks": backlinks,
        "findings": len(findings),
    }
