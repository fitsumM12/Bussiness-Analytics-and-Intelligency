# Q1, Create 1-D array having 10 elements, 
# find the dimensions of the array and 
# sort the array elements in ascending order using Numpy
"""
Created on Fri Mar 11 15:03:29 2022

@author: fitsum
"""
import numpy as np
#Creating 1-D array having 10 element
arr = np.array([1,2,3,4,5,6,7,8,9,0])
#Find the dimension of the array
print(arr.ndim)
# sort the array elements in ascending order using Numpy
arr = np.sort(arr)
print(arr)
