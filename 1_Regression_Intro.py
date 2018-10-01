import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')

#SIMPLIFY DATA! - recreat the dataframe with meaningful features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#f.ex. there're relationships between features - high & low - tell us about volatility for the day
# open&close price - tell if the price goes up or down, if so, how much
#% volatility:
df['HL_PCT']=(df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] * 100.0
df['HL_change']=(df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','HL_change','Adj. Volume']]

forecast_col = 'Adj. Close'
#na-non a number/non available
df.fillna(-99999, inplace=True)

#math.ceil'll takie anything - rounds everything up
#0.1 - using data that came 10 days ago to predict today
#0.001 - predict tomorrows price
forecast_out = int(math.ceil(0.1*len(df)))

#column'll be shifted up, this way the label column for each row'll be adjusted price 10 days in the features
df ['label'] = df[forecast_col].shift (-forecast_out)
df.dropna(inplace=True)
print(df.tail())
