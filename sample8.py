# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:01:50 2019

@author: Shrishti D Hore
"""
import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

ds1 = randn(1000)
ds2 = randn(100)

plt.hist(ds1)
#plt.savefig('histogram.png')
#plt.show

plt.hist(ds2)
#plt.show()

plt.hist(ds1, normed=True,color ='green', bins=15,alpha = 0.5)
plt.hist(ds2,normed=True,bins=15,aplha=0.5)
#plt.show()

ds3 = randn(1000)
ds4 = randn(1000)

sns_plot = sns.joinplot(ds3,ds4)
sns_plot.savefig('hist1.png')
sns_plot2 = sns.jointplot(ds3,ds4,jind ='hex')
sns_plot2 = savefig('hist2.png')






