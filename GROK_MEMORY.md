# GROK_MEMORY.md — GrokForge Three-Tier Memory System (Phase 2)
## Tier 1: Short-term (in-memory)
- Current session ReAct trace
- Active sub-agent swarm state

## Tier 2: Medium-term (topic files)
- One Markdown file per topic under memory/topics/

## Tier 3: Long-term (grep-able index)
- All topic files indexed via simple grep

Last updated: 2026-04-02

## Tier 4 – Spatial Long-Term Memory (MemPalace Backend) – LIVE
**Implemented:** `memory/backends.py` + `MemPalaceBackend` (pluggable via abstract `MemoryBackend`)

- Full bridge to side palace (Python 3.12 venv)
- Supports `status`, `wake_up`, `search`, `mine`, `grokforge_wake_up`
- Zero scope limits – ready for Rust hot-path, multi-modal drawers, swarm agents
- Default backend exposed via `memory.get_backend()`

This completes the 4-tier memory architecture exactly as specified in PROJECT-BIBLE.md.
