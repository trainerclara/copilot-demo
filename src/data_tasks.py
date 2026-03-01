
"""Data tasks for the Copilot demo.

Use Copilot to complete the functions below. You have a sample CSV at data/sales.csv
with columns: date, product, region, units, price.
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional

import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[2] / 'data' / 'sales.csv'


def main() -> None:
    print("Reading:", DATA_PATH)
    df = pd.read_csv(DATA_PATH, parse_dates=['date'])
    print(df.head())

    # TODO: Ask Copilot to write summarize_sales(df) that returns a DataFrame with
    # total revenue per region and month, sorted by revenue desc.
    # Then, pretty-print the result and optionally plot a bar chart.

    # Example prompt for Chat:
    # "Write a function summarize_sales(df: pd.DataFrame) -> pd.DataFrame that computes
    # revenue = units * price, groups by region and month (YYYY-MM), and returns the
    # top 10 rows sorted by revenue desc. Include a doctring and type hints."


if __name__ == '__main__':
    main()
