# 3. Add two numbers
"""
Created on Sat Mar  5 19:08:24 2022

@author: fitsum
"""
def add(num1,num2):
    return num1+num2
num1 = int(input("enter the first num:"))
num2 = int(input("enter the second num:"))
res = add(num1,num2)
print(f"The sum of {num1} and {num2} is {res}")