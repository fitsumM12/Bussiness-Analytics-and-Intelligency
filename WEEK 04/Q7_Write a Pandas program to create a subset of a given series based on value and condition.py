# Q7_Write a Pandas program to create a subset of a given series based on value and condition
"""
Created on Fri Mar 25 09:49:58 2022

@author: fitsum
"""
import pandas as pd
s = pd.Series([0, 1,2,3,4,5,6,7,8,9,10])
print("Original Data Series:")
print(s)
print("\nSubset of the above Data Series:")
n = 6
new_s = s[s < n]
print(new_s)