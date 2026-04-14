"""
coin/cli.py — COIN CLI

Every command that involves an LLM call supports --manual flag.
In manual mode the command prints the prompt to paste into Claude.ai
or ChatGPT, then optionally waits for you to paste the response back.
"""

from __future__ import annotations

import asyncio
import json
import sys
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

app = typer.Typer(help="COIN — ConnectedInformation knowledge base", rich_markup_mode="markdown")
console = Console()


def _mode_note(manual: bool) -> None:
    if manual:
        console.print(Panel(
            "[bold]Manual mode[/bold] — copy the prompt below into Claude.ai or ChatGPT.\n"
            "Paste the LLM response back using the [cyan]--apply[/cyan] flag.",
            style="cyan", expand=False
        ))


# ── coin ingest ────────────────────────────────────────────────────────────────

@app.command()
def ingest(
    source: str = typer.Argument(help="URL, file path, --tweet, or --audio"),
    tweet: bool = typer.Option(False),
    audio: bool = typer.Option(False),
    manual: bool = typer.Option(False, help="Print manual-mode prompt instead of running"),
) -> None:
    """Step 1 — Ingest a source into the knowledge base."""
    if manual:
        _mode_note(manual=True)
        prompt_path = Path(__file__).parent / "prompts" / "01_ingest.md"
        console.print(Markdown(prompt_path.read_text()))
        console.print(
            "\n[dim]Paste the raw source content where indicated, run through Claude.ai or ChatGPT,\n"
            "then save the JSON output to artifacts/documents/NNNN_slug.json[/dim]"
        )
        return

    hint = "tweet" if tweet else ("audio" if audio else None)

    async def _run() -> None:
        from coin.pipeline.step1_ingest import run as ingest_run
        from coin.store.database import init_db
        await init_db()
        with console.status(f"Ingesting [bold]{source}[/bold]..."):
            doc_id = await ingest_run(source, media_type_hint=hint)
        console.print(f"[green]✓[/green] Ingested as doc #{doc_id}")
        console.print(f"  Artifact saved to [cyan]artifacts/documents/[/cyan]")

    asyncio.run(_run())


# ── coin embed ─────────────────────────────────────────────────────────────────

@app.command()
def embed() -> None:
    """Step 2 — Embed all un-embedded document chunks (always agent mode — uses embeddings API)."""
    async def _run() -> None:
        from coin.pipeline.step2_embed import run as embed_run
        from coin.store.database import init_db
        await init_db()
        with console.status("Embedding chunks..."):
            n = await embed_run()
        console.print(f"[green]✓[/green] Embedded {n} chunk(s).")

    asyncio.run(_run())


# ── coin group ─────────────────────────────────────────────────────────────────

@app.command()
def group(
    manual: bool = typer.Option(False, help="Print the prompt to paste into Claude.ai/ChatGPT"),
    apply: Path | None = typer.Option(None, help="Path to JSON response from the web UI"),
) -> None:
    """Step 3 — Cluster documents into topic groups."""
    async def _run() -> None:
        from coin.pipeline.step3_group import (
            print_manual_prompt,
            apply_manual_response,
            run_agent,
        )

        if manual:
            _mode_note(manual=True)
            prompt = await print_manual_prompt()
            console.print(Markdown(prompt))
            console.print("\n[dim]Prompt also saved to [cyan]artifacts/group_prompt.md[/cyan][/dim]")

        elif apply:
            data = await apply_manual_response(apply)
            console.print(f"[green]✓[/green] Saved {len(data['groups'])} group(s) to artifacts/groups.json")
            for g in data["groups"]:
                console.print(f"  • {g['label']} ({len(g['doc_ids'])} docs)")

        else:
            with console.status("Grouping documents (agent mode)..."):
                data = await run_agent()
            console.print(f"[green]✓[/green] {len(data['groups'])} topic group(s) saved to artifacts/groups.json")
            for g in data["groups"]:
                console.print(f"  • {g['label']} ({len(g['doc_ids'])} docs)")

    asyncio.run(_run())


# ── coin compile ───────────────────────────────────────────────────────────────

@app.command()
def compile(
    topic: str | None = typer.Option(None, help="Compile a single topic by label"),
    manual: bool = typer.Option(False, help="Print the prompt to paste into Claude.ai/ChatGPT"),
    apply: Path | None = typer.Option(None, help="Path to a drafted .md file to save into wiki/"),
) -> None:
    """Step 4 — Compile wiki articles from topic groups."""
    async def _run() -> None:
        from coin.pipeline.step4_compile import (
            print_manual_prompt,
            apply_manual_article,
            run_agent,
        )

        if manual:
            _mode_note(manual=True)
            prompt = await print_manual_prompt(topic)
            console.print(Markdown(prompt))
            console.print("\n[dim]Prompt also saved to [cyan]artifacts/compile_prompt.md[/cyan][/dim]")

        elif apply:
            slug = await apply_manual_article(apply)
            console.print(f"[green]✓[/green] Article saved to wiki/{slug}.md")

        else:
            with console.status("Compiling articles (agent mode)..."):
                titles = await run_agent(topic)
            console.print(f"[green]✓[/green] Compiled {len(titles)} article(s):")
            for t in titles:
                console.print(f"  • {t}")

    asyncio.run(_run())


# ── coin link ──────────────────────────────────────────────────────────────────

@app.command()
def link() -> None:
    """Step 5 — Resolve [[wikilinks]] and rebuild the backlink index."""
    async def _run() -> None:
        from coin.pipeline.step5_link import run as link_run
        with console.status("Linking articles..."):
            n = await link_run()
        console.print(f"[green]✓[/green] Resolved {n} backlink(s).")

    asyncio.run(_run())


# ── coin lint ──────────────────────────────────────────────────────────────────

