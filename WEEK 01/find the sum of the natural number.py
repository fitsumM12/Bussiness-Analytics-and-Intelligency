#Q8.	Write a python program to find the sum of the natural number
"""
Created on Tue Feb 22 11:50:20 2022

@author: fitsum
"""

def sum(num):
    res = 0
    rem = 1
    while rem>0:
        rem = int(num%10)
        num = int(num/10)
        res = res+rem
    return res
num = int(input("enter the natural number to be added:"))
res = sum(int(num))
print(f'The sum of the number is {res}')