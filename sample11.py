# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:47:54 2019

@author: Shrishti D Hore
"""

import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('flights')
df2 = df.pivot('year','month','passengers')
print(df2)

#sns.clustermap(df2).savefig('cluster1.png')

#sns.clustermap(df2,col_cluster=False).savefig('cl2.png')