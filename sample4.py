# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 22:10:56 2019

@author: Shrishti D Hore
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe1 = DataFrame({'reference':['ola','uber','lyft','gojek','grab'], 'revenue':[1,2,3,4,5]})
dframe2 = DataFrame({'reference':['ola','uber','uber','ola'], 'revenue':[1,2,3,4]})

#print(dframe1)
#print(dframe2)

df3 = pd.merge(dframe1,dframe2, on = 'reference')
#print(df3)

df4 = pd.merge(dframe1,dframe2, on ="reference", how="left")
#print(df4)

df5 = pd.merge(dframe1,dframe2,on="reference",how="outer")
#print(df5)

df6 = pd.merge(dframe1,dframe2, on ="reference", how="right")
#print(df6)

df7 = DataFrame({'reference':['ola','ola','lyft','lyft','uber','uber','ola'],"revenue":[1,2,3,4,5,6,7]})
#print(df7)

df8 = DataFrame({'reference':['uber','uber','lyft','ola','ola'],"revenue":[1,2,3,4,5]})
#print(df8)

#print(pd.merge(df7,df8))

df9 = DataFrame({'reference':['ola','ola','lyft','lyft'],'revenue':['one','one','one','three'],'profit':[4,5,6,7]})
#print(df9)

df10 = DataFrame({'reference':['ola','ola','lyft'],'revenue':['one','two','three'],'profit':[1,2,3]})
#print(df10)

print(pd.merge(df9,df10,on = ['reference','revenue'],how='outer'))
