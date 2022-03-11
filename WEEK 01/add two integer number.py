#Q1.	Write a python program to add two integer number
"""
Created on Sun Feb 20 21:10:29 2022

@author: fitsum
"""

def add(num1, num2):
    return num1 + num2
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
sum = add(num1,num2)
print("The sum of two numbers: ",sum)