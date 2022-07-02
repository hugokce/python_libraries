# -*- coding: utf-8 -*-

import pandas as pd

url = "http://bit.ly/uforeports"

data = pd.read_csv(url)
print(data[["City",
            "Colors Reported",
            "Shape Reported",
            "State",
            "Time"]].head())
print(data.columns)
print(data.isnull().head(100))
print(data.notnull().head(100))
print(data.isnull().sum())

print(data.shape)
#data = data.dropna(how = "all")
#data = data.dropna(
#        subset=['City','Colors Reported'],how="any")

data['Shape Reported'].fillna(value='Belirsiz',inplace=True)
print(data['Shape Reported'].value_counts(dropna=False))

print(data.shape)











