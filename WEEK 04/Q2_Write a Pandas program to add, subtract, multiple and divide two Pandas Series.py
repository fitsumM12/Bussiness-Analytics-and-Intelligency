# Q2_Write a Pandas program to add, subtract, multiple and 
# divide two Pandas Series.
"""
Created on Fri Mar 25 09:31:45 2022

@author: fitsum
"""

import pandas as pd
ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,9])

ds = ds1 + ds2
print("Add two Series: ")
print(ds)

ds = ds1 - ds2
print("Substract two Series: ")
print(ds)

ds = ds1 * ds2
print("Multiply two Series: ")
print(ds)

ds = ds1 / ds2
print("Divide two Series: ")
print(ds)
