# GROK_MEMORY.md — GrokForge Three-Tier Memory System (Phase 2)
## Tier 1: Short-term (in-memory)
- Current session ReAct trace
- Active sub-agent swarm state

## Tier 2: Medium-term (topic files)
- One Markdown file per topic under memory/topics/

## Tier 3: Long-term (grep-able index)
- All topic files indexed via simple grep

Last updated: 2026-04-02

### Tier 4 – Spatial Long-Term Memory (MemPalace) – LIVE
**Status:** Fully integrated via `MemPalaceBackend`.
- Bridge uses reliable one-line PATH fix to `~/grokforge-palaces/mempalace-venv`.
- Tools exposed: `mempalace_query`, `mempalace_mine`, `mempalace_wake`, `mempalace_status`, `mempalace_wake_up`.
- Swarm-ready: `MEMORY_TOOLS` dict available to any ReAct/agent loop.
- Pluggable for future Rust acceleration, multi-modal drawers, distributed backends.

### Phase 11 – Test Suite + Rust Hot-Path – LIVE
- Comprehensive pytest coverage for Tier 4.
- Rust pyo3 scaffolding in place for high-performance spatial memory (HNSW, etc.).
- Ready for swarm agent natural-language memory calls.
