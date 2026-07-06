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
df["date"] = pd.to_datetime(df["date"])

df = df.query("gap > 0.3 and high > 1")

df = df.sort_values(["date", "gap"], ascending=False)
df = df.reset_index(drop=True)

df = df[["date", "ticker", "gap", "opchange"]]
df["date"] = df["date"].dt.strftime("%Y-%m-%d")

print(df)
