# 4.identity a number is prime or not
"""
Created on Sat Mar  5 19:13:07 2022

@author: fitsum
"""
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True
num = int(input("enter the number:"))
if(isprime(num)):
    print("the number is prime")
else:
    print("The number is not prime")