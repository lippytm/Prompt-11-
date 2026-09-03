from __future__ import annotations

import json
from pathlib import Path
from statistics import median
from time import perf_counter
from typing import Callable

from idea_ledger import IdeaLedger, Priority, Status


def _measure(name: str, fn: Callable[[], object], iterations: int = 200) -> dict:
    durations_ms: list[float] = []
    failures = 0
    for _ in range(iterations):
        start = perf_counter()
        try:
            fn()
        except Exception:
            failures += 1
        durations_ms.append((perf_counter() - start) * 1000)

    ordered = sorted(durations_ms)
    p95_index = max(0, min(len(ordered) - 1, int(len(ordered) * 0.95) - 1))
    return {
        "name": name,
        "iterations": iterations,
        "failures": failures,
        "success_rate": (iterations - failures) / iterations,
        "median_latency_ms": median(durations_ms),
        "p95_latency_ms": ordered[p95_index],
        "min_latency_ms": min(durations_ms),
        "max_latency_ms": max(durations_ms),
    }


def build_seeded_ledger(size: int = 100) -> IdeaLedger:
    ledger = IdeaLedger()
    for i in range(size):
        ledger.create(
            title=f"Idea {i}",
            description=f"Synthetic benchmark idea {i}",
            category="benchmark" if i % 2 == 0 else "learning",
            priority=Priority.HIGH if i % 3 == 0 else Priority.MEDIUM,
            tags=["synthetic", f"bucket-{i % 5}"],
        )
    return ledger


def run_baseline(iterations: int = 200) -> dict:
    ledger = build_seeded_ledger()
    sample_id = ledger.list()[0].idea_id

    measurements = [
        _measure(
            "create",
            lambda: ledger.create(
                title="Benchmark create",
                description="Synthetic",
                category="benchmark",
            ),
            iterations,
        ),
        _measure("get", lambda: ledger.get(sample_id), iterations),
        _measure("list_filtered", lambda: ledger.list(category="benchmark"), iterations),
        _measure(
            "update",
            lambda: ledger.update(sample_id, status=Status.TESTING),
            iterations,
        ),
        _measure("health_check", ledger.health_check, iterations),
    ]

    return {
        "benchmark_id": "IDEA-LEDGER-BASELINE-V1",
        "implementation": "deterministic",
        "ai_calls": 0,
        "ai_cost_usd": 0.0,
        "seed_size": 100,
        "measurements": measurements,
        "overall_success_rate": sum(item["success_rate"] for item in measurements) / len(measurements),
        "notes": [
            "Synthetic/public data only.",
            "This is the non-AI benchmark for later AI-assisted and hybrid comparisons.",
        ],
    }


def main() -> None:
    report = run_baseline()
    output = Path(__file__).with_name("baseline-results.json")
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
