# Q5.	Write a python program to check odd or even
"""
Created on Tue Feb 22 11:24:18 2022

@author: fitsum
"""
def check_odd_even(num):
    if num%2==0:
        print("{} is an even number".format(num) )
    else:
        print("{} is an odd number".format(num) )
        
num = int(input("Enter any number you like to check: "))
check_odd_even(num)


