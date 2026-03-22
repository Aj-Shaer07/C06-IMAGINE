#LINEAR REGRESSION USING SKLEARN

import math
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt

train_data = pd.read_csv('C06-IMAGINE/Task 2/a/train.csv')
print(train_data.head())
fig = px.scatter(train_data, x=train_data.iloc[:,0].values, y=train_data.iloc[:,1].values, title='Scatter Plot of train.csv Data')
fig.show()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x=train_data.iloc[:,0].values
X_train=np.array(x)
X_train=X_train.reshape(-1,1)
X=scaler.fit_transform(X_train)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

model = LinearRegression()
y=train_data.iloc[:,1].values
model.fit(X,y)

test_data = pd.read_csv('C06-IMAGINE/Task 2/a/test.csv')
x_test=test_data.iloc[:,0].values
y_test=test_data.iloc[:,1].values

x_test=test_data.iloc[:,0].values
X=np.array(x_test)
X=X.reshape(-1,1)
X_test= scaler.transform(X)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:",mse)
print("Mean Absolute Error:",mae)
print("Root Mean Squared error:",rmse)
print("R-Squared:",r2)