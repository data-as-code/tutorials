from pathlib import Path

import pandas as pd


def load():
    return pd.read_parquet(Path(__file__).parent / "energy.parquet")
