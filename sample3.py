# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 18:52:59 2019

@author: Shrishti D Hore
"""

import pandas as pd
from pandas import DataFrame
from pandas import read_html
from lxml import html

url = "https://countrycode.org/"
dflist = pd.io.html.read_html(url)
dframe = dflist[0]
print(dframe)