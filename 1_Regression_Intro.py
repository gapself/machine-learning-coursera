import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

#SIMPLIFY DATA! - recreat the dataframe with meaningful features
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
#f.ex. there're relationships between features - high & low - tell us about volatility for the day
# open&close price - tell if the price goes up or down, if so, how much
#% volatility:
df['HL_PCT']=(df['Adj. High']-df['Adj. Close']) / df['Adj. Close'] * 100.0
df['HL_change']=(df['Adj. Close']-df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','HL_change','Adj. Volume']]

print(df.head())