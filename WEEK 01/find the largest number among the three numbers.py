# Q6. Write a python program to find the largest number among the three numbers# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 11:32:34 2022

@author: fitsum
"""

def find_largest(num1, num2, num3):
    if num1>num2:
        if num1>num3:
            return num1
        else:
            return num3
    else:
        if num2>num3:
            return num2
        else:
            return num3

num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))

res = find_largest(num1, num2, num3)
print(f'The largest of three numbers is {res}')