# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN"
                  ,"Test1","Test2","Test3","Test4"
                  ,"Final","Sonuc"]
print(notlar)
print(type(notlar))
print(notlar.head())
print(notlar.tail())
print(notlar["Final"])
print(notlar.iloc[2])
print(notlar[0:10])