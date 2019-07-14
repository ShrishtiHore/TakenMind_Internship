# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:44:35 2019

@author: Shrishti D Hore
"""

import pandas as pd

excelfile = pd.ExcelFile('animax.xlsx')
dframe = excelfile.parse('anime')
print(dframe)




