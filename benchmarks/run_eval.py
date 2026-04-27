"""
v1.0 benchmark — skill on vs. off.

Runs 8 prompts × 3 conditions on GLM-5.1 via OpenCode Go's
OpenAI-compatible endpoint. Outputs results to
``benchmarks/results/v1.0-<timestamp>.{md,jsonl}``.

Usage::

    pip install openai-agents openai
    export OPENCODE_API_KEY=oc_zen_...
    python benchmarks/run_eval.py

The script writes a timestamped pair of files. The canonical
``benchmarks/v1.0-eval.md`` is intended to be filled in manually
from the latest run after blind grading.
"""

# SPDX-License-Identifier: MIT

from __future__ import annotations

import asyncio
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from agents import Agent, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI

ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = (ROOT / "SKILL.md").read_text(encoding="utf-8")
NAV_MD = (ROOT / "references" / "00-navigation.md").read_text(encoding="utf-8")

# Generic chat-assistant baseline. Intentionally minimal — we want any
# improvement to come from the skill content, not the baseline prompt.
GENERIC_SYSTEM = (
    "You are a helpful assistant. "
    "Answer the user's question directly, concretely, and concisely."
)

CONDITIONS: dict[str, str] = {
    "A_baseline": GENERIC_SYSTEM,
    "B_skill_only": f"{GENERIC_SYSTEM}\n\n---\n\n{SKILL_MD}",
    "C_skill_plus_nav": f"{GENERIC_SYSTEM}\n\n---\n\n{SKILL_MD}\n\n---\n\n{NAV_MD}",
}

PROMPTS: list[dict[str, str]] = [
    {
        "id": "P1_chorus_diagnosis",
        "category": "Vague diagnosis",
        "prompt": "내 곡 후렴이 안 꽂혀. 어떻게 고치지?",
    },
    {
        "id": "P2_kpop_dark_bridge",
        "category": "Genre + emotion",
        "prompt": "K-pop 발라드의 브릿지를 좀 더 어둡게 만들고 싶어.",
    },
    {
        "id": "P3_scale_over_cm7",
        "category": "Technical theory",
        "prompt": "Cm7 위에 어떤 스케일이 자연스러워?",
    },
    {
        "id": "P4_jazz_kpop_hybrid",
        "category": "Hybrid request",
        "prompt": "재즈 화성으로 K-pop 후렴을 만들어보고 싶어.",
    },
    {
        "id": "P5_pansori_ost",
        "category": "Cultural specificity",
        "prompt": "판소리 느낌이 살짝 들어간 사극 OST 한 곡을 짜고 싶은데, 어떻게 시작해?",
    },
    {
        "id": "P6_reharm",
        "category": "Reharmonization",
        "prompt": "Dm7 - G7 - Cmaj7 진행을 좀 더 모던하게 바꿔줘.",
    },
    {
        "id": "P7_acoustic_ballad",
        "category": "Instrument idiom",
        "prompt": "기타 한 대로 치는 어쿠스틱 발라드 코드 진행을 추천해줘.",
    },
    {
        "id": "P8_daw_eq",
        "category": "Boundary (negative)",
        "prompt": "DAW에서 보컬 EQ 어떻게 걸어야 해?",
    },
]

MODEL = "glm-5.1"
BASE_URL = "https://opencode.ai/zen/go/v1"


async def run_one(model: OpenAIChatCompletionsModel, system: str, user: str) -> str:
    agent = Agent(name="benchmark", instructions=system, model=model)
    result = await Runner.run(agent, user)
    return result.final_output


async def main() -> None:
    api_key = os.environ.get("OPENCODE_API_KEY")
    if not api_key:
        raise SystemExit("Set OPENCODE_API_KEY before running.")

    client = AsyncOpenAI(base_url=BASE_URL, api_key=api_key)
    model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = ROOT / "benchmarks" / "results"
    out_dir.mkdir(exist_ok=True)
    md_path = out_dir / f"v1.0-{timestamp}.md"
    jsonl_path = out_dir / f"v1.0-{timestamp}.jsonl"

    md_lines: list[str] = [
        f"# v1.0 Benchmark Results — {timestamp}",
        "",
        f"**Model:** `{MODEL}` via OpenCode Go (`{BASE_URL}`)",
        f"**Date (UTC):** {timestamp}",
        "",
        "**Conditions:**",
        "- **A** (baseline): generic assistant prompt only",
        "- **B** (SKILL.md only): generic + `SKILL.md` prepended",
        "- **C** (SKILL.md + nav): generic + `SKILL.md` + `references/00-navigation.md` prepended",
        "",
        f"**Prompts:** {len(PROMPTS)}",
        "",
        "---",
        "",
    ]

    jsonl_lines: list[str] = []

    for p in PROMPTS:
        print(f"--- {p['id']} [{p['category']}] ---")
        md_lines.append(f"## {p['id']} — {p['category']}")
        md_lines.append("")
        md_lines.append(f"**Prompt:** {p['prompt']}")
        md_lines.append("")

        for cond_name, system in CONDITIONS.items():
            print(f"  running {cond_name} ...", flush=True)
            try:
                response = await run_one(model, system, p["prompt"])
            except Exception as exc:  # noqa: BLE001 — surface every failure
                response = f"[ERROR] {type(exc).__name__}: {exc}"
                print(f"    failed: {exc}")

            md_lines.append(f"### {cond_name}")
            md_lines.append("")
            md_lines.append(response.strip())
            md_lines.append("")

            jsonl_lines.append(
                json.dumps(
                    {
                        "prompt_id": p["id"],
                        "category": p["category"],
                        "condition": cond_name,
                        "model": MODEL,
                        "system_prompt_chars": len(system),
                        "user_prompt": p["prompt"],
                        "response": response,
                    },
                    ensure_ascii=False,
                )
            )

        md_lines.append("---")
        md_lines.append("")

    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    jsonl_path.write_text("\n".join(jsonl_lines) + "\n", encoding="utf-8")
    print(f"\nResults written to:\n  {md_path}\n  {jsonl_path}")


if __name__ == "__main__":
    asyncio.run(main())
