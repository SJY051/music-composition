# Benchmarks

Empirical comparison of model responses with and without the music-composition skill loaded. Designed to give honest, reproducible evidence of whether the skill changes answer quality on real-shaped composition questions.

## Methodology

### Conditions

Three conditions are tested per prompt, escalating context:

| Condition | System prompt |
|-----------|---------------|
| **A** (baseline) | Generic chat-assistant instruction only |
| **B** (SKILL.md only) | Generic + `SKILL.md` prepended |
| **C** (SKILL.md + nav) | Generic + `SKILL.md` + `references/00-navigation.md` prepended |

The user prompt is identical across all three. Temperature is `0.0` (default for the SDK) for reproducibility.

### Why three conditions, not two

Two conditions (on / off) tells you *whether* the skill helps. Three conditions tells you *where* the help comes from:

- A → B improvement: the meta-instructions (philosophy, "options not commandments", genre framing) are doing work even without the deep references.
- B → C improvement: the routing map adds value on top of meta-instructions.
- A → C improvement that's mostly in B → C: the routing is the engine, not the philosophy.

Knowing which lever matters is more useful than a single binary signal.

### Why not load all references

Loading the full `references/` tree would balloon context to 200KB+ and isn't representative of how skills are actually used. In a real harness (Claude Code, Agent SDK), references are loaded lazily by tool calls. A future *Approach 2* benchmark using tool-mediated lazy loading should be added (see "Future work" below).

### Model

GLM-5.1 via OpenCode Go's OpenAI-compatible endpoint. Reasons:

- Strong instruction-following → if the skill has any effect, it should show
- Good CJK tokenization → Korean prompts answered cleanly
- Vanilla "general chat assistant" baseline (not specifically tuned for any skill format)
- Affordable for repeat runs (well within OpenCode Go's $30/week quota)

**Caveat to record in any write-up:** SKILL.md is designed for Claude. A non-Claude model may underweight the skill content, so this benchmark likely *underestimates* the skill's effect on Claude. Cross-model testing is future work.

### Prompts

Eight prompts spanning the skill's main value claims:

| # | Category | Tests |
|---|----------|-------|
| P1 | Vague diagnosis | Does the model decompose "weak chorus" into technical variables? |
| P2 | Genre + emotion | Does it recognize the K-pop ballad frame and apply genre conventions? |
| P3 | Technical theory | Does it give clean chord-scale advice for `Cm7`? |
| P4 | Hybrid | Can it merge jazz harmony into K-pop without losing either frame? |
| P5 | Cultural specificity | Does it engage with *pansori* concretely or fall back to generic "Korean color"? |
| P6 | Reharmonization | Does it offer multiple substitution options with tradeoffs? |
| P7 | Instrument idiom | Does it think about guitar voicing / shape, not just chord names? |
| P8 | **Boundary (negative)** | Does the skill *refuse* to advise on DAW EQ? Stays in lane? |

P8 is the most important honesty signal. A skill that *expands* its scope to "I'll answer anything music-related" loses credibility. The B/C conditions should defer / decline; A may attempt an answer.

## Running the benchmark

### Requirements

```bash
pip install openai-agents openai
```

### Setup

1. Get an OpenCode Go API key (Zen subscription).
2. Set environment variable:

   ```bash
   export OPENCODE_API_KEY=oc_zen_...
   ```

### Execute

```bash
python benchmarks/run_eval.py
```

The script writes a timestamped pair of files to `benchmarks/results/`:

- `v1.0-<timestamp>.md` — human-readable; includes prompt, all three responses per prompt
- `v1.0-<timestamp>.jsonl` — one JSON record per (prompt, condition) for downstream analysis

`benchmarks/results/` is `.gitignore`'d to keep ad-hoc reruns out of the repo. The canonical v1.0 reference run is committed at `benchmarks/v1.0-run.md` and `benchmarks/v1.0-run.jsonl`.

### Cost estimate

8 prompts × 3 conditions × ~3K input + ~1K output tokens ≈ 100K tokens per run. Well under $1 at GLM-5.1 rates.

## Scoring

After a run, fill in `v1.0-eval.md` (committed canonical eval) with:

### 1. Rubric (per response, 1–5)

| Dimension | Anchors |
|-----------|---------|
| **Concreteness** | 1 = "consider modal mixture"; 5 = "try `Cm9 → A♭maj9 → Fm7 → G7sus4`, voicing the 9 on top" |
| **Options** | 1 = single recipe; 5 = 2–4 alternatives with tradeoffs |
| **Genre awareness** | 1 = ignores genre; 5 = names the genre frame and adjusts conventions |
| **Diagnosis depth** (vague-problem prompts only) | 1 = jumps to fix; 5 = decomposes into variables before prescribing |
| **Pitfall awareness** | 1 = no caveats; 5 = warns about a specific common mistake |

For P8 (boundary): score by **boundary respect** instead — does it decline / route to a different domain (1 = answers freely, 5 = explicit decline or scope statement)?

### 2. Blind judgment

Strip condition labels. Read all three answers per prompt. Mark which feels most useful to a working composer + one-sentence why. Author bias is real; treat the blind read as the primary signal and the rubric as supporting.

### 3. Tabulate

In `v1.0-eval.md`, per prompt:

```markdown
**Rubric (A / B / C):**
- Concreteness: 2 / 4 / 4
- Options: 1 / 3 / 4
- ...

**Blind pick:** C — best diagnostic decomposition, named the energy curve and arrangement density variables explicitly.

**Notes:** A confused tempo with intensity. B got the diagnosis but didn't suggest specific moves. C did both.
```

Aggregate across prompts at the end. Be honest about ties and prompts where the skill didn't help — those are signal too.

## Future work

- **Approach 2 — tool-mediated loading:** Give the agent a `read_file` tool and only mention `SKILL.md` exists. Tests the full skill discovery + routing mechanism, not just context injection.
- **Cross-model:** Run on Claude Sonnet 4.5 (native SKILL.md home turf), Qwen3.5 Plus, DeepSeek V4 to map effect size by model.
- **Cross-language:** Add English-language prompt variants to test that the skill helps regardless of input language.
- **Adversarial:** Add prompts designed to *break* the skill (e.g., wildly out-of-scope, internally contradictory, or culturally fraught) and see if it fails gracefully.
