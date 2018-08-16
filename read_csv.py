# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:23:22 2018

@author: L0k35h_p4nd3y
"""

import pandas as pd
df = pd.read_csv('G:/MCA hons/5 sem/python/auto.csv')
print(df)
print(df.dtypes)
print(df.describe())
#print(df.describe(include -"all"))
print(df.head(5))
print(df["symboling"])
print(df.info())
#df("price") = df["price"].astype("int")
print(df.info())
df["length"] = df["length"] / df["length"].max()