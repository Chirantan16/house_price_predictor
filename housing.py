import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import  mean_squared_error
from math import sqrt
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv('train.csv')
df1 = pd.read_csv('test.csv')

X_train = np.array(df.iloc[:, 0:4])
y_train = np.array(df.iloc[:, 4:])

X_test = np.array(df.iloc[:, 0:4])
y_test = np.array(df.iloc[:, 4:])

model = DecisionTreeRegressor()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)
print("Root Mean squared error is: ", sqrt(mean_squared_error(y_test, y_predicted)))


pickle.dump(model, open('housing.pkl', 'wb'))
