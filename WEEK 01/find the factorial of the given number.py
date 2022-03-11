# Q7.	Write a python program to find the factorial of the given number
"""
Created on Tue Feb 22 11:39:09 2022

@author: fitsum
"""

def factorial(num):
    res =1
    while num>0:
        res= res*(num)
        num =num -1
    return res

num = int(input("enter the number to find the factorial:"))
res = factorial(num)
print(f'The factorial will be: {res}')