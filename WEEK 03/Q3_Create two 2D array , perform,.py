# Q3).  Create two 2D array , perform, +, -, *
"""
Created on Fri Mar 11 15:22:41 2022

@author: fitsum
"""
import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[3,2,1],[6,5,4],[9,8,7]])

#Adddition of two array
added_array = arr1+arr2
print("Addition of an array")
print(added_array)
print("\n")

#substractionof two array
substracted_array = arr2-arr1
print("Substraction of an array")
print(substracted_array)
print("\n")

#Dividing an array
divided_array = arr2/arr1
print("Dividing an array")
print(divided_array)
print("\n")

#Multiplication of an array
multiplied_array = np.dot(arr1,arr2)
print("Multiplications of an array")
print(multiplied_array)
print("\n")
