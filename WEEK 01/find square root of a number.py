#Q2.Write a python program to find square root of a number
"""
Created on Sun Feb 20 21:17:51 2022

@author: fitsum
"""
import math 
def findSQRT(num):
    return math.sqrt(num)

num = int(input("enter the number:"))
res = findSQRT(num)
print("Result: ",res)