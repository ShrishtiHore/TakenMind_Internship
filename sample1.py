import numpy as np
import pandas as pd
from pandas import Series, DataFrame

dframe = pd.read_csv('demo.csv')
print(dframe)

dframe = pd.read_csv('demo.csv',header=None)
print(dframe)

dframe2 = pd.read_table('demo.csv', sep=',',header=None)
print(dframe2)

dframe3 = pd.read_csv('demo.csv',nrows = 3, header=None)
print(dframe3)

#values to csv
dframe2.to_csv('outputCSV.csv', sep='!')

#select specific columns 
dframe.to_csv('dataoutput.csv', columns=[0,1])
