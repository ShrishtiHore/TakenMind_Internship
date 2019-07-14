# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 12:20:28 2019

@author: Shrishti D Hore
"""
'''
import pandas as pd
import numpy as np
from pandas import DataFrame

df1 = DataFrame({'reference':['O','U','L','O','U'],'data':range(5)})
df2 = DataFrame({'profit':[10,20]},index=['O','U'])

print(pd.merge(df1,df2, left_on = 'reference', right_index=True))

df3 = DataFrame({'ref1':['A','A',,'O','O','A'],'ref2':['5,10,15,20,25],'ref3':[0,1,2,3,4,5]})

df4 = DataFrame(np.arrange(10).reshape(5,2), index=['A','A',,'O','O','A],[20,10,10,10,10],columns = ['col1','col2'])

print(pd.merge(df3,df4, left_on = ['ref1','ref2'], right_index=True))

'''
import pandas as pd
import numpy as np
from pandas import Series,DataFrame
from numpy import random

B1=np.arange(25).reshape(5,5)
A1= random.randn(25).reshape(5,5)

print(B1)
print(A1)

print(np.concatenate([A1,B1],axis = 1))
print(np.concatenate([A1,B1],axis = 0))

s1 = Series([100,200,300],index = ['A','B','C'])
s2 = Series([400,500],index = ['D','E'])

print(pd.concat([s1,s2]))
print(pd.concat([s1,s2],axis=1, sort=True))

df1= DataFrame(random.rand(4,3), columns=['A','B','C'])
df2= DataFrame(random.rand(4,3), columns=['B','D','A'])

print("pd.concat dataframes")
print(pd.concat([df1,df2]))
print("pd.concat dataframe - continuous index")
print(pd.concat([df1,df2],ignore_index=True))



