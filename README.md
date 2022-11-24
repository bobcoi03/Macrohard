# Macrohard
Building trading models on daily largest gainers

Plan:

1. Collect Data

Collect prices (1-3 month 2-5 mins interval), volume, news, other data on stocks that has the highest one day gain. Put data in DB

2. Build Models
Genetic Algo - at each interval or ~ 30 minutes make decision to buy, sell or hold.

Optimize for profit, discourage number of trades

NN

Some other non machine learning models

3. Run backtests and simulations
Run models on benchmark dataset

4. Trade

Connect to IBKR API and trade away