#  predict() function predict the labels of the data values on the basis of the trained model.
# Accepts only a single argument which is usually the data to be tested.
# returns the labels of the data passed as argument based upon the learned or trained data obtained from the model

import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

main = 'C:\\Users\joaopaulo\\Documents\\GitHub\\BIKE-RENTAL-COUNT'
file = 'day.csv'
day = os.path.join(main, file)
DF = pd.read_csv(day)
df = DF.copy()

#Split X, y, training and testing datasets.
columns = ['season', 'yr', 'mnth', 'weathersit', 'holiday']
df = pd.get_dummies(df, columns=columns)
#X = df.drop(['cnt', 'instant', 'dteday'], axis=1)
# X = df.drop(['cnt', 'instant'], axis=1)
X = df.drop(['cnt', 'dteday'], axis=1)
y = df['cnt']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=0)

#Build Decision Tree model
DT_model = DecisionTreeRegressor(max_depth=5).fit(X_train, y_train)
DT_predict = DT_model.predict(X_test) #Predictions on testing data
print(DT_predict)
#DT_predict.to_csv(os.path.join(main, 'DT_predict().csv'), index=False, encoding='utf-8')
# np.savetxt(os.path.join(main, 'DT_predict().csv'), DT_predict, delimiter=',')