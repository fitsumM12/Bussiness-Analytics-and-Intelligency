#9. To find out sum of 1/1!+2/2!+3/3!+....n/n!
"""
Created on Sat Mar  5 20:31:44 2022

@author: fitsum
"""

def fact(n): 
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)    
def add(n):
    sum =0
    for i in range(0,n+1):
        sum = sum + (i/fact(i))
    return sum
n = int(input("enter the value of n:"))
res = add(n)
print(f"Result: {res}")