@app.command()
def lint(
    manual: bool = typer.Option(False),
    apply: Path | None = typer.Option(None, help="Path to JSON findings file from the web UI"),
) -> None:
    """Step 6 — Find contradictions, gaps, and stale content."""
    async def _run() -> None:
        from coin.pipeline.step6_lint import (
            print_manual_prompt,
            apply_manual_findings,
            run_agent,
        )
        from rich.table import Table

        if manual:
            _mode_note(manual=True)
            prompt = await print_manual_prompt()
            console.print(Markdown(prompt))

        elif apply:
            findings = await apply_manual_findings(apply)
            console.print(f"[green]✓[/green] Recorded {len(findings)} finding(s).")

        else:
            with console.status("Linting (agent mode)..."):
                findings = await run_agent()

            if not findings:
                console.print("[green]✓[/green] No issues found.")
                return

            table = Table(title="Lint Findings")
            table.add_column("Kind", style="bold")
            table.add_column("Article")
            table.add_column("Detail")
            for f in findings:
                table.add_row(f["kind"], f.get("article_slug") or "—", f["detail"])
            console.print(table)

    asyncio.run(_run())


# ── coin ask ───────────────────────────────────────────────────────────────────

@app.command()
def ask(
    question: str = typer.Argument(),
    manual: bool = typer.Option(False, help="Print the Q&A prompt to paste into Claude.ai/ChatGPT"),
) -> None:
    """Step 7 — Ask a question against the knowledge base."""
    async def _run() -> None:
        from coin.pipeline.step7_qa import print_manual_prompt, run_agent

        if manual:
            _mode_note(manual=True)
            prompt = await print_manual_prompt(question)
            console.print(Markdown(prompt))
            return

        with console.status("Thinking..."):
            answer = await run_agent(question)

        console.rule(f"[bold]{question}[/bold]")
        console.print(answer["text"])
        if answer.get("web_searched"):
            console.print("[dim italic]↳ Supplemented with live web research[/dim italic]")
        console.print(f"\n[dim]Confidence: {answer['confidence']}[/dim]")
        if answer.get("citations"):
            console.print("\n[bold]Sources:[/bold]")
            for c in answer["citations"]:
                console.print(f"  • {c['source_url']}")

    asyncio.run(_run())


# ── coin run ───────────────────────────────────────────────────────────────────

@app.command()
def run() -> None:
    """Agent mode: run steps 2–6 end-to-end (embed → group → compile → link → lint)."""
    async def _run() -> None:
        from coin.agent.orchestrator import run_pipeline
        with console.status("Running full pipeline..."):
            result = await run_pipeline()
        console.print(f"[green]✓[/green] Pipeline complete. {result['articles']} article(s) compiled.")

    asyncio.run(_run())


# ── coin watch ─────────────────────────────────────────────────────────────────

watch_app = typer.Typer(help="Watch mode — auto-research on a schedule")
app.add_typer(watch_app, name="watch")


@watch_app.command("add")
def watch_add(
    topic: str = typer.Argument(),
    cron: str = typer.Option("0 9 * * 1", help="Cron expression"),
) -> None:
    """Add a topic to watch mode."""
    async def _run() -> None:
        from coin.store.database import get_db
        async with get_db() as db:
            await db.execute(
                "INSERT OR REPLACE INTO watched_topics (topic, cron) VALUES (?, ?)",
                (topic, cron),
            )
            await db.commit()
        console.print(f"[green]✓[/green] Watching [bold]{topic}[/bold] — cron: {cron}")

    asyncio.run(_run())


@watch_app.command("run")
def watch_run() -> None:
    """Run all scheduled watch topics now."""
    async def _run() -> None:
        from coin.agent.watcher import Watcher
        watcher = Watcher()
        with console.status("Running watch tasks..."):
            n = await watcher.run_all()
        console.print(f"[green]✓[/green] Updated {n} topic(s).")

    asyncio.run(_run())


# ── coin export ────────────────────────────────────────────────────────────────

export_app = typer.Typer()
app.add_typer(export_app, name="export")


@export_app.command("html")
def export_html(out: Path = typer.Option(Path("./export"))) -> None:
    """Export the KB as an HTML report."""
    async def _run() -> None:
        from coin.export.html_exporter import HtmlExporter
        with console.status("Exporting HTML..."):
            path = await HtmlExporter().export(out)
        console.print(f"[green]✓[/green] {path}")

    asyncio.run(_run())


@export_app.command("pdf")
def export_pdf(out: Path = typer.Option(Path("./coin.pdf"))) -> None:
    """Export as PDF."""
    async def _run() -> None:
        from coin.export.pdf_exporter import PdfExporter
        with console.status("Generating PDF..."):
            path = await PdfExporter().export(out)
        console.print(f"[green]✓[/green] {path}")

    asyncio.run(_run())


@export_app.command("snapshot")
def export_snapshot(out: Path = typer.Option(Path("./coin-snapshot.json"))) -> None:
    """Export a full-KB JSON snapshot."""
    async def _run() -> None:
        from coin.export.snapshot import export_snapshot as snap
        with console.status("Snapshotting..."):
            path = await snap(out)
        console.print(f"[green]✓[/green] {path}")

    asyncio.run(_run())


# ── coin serve ─────────────────────────────────────────────────────────────────

@app.command()
def serve(
    host: str = typer.Option("127.0.0.1"),
    port: int = typer.Option(7860),
    reload: bool = typer.Option(False),
) -> None:
    """Start the COIN web UI."""
    import uvicorn
    console.print(f"[bold]COIN[/bold] → http://{host}:{port}")
    uvicorn.run("coin.web.app:app", host=host, port=port, reload=reload)


if __name__ == "__main__":
    app()
