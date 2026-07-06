# stockdata

Scripts to fetch stock data from [Massive](https://www.massive.com).

[`fetch.py`](src/fetch.py): Fetches stock data from Massive with start and end dates.

```bash
uv run src/fetch.py
```

[`process.py`](src/process.py): Adds columns for previous OHLC and gap.

```bash
uv run src/process.py
```
