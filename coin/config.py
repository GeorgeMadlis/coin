"""coin/config.py — Pydantic settings, reads .env"""

from __future__ import annotations
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="COIN_", extra="ignore")

    # Operating mode
    mode: Literal["manual", "agent"] = "manual"

    # LLM (only needed in agent mode)
    llm_provider: Literal["anthropic", "openai", "ollama"] = "anthropic"
    anthropic_model: str = "claude-sonnet-4-20250514"
    openai_model: str = "gpt-4o"
    ollama_model: str = "llama3"
    ollama_base_url: str = "http://localhost:11434"

    # Embeddings (only needed in agent mode)
    embed_provider: Literal["openai", "ollama"] = "ollama"
    embed_model: str = "nomic-embed-text"
    embed_dim: int = 1536

    # Storage
    db_path: str = "./coin.db"
    wiki_dir: str = "./wiki"
    artifacts_dir: str = "./artifacts"

    # Web
    host: str = "127.0.0.1"
    port: int = 7860

    # Ingestion
    chunk_size: int = 512
    chunk_overlap: int = 64
    max_tokens_per_doc: int = 32000

    # Q&A
    qa_confidence_threshold: float = 0.65
    qa_max_web_searches: int = 3

    # Watch mode
    watch_enabled: bool = False
    stale_days: int = 90


settings = Settings()
