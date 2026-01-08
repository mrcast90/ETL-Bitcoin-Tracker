# ETL Bitcoin Tracker

## Description
A Python-based ETL (Extract, Transform, Load) pipeline that monitors Bitcoin prices in real-time. The script connects to the CoinGecko API, processes the raw data, and exports it into a structured CSV file.

## Tech Stack
* **Python 3.12**
* **Pandas:** Data manipulation and structuring.
* **Requests:** REST API consumption.
* **CSV:** Data storage.

## How it works
1. **Extract:** Fetches current BTC price in BRL.
2. **Transform:** Adds timestamps and formats the data using Pandas.
3. **Load:** Saves the historical data into `relatorio_cripto.csv`.
