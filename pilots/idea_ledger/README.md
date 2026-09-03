# Idea Ledger Pilot — Deterministic Baseline

This directory contains the non-AI reference implementation for `SH-PILOT-001` and the first benchmark against which AI-assisted and hybrid variants will be measured.

## Files

- `idea_ledger.py` — deterministic reference implementation.
- `test_idea_ledger.py` — standard-library `unittest` test harness.
- `benchmark.py` — repeatable latency/success benchmark.
- `baseline-results.json` — first recorded local validation snapshot.

## Requirements

- Python 3.10+ recommended.
- No external Python packages.
- No API keys.
- No network access.

## Run tests

From this directory:

```bash
python -m unittest -v
```

Expected baseline: all tests pass before any AI-assisted implementation is compared.

## Run benchmark

```bash
python benchmark.py
```

The benchmark seeds 100 synthetic ideas and measures 200 iterations each of:

- create;
- get;
- filtered list;
- update;
- health check.

The benchmark reports deterministic success rate and operation latency. It records `ai_calls = 0` and `ai_cost_usd = 0.0` by definition.

## Comparison contract for future variants

Every AI-assisted or hybrid implementation should preserve equivalent user-visible behavior and emit at least:

```json
{
  "implementation": "deterministic|ai_assisted|hybrid",
  "provider": null,
  "model": null,
  "ai_calls": 0,
  "ai_cost_usd": 0.0,
  "overall_success_rate": 1.0,
  "measurements": []
}
```

Additional AI measurements should include:

- provider/model provenance;
- time to first response;
- end-to-end task latency;
- input/output usage and cost where available;
- generated-code test pass rate;
- human correction count;
- repair attempts/success;
- approval compliance;
- learning-effectiveness measurements.

## Fair-comparison rules

1. Run deterministic, AI-assisted, and hybrid variants on the same machine/environment when comparing latency.
2. Use the same synthetic fixtures and scenario definitions.
3. Do not count a generated answer as successful unless deterministic validation passes.
4. Separate model latency from total workflow latency.
5. Report retries and failed-call cost.
6. Preserve hard-stop criteria from Prompt #11.
7. Do not average away safety, privacy, or approval failures.

## Baseline interpretation

The deterministic implementation is expected to be extremely fast and effectively cost-zero for basic CRUD and validation. AI variants are not expected to beat it at simple data operations. Their viability must instead come from higher-level value such as:

- understanding natural-language requirements;
- tutoring;
- generating code/tests/docs;
- diagnosing unfamiliar failures;
- adapting content;
- producing useful explanations;
- reducing overall human effort.

The hybrid target is therefore: **AI for ambiguity and generation; deterministic code for truth, state, validation, permissions, and promotion.**
