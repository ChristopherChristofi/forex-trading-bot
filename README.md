# Forex Trading Bot

Adaptation of forex trading bot and backstream testing methodologies

## Use Instructions:

1. ***Authentication:***
Build .env file and provide OANDA crendentials for account

2. ***Install:***
```sh
pip install -r requirements
```

3. ***Data Extraction:***

Connect to API:
```sh
python oanda_api.py
```
Build datasets (moving averages):
```sh
python ma_sim.py
```