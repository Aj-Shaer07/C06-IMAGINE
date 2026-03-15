import re

import pandas as pd
dataset = pd.read_csv('C06-IMAGINE/Task_1/Task 1 - B/sleep.csv') #https://www.kaggle.com/datasets/mathurinache/sleep-dataset
#the missing vakues are represented by "?"
print(dataset.head())
print(dataset.info())
dataset.replace('?', pd.NA, inplace=True)
print(dataset.isnull().sum())
print("="*25)
for column in dataset.columns:
    dataset[column]=dataset[column].astype(float)
dataset=dataset.fillna(dataset.mean(), inplace=True)
#after replacing the missing values with the mean
print(dataset.isnull().sum())
print(dataset.info())
for column in dataset.columns:
    print(f"{column}:\nmean: {dataset[column].mean()}\nmedian: {dataset[column].median()}\nmode: {dataset[column].mode()[0]}\nstandard_deviation: {dataset[column].std()}\n")

