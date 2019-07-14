# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:27:26 2019

@author: Shrishti D Hore
"""

import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset('flights')
df2=df.pivot('year','month','passengers')
print(df2)

#sns.heatmap(df2).getfigure().savefig('heatmap1.png')
#sns.heatmap(df2,annot=True,fmt='d').get_figure().savefig('heatmap2.png')

sns.heatmap(df2, center=df2.loc[1955,'January']).get_figure().savefig('heatmap3.png')



