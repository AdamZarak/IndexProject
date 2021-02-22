#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import yfinance as yf

ticker = "MSFT"
yf.download(ticker)

newtime = yf.download(ticker, start = "2014-01-01", end = "2018-12-31")

import matplotlib.pyplot as plt
newtime['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("Miscrosoft Price data")
plt.style.use('default')
plt.show()

newtime_daily = yf.download(ticker, start = "2014-01-01", end = "2018-12-31", period = "1d")
newtime_daily

#let's import numpy for the "shift" function.

import numpy as np
msft_daily_returns = (newtime_daily['Adj Close'] / newtime_daily['Adj Close'].shift(1)) - 1
msft_daily_returns

#Let's transform the series to a data frame in order to facilitate the plotting
msft_daily_returns = msft_daily_returns.to_frame()
msft_daily_returns.columns = ['Simple daily Return']

msft_daily_returns['Simple daily Return'].plot()
plt.xlabel("Date")
plt.ylabel("Percent")
plt.title("Miscrosoft Price data")
plt.show()

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
msft_daily_returns.plot.hist(bins = 60)
ax1.set_xlabel("Daily returns %")
ax1.set_ylabel("Percent")
ax1.set_title("Microsoft daily returns")
ax1.text(-0.075,50,"Extreme Low returns")
ax1.text(0.05,50,"Extreme High returns")
plt.show()

avg_returns_daily = msft_daily_returns['Simple daily Return'].mean()
avg_returns_daily

Out[25]: 0.00098736878588533
    
avg_returns_4y = msft_daily_returns['Simple daily Return'].mean() * 250*4
avg_returns_4y 

Out[28]: 0.9873687858853301
    
import pandas as pd
import yfinance as yf
tickers = ["F", "MSFT", "FB", "NFLX", "GOOG", "BLDP", "TSLA"]

manystocks = yf.download(tickers, start = "2014-01-01", end = "2018-12-31", period = "1d")
manystocks_groupby = yf.download(tickers, start = "2014-01-01", end = "2018-12-31", period = "1d", group_by= "Ticker")
stocksclose = yf.download(tickers, start = "2014-01-01", end = "2018-12-31", period = "1d").Close
many_stocks_daily_returns = manystocks['Adj Close'].pct_change()
(stocksclose / stocksclose.iloc[0] * 100).plot(figsize = (20, 10))

                                               


# In[ ]:




