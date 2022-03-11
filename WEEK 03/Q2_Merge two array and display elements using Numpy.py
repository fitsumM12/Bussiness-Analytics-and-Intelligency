# Q2, Merge two array and display elements using Numpy
"""
Created on Fri Mar 11 15:14:11 2022

@author: fitsum
"""
import numpy as np
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([5,6,7,8,9,2])
merged_array = np.append(arr1,arr2)
print(merged_array)