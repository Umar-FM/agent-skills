#!/usr/bin/env python3
"""Calculate creator-side YouTube metrics from a CSV or command-line values.

This is a diagnostic utility, not an estimator of YouTube's internal ranking.
"""
from __future__ import annotations
import argparse
import csv
from pathlib import Path


def safe_div(a: float, b: float) -> float:
    return a / b if b else 0.0


def calculate(impressions: float, ctr_percent: float, avd_minutes: float, revenue: float, variable_cost: float, production_hours: float) -> dict[str, float]:
    ctr = ctr_percent / 100.0
    return {
        'qualified_watch_minutes_per_impression': ctr * avd_minutes,
        'expected_watch_hours_per_1000_impressions': ctr * avd_minutes * 1000 / 60,
        'revenue_per_1000_impressions': safe_div(revenue * 1000, impressions),
        'contribution_margin': revenue - variable_cost,
        'revenue_per_production_hour': safe_div(revenue, production_hours),
        'contribution_per_production_hour': safe_div(revenue - variable_cost, production_hours),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--impressions', type=float, required=True)
    parser.add_argument('--ctr', type=float, required=True, help='CTR percentage, e.g. 6.2')
    parser.add_argument('--avd', type=float, required=True, help='Average view duration in minutes')
    parser.add_argument('--revenue', type=float, default=0)
    parser.add_argument('--variable-cost', type=float, default=0)
    parser.add_argument('--production-hours', type=float, default=0)
    args = parser.parse_args()
    for key, value in calculate(args.impressions, args.ctr, args.avd, args.revenue, args.variable_cost, args.production_hours).items():
        print(f'{key}: {value:.4f}')

if __name__ == '__main__':
    main()
