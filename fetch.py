# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "massive>=2.8.0",
#     "python-dotenv>=1.2.2",
# ]
# ///

from massive import RESTClient

import os
from dotenv import load_dotenv

_ = load_dotenv()
MASSIVE_API_KEY = os.getenv("MASSIVE_API_KEY")

client = RESTClient(MASSIVE_API_KEY)

grouped = client.get_grouped_daily_aggs(
    "2025-11-03",
    adjusted=True,
    include_otc=False,
)

print(grouped)
