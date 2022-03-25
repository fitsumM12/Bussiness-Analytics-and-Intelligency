# Q8_Write a Pandas program to change the order of index of a given series.
"""
Created on Fri Mar 25 09:53:03 2022

@author: fitsum
"""

import pandas as pd
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)