# Import required packages
import pandas_datareader.data as web 
import datetime  
import pandas as pd
import talib
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
%matplotlib inline

print(sp500_df.head())


print(sp500_df.describe())

print("Summarized Data")
print(sp500_df.describe(include=['O']))

print(sp500_df.dtypes)

print(sp500_df.isna().sum())


tickers = ['MSFT','GOOGL','AMZN', 'AMD', '^GSPC' ]
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 12, 31)
data = pd.DataFrame()

for ticker in tickers:
    df1 = web.DataReader(ticker, 'yahoo', start, end)
    data[ticker] = df1['Adj Close']
    data.rename(columns = {'^GSPC':'S&P500'}, inplace = True)


    
print(data.head())

#Correlation
correlation = data.corr()
mask = np.zeros_like(correlation, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
ig, ax = plt.subplots(figsize=(8, 8))
sns.heatmap(correlation, mask=mask, square=True, linewidths=.5, annot=True, 
            cbar_kws={"shrink": .5})
ax.set_title('Stocks Correlation with S&P 500')

#Daily Return
data_dup = data.copy()


data_dup = (data_dup - data_dup.iloc[0, :])/data_dup.iloc[0, :]*100

data_dup.plot(legend=True, figsize=(14, 8), linewidth=1)
plt.axhline(y=0, linestyle='dashed', color='black', linewidth=1)
plt.xlabel('Year')
plt.ylabel('Return %')
plt.title('Stocks and S&P 500 Returns 2010 to 2019')

#Calculate the daily close percentage of S&P 500
daily_close = sp500_df['Adj Close']

sp500_df['Return'] = 100 * (sp500_df['Adj Close'].pct_change())

daily_pct_chg = round(sp500_df['Return'],2)
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(sp500_df['Return'], color='b')
plt.xlabel('Year')
plt.ylabel('Daily Return %')
plt.title('Simple Returns - S&P 500 Index Daily Returns over the years')
plt.show()

#Create 14 day close feature
sp500_df['14d_future_close'] = sp500_df['Adj Close'].shift(-14)
sp500_df['14d_future_close_pct'] = sp500_df['14d_future_close'].pct_change(14)
sp500_df['ma14'] = talib.SMA(sp500_df['Adj Close'].values, timeperiod=14)
sp500_df['ma200'] = talib.SMA(sp500_df['Adj Close'].values, timeperiod=200)
sp500_df['rsi14'] = talib.RSI(sp500_df['Adj Close'].values, timeperiod=14)
sp500_df['rsi200'] = talib.RSI(sp500_df['Adj Close'].values, timeperiod=200)
sp500_df['ema14'] = talib.EMA(sp500_df['Adj Close'].values, timeperiod=14)
sp500_df['ema200'] = talib.EMA(sp500_df['Adj Close'].values, timeperiod=200)
sp500_df = sp500_df.drop(['High','Low','Open','Close','Volume'],axis=1)
corr = sp500_df.corr()
%matplotlib inline
fig, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corr, annot=True)









