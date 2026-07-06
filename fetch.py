# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "massive>=2.8.0",
#     "numpy>=2.5.1",
#     "pandas>=3.0.3",
#     "python-dotenv>=1.2.2",
# ]
# ///

import time

import numpy as np
import pandas as pd

from massive import RESTClient

import os
from dotenv import load_dotenv

import logging

from urllib3.exceptions import MaxRetryError

logging.basicConfig(level=logging.INFO)

_ = load_dotenv()
MASSIVE_API_KEY = os.getenv("MASSIVE_API_KEY")

client = RESTClient(MASSIVE_API_KEY)

dates = pd.bdate_range("2026-06-01", "2026-06-06")

try:
    alldata = pd.read_csv("data.csv")
    alldata["date"] = pd.to_datetime(alldata["date"])
except FileNotFoundError:
    alldata = pd.DataFrame()

for date in dates:
    fmtdate = date.strftime("%Y-%m-%d")

    if (
        "date" in alldata.columns
        and date.normalize() in alldata["date"].dt.normalize().values
    ):
        logging.info(f"{fmtdate} already fetched. Skipping")
        continue

    logging.info(f"fetching {fmtdate}")
    while True:
        try:
            grouped = client.get_grouped_daily_aggs(
                fmtdate,
                adjusted=True,
                include_otc=False,
            )
        except MaxRetryError:
            logging.info(f"MaxRetryError for {fmtdate}. Retrying in 30 seconds")
            time.sleep(30)
        else:
            break

    df = pd.DataFrame(grouped)
    df["date"] = pd.to_datetime(df["timestamp"], unit="ms")

    logging.info(f"fetched {len(df)} rows for {fmtdate}")
    alldata = pd.concat([alldata, df], ignore_index=True)

alldata.drop_duplicates(subset=["ticker", "date"], inplace=True)
alldata.to_csv("data.csv", index=False)
