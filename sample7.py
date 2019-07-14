# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:30:34 2019

@author: Shrishti D Hore
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame(np.random.randn(1000,5))

#for top 5
print(df.head())

print("*************************************")

#for last 5
print(df.tail())

print("*************************************")

#to find count-no. of values present, mean, std dev, min,25%,50%,75% precentile value in the dataframe, max values
print (df.describe())

print("*************************************")

#
column = df[0]
print(column.head())

#to check which absolute values in column are greater than 3
print("**************************************")
print(column[np.abs(column)>3])

print("**************************************")
#print(df[np.abs(df)>3.any(1)])

#to set the range of values from -5 to +5
df[(np.abs(df)>3)] = np.sign(df)*5
print("***************************************")
print(df.describe())
























