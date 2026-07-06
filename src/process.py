# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "numpy>=2.5.1",
#     "pandas>=3.0.3",
# ]
# ///

from pathlib import Path
import pandas as pd

CSV_PATH = Path(__file__).parents[1] / "data" / "data.csv"

df = pd.read_csv(CSV_PATH)
print(df.head())
