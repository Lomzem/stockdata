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

df = df.sort_values(["ticker", "date"])

df["popen"] = df.groupby("ticker")["open"].shift(1)
df["phigh"] = df.groupby("ticker")["high"].shift(1)
df["plow"] = df.groupby("ticker")["low"].shift(1)
df["pclose"] = df.groupby("ticker")["close"].shift(1)

df["gap"] = df["open"] / df["pclose"] - 1

df.to_csv(CSV_PATH, index=False)
