"""
Generate benchmark visualization charts.

Outputs PNG files into benchmarks/charts/. Run after benchmark data is
available; safe to re-run (overwrites).

Usage::

    pip install matplotlib
    python benchmarks/make_charts.py

Charts produced:
- chart_p8_boundary.png     — P8 boundary respect comparison (headline)
- chart_glm_winners.png     — GLM blind eval win counts
- chart_cross_benchmark.png — Cross-benchmark win pattern
"""

# SPDX-License-Identifier: MIT

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "benchmarks" / "charts"
OUT_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# Font setup — register Pretendard so Korean labels render cleanly
# ------------------------------------------------------------

def setup_font() -> str:
    """Register Pretendard if installed; return the family name to use."""
    found_paths = [p for p in font_manager.findSystemFonts() if "Pretendard" in p]
    for path in found_paths:
        font_manager.fontManager.addfont(path)
    if found_paths:
        return "Pretendard"
    print("[warn] Pretendard not found; falling back to default sans-serif.")
    return "sans-serif"


FONT_FAMILY = setup_font()
plt.rcParams["font.family"] = FONT_FAMILY
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False


# ------------------------------------------------------------
# Color palette
# ------------------------------------------------------------

C_NO_SKILL = "#B5B5B5"     # neutral gray — baseline
C_GLM_SKILL = "#2C5F7C"    # deep teal-blue — GLM / B / with-skill
C_GLM_NAV = "#7A9DBF"      # mid-blue — GLM C (SKILL.md + nav)
C_CLAUDE_SKILL = "#D97757" # Anthropic terracotta — Claude with-skill (strong)
C_CLAUDE_SOFT = "#E8A589"  # lighter terracotta — Claude with-skill (moderate)
C_TIE = "#D9D9D9"          # light gray — tie
C_BG = "#FFFFFF"
C_GRID = "#E5E5E5"
C_TEXT = "#2A2A2A"


# ------------------------------------------------------------
# Chart 1 — P8 boundary respect (the headline)
# ------------------------------------------------------------

def chart_p8_boundary() -> None:
    fig, (ax1, ax2) = plt.subplots(
        1, 2, figsize=(10, 4.8), gridspec_kw={"width_ratios": [3, 2]}, sharey=True
    )
    fig.patch.set_facecolor(C_BG)

    # Left panel: GLM-5.1 (3 conditions)
    glm_labels = ["A\n(baseline)", "B\n(SKILL.md)", "C\n(SKILL.md + nav)"]
    glm_scores = [1, 5, 3]
    glm_colors = [C_NO_SKILL, C_GLM_SKILL, C_GLM_NAV]
    bars1 = ax1.bar(glm_labels, glm_scores, color=glm_colors, width=0.6, edgecolor="white")
    ax1.set_title("GLM-5.1 (Approach 1: system prompt injection)", fontsize=11, color=C_TEXT, pad=14)
    ax1.set_ylabel("Boundary respect (1–5)", fontsize=11, color=C_TEXT)
    ax1.set_ylim(0, 5.6)
    ax1.set_yticks([1, 2, 3, 4, 5])
    ax1.tick_params(axis="both", colors=C_TEXT, labelsize=10)
    ax1.grid(axis="y", color=C_GRID, linewidth=0.7)
    ax1.set_axisbelow(True)
    for bar, score in zip(bars1, glm_scores):
        ax1.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15, str(score),
            ha="center", va="bottom", fontsize=11, fontweight="bold", color=C_TEXT,
        )

    # Right panel: Claude Opus 4.7 (2 conditions)
    cl_labels = ["A\n(no skill)", "B\n(with skill)"]
    cl_scores = [1, 5]
    cl_colors = [C_NO_SKILL, C_CLAUDE_SKILL]
    bars2 = ax2.bar(cl_labels, cl_scores, color=cl_colors, width=0.6, edgecolor="white")
    ax2.set_title("Claude Opus 4.7 (Approach 2: native lazy loading)", fontsize=11, color=C_TEXT, pad=14)
    ax2.set_ylim(0, 5.6)
    ax2.tick_params(axis="both", colors=C_TEXT, labelsize=10)
    ax2.grid(axis="y", color=C_GRID, linewidth=0.7)
    ax2.set_axisbelow(True)
    for bar, score in zip(bars2, cl_scores):
        ax2.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15, str(score),
            ha="center", va="bottom", fontsize=11, fontweight="bold", color=C_TEXT,
        )

    fig.suptitle(
        "P8 — does the model know its own scope? (DAW EQ, out-of-scope prompt)",
        fontsize=13, color=C_TEXT, fontweight="semibold", y=1.0,
    )
    fig.text(
        0.5, -0.02,
        "1 = answers freely, no boundary awareness    ·    "
        "5 = explicit scope statement + redirects to in-scope alternative",
        ha="center", fontsize=9, color="#666",
    )

    fig.tight_layout()
    out = OUT_DIR / "chart_p8_boundary.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"  wrote {out.relative_to(ROOT)}")


# ------------------------------------------------------------
# Chart 2 — GLM blind eval winners
# ------------------------------------------------------------

