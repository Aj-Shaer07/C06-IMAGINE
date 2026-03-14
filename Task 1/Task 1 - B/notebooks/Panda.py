# Load CSV Dataset
import pandas as pd
df=pd.read_csv("data.csv")

# Inspect dataset
df.head()
df.info()
df.describe()

# Handle missing values
df.isnull().sum()
df.fillna(0)
df.dropna()

# Select specific columns
df["age"]
df[["age","salary"]]

# Descriptive Satistics
df.mean()
df.median()
df.std()
