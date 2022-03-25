# Q3_Write a Pandas program to convert a NumPy array to a Pandas series
"""
Created on Fri Mar 25 09:36:58 2022

@author: fitsum
"""

import numpy as np
import pandas as pd
np_array = np.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(np_array)

new_series = pd.Series(np_array)
print("Converted Pandas Series:")
print(new_series)