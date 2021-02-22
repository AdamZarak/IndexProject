#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import datetime
import time
import requests
import io
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import quandl as ql
import yfinance as yf

#ql.ApiConfig.api_key = "vnbx82q4tvawzFjUi94H"
plt.style.use("dark_background")
ticker = "DJIA"
yf.download(ticker)

newtime = yf.download(ticker, start = "1981-02-20", end = "2021-02-19")

newtime['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel("Adjusted")
plt.title("DJIA Price Data")

plt.show()

newtime_daily = yf.download(ticker, start = "1981-02-20", end = "2021-02-19", period = "1d")
newtime_daily

#let's import numpy for the "shift" function.


djia_daily_returns = (newtime_daily['Adj Close'] / newtime_daily['Adj Close'].shift(1)) - 1
djia_daily_returns

#Let's transform the series to a data frame in order to facilitate the plotting
djia_daily_returns = djia_daily_returns.to_frame()
djia_daily_returns.columns = ['Simple daily Return']

djia_daily_returns['Simple daily Return'].plot()
plt.xlabel("Date")
plt.ylabel("Percent")
plt.title("DJIA Price Data")
plt.show()



#fig = plt.figure()
#ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
#msft_daily_returns.plot.hist(bins = 60)
#ax1.set_xlabel("Daily returns %")
#ax1.set_ylabel("Percent")
#ax1.set_title("Microsoft daily returns")
#ax1.text(-0.075,50,"Extreme Low returns")
#ax1.text(0.05,50,"Extreme High returns")
#plt.show()

avg_returns_daily = djia_daily_returns['Simple daily Return'].mean()
avg_returns_daily

Out[25]: 0.00098736878588533
    
avg_returns_4y = djia_daily_returns['Simple daily Return'].mean() * 250*4
avg_returns_4y 

Out[28]: 0.9873687858853301
    

tickers = ["INX", "DOWI", "NASX", "RUT"]

manystocks = yf.download(tickers, start = "2014-01-01", end = "2019-12-31", period = "1d")
manystocks_groupby = yf.download(tickers, start = "2014-01-01", end = "2019-12-31", period = "1d", group_by= "Ticker")
stocksclose = yf.download(tickers, start = "2014-01-01", end = "2019-12-31", period = "1d").Close
many_stocks_daily_returns = manystocks['Adj Close'].pct_change()
(stocksclose / stocksclose.iloc[0] * 100).plot(figsize = (20, 10))










# In[18]:


import datetime
import pandas_datareader.data as web
plt.style.use('dark_background')
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2020, 1, 27)
SP500 = web.DataReader(['sp500'], 'fred', start, end)

SP500['daily_return'] = (SP500['sp500']/ SP500['sp500'].shift(1)) -1

#Drop all Not a number values using drop method.
SP500.dropna(inplace = True)

SP500['daily_return'].plot(title='S&P 500 daily returns')

SP500['sp500'].plot(title='S&P 500 Price')


# In[6]:


from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
plt.style.use('dark_background')
ts = TimeSeries(key='H9WXH8EFNLZKJ1NJ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='AAPL',interval='60min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the AAPL stock (60 min)')
plt.show()


# In[ ]:




