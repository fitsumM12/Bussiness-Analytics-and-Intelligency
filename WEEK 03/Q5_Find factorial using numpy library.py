# 5). Find factorial using numpy library
"""
Created on Fri Mar 11 16:31:37 2022

@author: fitsum
"""
import numpy as np
num = int(input("enter the number:"))
res = np.math.factorial(num)
print(f"The factorial of {num} is {res}")