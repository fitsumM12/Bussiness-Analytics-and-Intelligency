#Q5.Write a Pandas program to convert a given Series to an array.
"""
Created on Fri Mar 25 09:45:48 2022

@author: fitsum
"""

import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', 'Fitsum','mesfin', '300.12', '400'])
print("Original Data Series:")
print(s1)
print("Series to an array")
a = np.array(s1.values.tolist())
print (a)