import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
api_key='tB3urdgNfDsJMKZVPtA_'

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
forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

#column'll be shifted up, this way the label column for each row'll be adjusted price 10 days in the features
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'],axis=1)) #our features're everything without label column
y = np.array(df['label'])

#Takes your values and attempts to normalize them to be between -1 and 1.
# This is done for efficiency and accuracy, but is not required.﻿:
x = preprocessing.scale(x)
# x = x[:-forecast_out+1] #x[:29]
#It returns a new dataframe without the column label, then it is converted into a numpy array and then it is saved in the X value
# 1 refers to the axis,  axis=1  refers the 'column', axis=0  refers to the 'row'
y = np.array(df['label'])

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

# clf=LinearRegression() or the 2. algorithm:
clf =svm.SVR(kernel='poly')
# clf =svm.SVR()
clf.fit(x_train,y_train)
accuracy = clf.score(x_test,y_test)

print(accuracy)
