# 2. Swap two numbers
"""
Created on Sat Mar  5 18:52:09 2022

@author: fitsum
"""
num1, num2 =0,0
def swap(num1, num2):
    tmp = num1
    num1 = num2 
    num2 = tmp
    print(f"num1 = {num1}, num2 = {num2}")
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
print("befor swapping\n")
print(f"num1 = {num1}, num2 = {num2}")
print("\n after swapping\n")
swap(num1,num2)