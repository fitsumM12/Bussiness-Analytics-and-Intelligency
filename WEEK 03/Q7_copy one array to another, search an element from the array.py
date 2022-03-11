# 7). copy one array to another, search an element from the array
"""
Created on Fri Mar 11 16:38:03 2022

@author: fitsum
"""

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10]);
#copy an array
arr_copy = np.copy(arr)


num = int(input("search a number from 1-10:"))
for i in range(0,len(arr)):
    if num == arr[i]:
        print(f"The number {num} is found at {i} index")
        break
    else:
        continue
