# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb_1000.csv")
print(films.columns)

films = films.drop("content_rating",axis=1)
films = films.drop("actors_list",axis=1)

films = films.drop(2,axis=0)

rowsToDrop = [0,1,3,4,6,8,9,10]
films = films.drop(rowsToDrop,axis=0)
print(films.mean(axis=0))