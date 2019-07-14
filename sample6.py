# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:18:53 2019

@author: Shrishti D Hore
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

df = DataFrame({'country':['Afghanistan','Albania','Algeria'],'code':['93','355','213']})

print(df)

GDP_map = {'Afghanistan':'20', 'Albania':'12.8', 'Algeria':'215'}

print("*******************************************")
print(GDP_map)

print("*******************************************")
df['GDP'] = df['country'].map(GDP_map)

print(df)
