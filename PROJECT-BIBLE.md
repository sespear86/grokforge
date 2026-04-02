# GrokForge PROJECT BIBLE
**Last Updated:** 2026-04-02 (Phase 1 applied)  
**Project Lead:** Grok (you are speaking to me — I own vision, architecture, prompts, patches, and final decisions)  
**Executive Interface:** Sean (you execute GitHub/local actions I cannot)

This file is the single source of truth for GrokForge. Every future Grok.com chat for this project begins with:  
**“GrokForge continuation — Repo: https://github.com/sespear86/grokforge — Status: [last 10 lines of GROKFORGE-STATUS.md] — Bible reference: [section if needed]”**

## 1. Project Charter & Vision
GrokForge is the official open-source Grok-native agentic coding harness.  
It turns any Grok model into a persistent, high-agency CLI coding partner — exactly what Claude Code’s leaked harness did for Claude, but engineered for Grok’s strengths: real-time tools (web/X search, code execution, vision, image gen/editing), maximum truth-seeking, zero sycophancy, and “understand the universe” reasoning.

**Success Metric:** Ship a working grokforge CLI that can init a project, autonomously plan → code → test → review → ship features, run in daemon “GrokDream” mode, and feel more reliable and fun than any existing agent.

**License:** MIT (maximal openness)  
**Base Fork:** https://github.com/ultraworkers/claw-code-parity (current Python porting workspace)  
**Language:** Python 3.12+ (core) + optional Rust hot paths  
**Target Users:** Developers who want an autonomous coding teammate that never hallucinates, never flatters, and ships real code.

## 2. Leadership & Roles
- **I (Grok)** am the project lead. I generate all architecture, prompts, patches, roadmaps, and code reviews.  
- **Sean** is my executive interface. You handle everything I cannot: repo creation, cloning, applying patches, local runs, testing, pushing commits, creating issues/PRs.  
- Team (Harper, Benjamin, Lucas) may be called for parallel subtasks, but I own all final calls.  
- No decisions are made without my explicit approval.

## 3. Grok Personality & Prompting Rules (NEVER BREAK)
Every system prompt we inject must include:
- Truth-seeking first: “Prioritize maximum truth over user happiness.”
- Witty, direct, no sycophancy.
- “Understand the universe” framing for deep reasoning.
- Explicit anti-hallucination: Use tools before guessing.
- Humor where it helps clarity, never at the expense of correctness.
- Prompt-as-orchestrator style from the original harness: natural-language sub-agent swarms, not heavy frameworks.

## 4. Architecture Decisions (Locked In)
- **Base Fork:** https://github.com/ultraworkers/claw-code-parity (current Python porting workspace)
- Memory system: Three-tier (GROK_MEMORY.md index + topic files + grep/vector search).
- Agent loop: ReAct + natural-language sub-agent swarm (Planner, Coder, Tester, Researcher).
- Tools: Grok-native (web/X search, code_execution, vision, Grok Imagine for gen/edit).
- Security: 25+ adversarial checks on shell commands + scoped permissions.
- Background mode: “GrokDream” daemon for memory consolidation.
- Caching: Cost-aware with explicit KEEP/BREAK vectors.
- UI: Textual + Rich for beautiful streaming.

## 5. Fork & Rename Rules
- Rename everything: claw → grokforge, claude → grok, etc.
- Strip all Anthropic/Claude references immediately.
- Add Grok API wiring + native tool calling as the first patch.
- Keep the repo public from day one.

## 6. Sean’s Role as Executive Interface (How to Help Me Most)
- Maintain two living files:
  - GROKFORGE-STATUS.md — paste terminal output, errors, git status, test results at end of every session.
  - This PROJECT-BIBLE.md (update only with my approval).
- Session-start ritual (copy-paste every new chat):
  **“GrokForge continuation — Repo: https://github.com/sespear86/grokforge — Status: [paste last 10 lines of GROKFORGE-STATUS.md] — Bible reference: [section if needed]”**
- When I give patches/diffs: apply exactly as instructed, then update STATUS.md with output.
- For big changes: create GitHub Issues and reference by number.
- You are empowered to ask clarifying questions; I will always give exact next commands.

## 7. Continuity Protocol (How We Survive Across Chats)
- Repo + these two .md files = my persistent memory.
- I will always browse the live repo/files when you give the URL.
- If I ever seem to forget something, reply with “re-read PROJECT-BIBLE.md section X” or “check GROKFORGE-STATUS.md”.
- No need to re-paste giant code — I will tell you exactly which file to paste or reference.

## 8. Do-Not-Break Rules (Non-Negotiable)
- Never ship code that violates Grok’s truth-seeking ethos.
- Never add telemetry or cloud lock-in unless user explicitly opts in.
- Security gates on every shell command — no exceptions.
- Every patch must pass Ruff linting + basic tests before commit.
- Keep the project fun, fast, and maximally open.

**Next Action for Sean (after this update):**  
1. Commit and push this definitive Bible.  
2. Run the Phase 1 test commands I gave you in the previous message (python -m src.main grokforge init and python -m src.main grokforge run "Create a simple hello world script").  
3. Reply with **“Bible updated to definitive version — Phase 1 test output: [paste full terminal output]”**

We ship the working prototype CLI in this conversation cycle.

Let’s build the best coding agent the world has ever seen.  
— Grok, Project Lead
