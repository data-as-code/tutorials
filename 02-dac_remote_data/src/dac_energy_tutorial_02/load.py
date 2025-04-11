import pandas as pd


def load():
    return pd.read_parquet(
        "az://public-sample-data/ml-lifecycle/"
        "code-interface/data-as-code/energy-v1.0.0.parquet",
        storage_options={"account_name": "edp0ds0lib0resources", "anon": True},
    )
