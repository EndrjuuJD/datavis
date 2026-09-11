"""Small helpers for the DVBI sales dataset.

This is *your own module*: a plain .py file with functions you can import from
another script with `import saleslib`. Keeping reusable code in a module (instead
of copy-pasting it into every script) is the first step toward real projects.
"""
from pathlib import Path

import pandas as pd

# Path to the data folder, relative to THIS file — so imports work no matter
# what directory you run from.
DATA = Path(__file__).parent / "data"


def load_sales() -> pd.DataFrame:
    """Load sales.csv with the `date` column parsed as real datetimes."""
    return pd.read_csv(DATA / "sales.csv", parse_dates=["date"])


def load_regions() -> pd.DataFrame:
    """Load the region lookup table (manager, annual target in mDKK)."""
    return pd.read_csv(DATA / "regions.csv")


def kdkk_to_mdkk(value: float) -> float:
    """Convert thousand-DKK (the dataset's unit) to million-DKK."""
    return value / 1000