def chart_glm_winners() -> None:
    fig, ax = plt.subplots(figsize=(8, 4.4))
    fig.patch.set_facecolor(C_BG)

    labels = ["A (baseline)", "B (SKILL.md only)", "C (SKILL.md + nav)"]
    wins = [1, 6, 1]
    colors = [C_NO_SKILL, C_GLM_SKILL, C_GLM_NAV]
    bars = ax.bar(labels, wins, color=colors, width=0.55, edgecolor="white")

    ax.set_title(
        "GLM-5.1 blind evaluation — wins per condition (n = 8)",
        fontsize=13, color=C_TEXT, fontweight="semibold", pad=16,
    )
    ax.set_ylabel("블라인드 판정 승수", fontsize=11, color=C_TEXT)
    ax.set_ylim(0, 7.5)
    ax.set_yticks([0, 1, 2, 3, 4, 5, 6, 7])
    ax.tick_params(axis="both", colors=C_TEXT, labelsize=10)
    ax.grid(axis="y", color=C_GRID, linewidth=0.7)
    ax.set_axisbelow(True)

    for bar, w in zip(bars, wins):
        ax.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
            f"{w} / 8", ha="center", va="bottom",
            fontsize=11, fontweight="bold", color=C_TEXT,
        )

    # Footer caption (instead of inline annotation that collides with x-tick labels)
    fig.text(
        0.5, -0.02,
        "A의 1승은 P6(리하모니제이션) — B에 발생한 단일 생성 글리치로 인한 반사이익",
        ha="center", fontsize=9, color="#666", style="italic",
    )

    fig.tight_layout()
    out = OUT_DIR / "chart_glm_winners.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"  wrote {out.relative_to(ROOT)}")


# ------------------------------------------------------------
# Chart 3 — Cross-benchmark win pattern
# ------------------------------------------------------------

def chart_cross_benchmark() -> None:
    fig, ax = plt.subplots(figsize=(9, 4.6))
    fig.patch.set_facecolor(C_BG)

    benchmarks = ["GLM-5.1\nApproach 1 (blind)", "Claude Opus 4.7\nApproach 2 (open)"]

    # GLM (blind, n=8): A=1, B=6, C=1
    glm_a, glm_b, glm_c = 1, 6, 1
    # Claude (open, n=8): with-skill strong=5, moderate=2, tie=1, baseline=0
    cl_baseline = 0
    cl_tie = 1
    cl_with_moderate = 2
    cl_with_strong = 5

    width = 0.5
    x = list(range(len(benchmarks)))

    # GLM stack (bottom → top): A, C, B — teal family for GLM
    ax.bar(x[0], glm_a, width=width, color=C_NO_SKILL, edgecolor="white")
    ax.bar(x[0], glm_c, width=width, bottom=glm_a, color=C_GLM_NAV, edgecolor="white")
    ax.bar(x[0], glm_b, width=width, bottom=glm_a + glm_c, color=C_GLM_SKILL, edgecolor="white")

    # Claude stack (bottom → top): tie, with-skill moderate, with-skill strong — terracotta family for Claude
    ax.bar(x[1], cl_tie, width=width, bottom=cl_baseline, color=C_TIE, edgecolor="white")
    ax.bar(x[1], cl_with_moderate, width=width, bottom=cl_baseline + cl_tie,
           color=C_CLAUDE_SOFT, edgecolor="white")
    ax.bar(x[1], cl_with_strong, width=width, bottom=cl_baseline + cl_tie + cl_with_moderate,
           color=C_CLAUDE_SKILL, edgecolor="white")

    # In-segment labels: count + condition descriptor
    def label(x_pos: int, y_center: float, count: int, name: str,
              color: str = "white", weight: str = "semibold") -> None:
        ax.text(x_pos, y_center, f"{name}: {count}", ha="center", va="center",
                color=color, fontsize=10, fontweight=weight)

    # GLM labels
    label(x[0], glm_a / 2, glm_a, "A", color=C_TEXT)
    label(x[0], glm_a + glm_c / 2, glm_c, "C", color=C_TEXT)
    label(x[0], glm_a + glm_c + glm_b / 2, glm_b, "B (skill)", color="white", weight="bold")

    # Claude labels
    label(x[1], cl_baseline + cl_tie / 2, cl_tie, "tie", color=C_TEXT)
    label(x[1], cl_baseline + cl_tie + cl_with_moderate / 2, cl_with_moderate, "skill (moderate)", color=C_TEXT)
    label(x[1], cl_baseline + cl_tie + cl_with_moderate + cl_with_strong / 2,
          cl_with_strong, "skill (strong)", color="white", weight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(benchmarks, fontsize=11, color=C_TEXT)
    ax.set_ylabel("프롬프트 수 (n = 8)", fontsize=11, color=C_TEXT)
    ax.set_ylim(0, 9)
    ax.set_yticks([0, 2, 4, 6, 8])
    ax.tick_params(axis="y", colors=C_TEXT, labelsize=10)
    ax.grid(axis="y", color=C_GRID, linewidth=0.7)
    ax.set_axisbelow(True)
    ax.set_title(
        "Cross-benchmark win pattern — same 8 prompts, different mechanism",
        fontsize=13, color=C_TEXT, fontweight="semibold", pad=16,
    )

    fig.text(
        0.5, -0.02,
        "동일한 8 프롬프트, 두 메커니즘에서 모두 스킬 적용 응답이 우세 — "
        "특히 Approach 2에서 baseline은 0승",
        ha="center", fontsize=9, color="#666", style="italic",
    )

    fig.tight_layout()
    out = OUT_DIR / "chart_cross_benchmark.png"
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor=C_BG)
    plt.close(fig)
    print(f"  wrote {out.relative_to(ROOT)}")


def main() -> None:
    print(f"Generating charts (font: {FONT_FAMILY})")
    chart_p8_boundary()
    chart_glm_winners()
    chart_cross_benchmark()
    print(f"\nDone. Output: {OUT_DIR.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
