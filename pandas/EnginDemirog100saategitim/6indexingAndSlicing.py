# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
notlar.columns = ["İsim","Soyisim","SSN"
                  ,"Test1","Test2","Test3","Test4"
                  ,"Final","Sonuc"]
print(notlar)
print(notlar.loc[:,"İsim"])
print(notlar.loc[:5,"İsim"])
print(notlar.loc[:5,"İsim":"Test4"])
print(notlar.loc[:5,["İsim","Soyisim","Final"]])
print(notlar.loc[:5,:"Test2"])
print(notlar.loc[::-1,:"İsim"])
