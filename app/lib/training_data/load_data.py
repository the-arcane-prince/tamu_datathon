import polars as pl
import os

def load_data(color: str) -> pl.DataFrame:
    assert color in ["green", "yellow", "blue", "purple"]
    return pl.read_json(f"{os.getenv('BASEDIR')}/data_{color}.json")

def load_all_data() -> pl.DataFrame:
    return pl.concat([load_data(color) for color in ["green", "yellow", "blue", "purple"]])