# Q6_Write a Pandas program to sort a given Series.
"""
Created on Fri Mar 25 09:48:10 2022

@author: fitsum
"""

import pandas as pd
s = pd.Series(['100', '200', 'Fitsum', '300.12', '400'])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)