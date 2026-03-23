import math
import numpy as np
import pandas as pd
import plotly.express as px
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv('C06-IMAGINE/Task 2/c/wine_dataset.csv')

X = df[['alcohol','malic_acid','ash']].values
y = df['target'].values

a=df.columns
print(a)

print(df.head())
fig = px.scatter_3d(df,x='alcohol',y='malic_acid',z='ash',color='target',title='Scatter Plot of wine_dataset.csv Data')
fig.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:",mse)
print("Mean Absolute Error:",mae)
print("Root Mean Squared error:",rmse)
print("R-Squared:",r2)


#to find if a column is related to another
#gives correlation plot
corr = df.corr()
plt.figure(figsize=(20,20))
sns.heatmap(corr, cmap='mako_r',annot=True)                     
plt.show()
