import bs4 as bs
import requests
import pandas as pd


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

#Reading stock data from Yahoo

import datetime
import pandas_datareader.data as web 


resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = bs.BeautifulSoup(resp.text, 'lxml')
table = soup.find('table', {'class': 'wikitable sortable'})
if len(table.contents) == 0:
  print("No table found")
else:
  print("Table extracted correctly!")
  print(type(table))

tickers = []
industries = []
for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        #fourth element is the sector
        industry = row.findAll('td')[4].text
        
        tickers.append(ticker)
        industries.append(industry)
print(tickers)

tickers = list(map(lambda s: s.strip(), tickers))
industries = list(map(lambda s: s.strip(), industries))

print(tickers)

tickerdf = pd.DataFrame(tickers,columns=['ticker'])
sectordf = pd.DataFrame(industries,columns=['industry'])

tickerandsector =pd.merge(tickerdf, sectordf, on = tickerdf.index, how = "outer")
tickerandsector = tickerandsector.drop('key_0', axis=1)
print(tickerandsector)

#Grab the data from Yahoo Finance for date range between 2010-2019
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2019, 12, 31)


sp500_df = web.DataReader("^GSPC", 'yahoo', start, end)

dates =[]
for x in range(len(sp500_df)):
    newdate = str(sp500_df.index[x])
    newdate = newdate[0:10]
    dates.append(newdate)

sp500_df.insert(0,'Date', dates)

sp500_df.to_csv("sp500_data.csv")

