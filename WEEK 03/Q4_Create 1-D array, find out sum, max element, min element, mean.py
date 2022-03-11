# Q4. Create 1-D array, find out sum, max element, min element, mean
"""
Created on Fri Mar 11 15:49:19 2022

@author: fitsum
"""
import numpy as np
arr = np.array([1,2,3,4,55,6])

#Find ou the sum of each element
sum = 0 
i = 0
for i in range(0,len(arr)):
    sum = sum + arr[i]
print(f"\n The sum of each element: {sum}")

#Max element
MAX = arr[0]
for i in range(0, len(arr)):
    if MAX<arr[i]:
        MAX = arr[i]
    else:
        continue
print(f"\nThe maximum element is {MAX}")

#MIN element
MIN = arr[0]
for i in range(0, len(arr)):
    if MIN>arr[i]:
        MIN = arr[i]
    else:
        continue
print(f"\nThe minimum element is {MAX}")

#MEAN of elemen
res=0
for i in range(0, len(arr)):
    res = res+arr[i]
mean = res/len(arr)
print(f"\nThe mean of element is {mean}")