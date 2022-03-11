# 8. To check whether 2 given strings are palindrome or not
"""
Created on Sat Mar  5 20:20:45 2022

@author: fitsum
"""
string01 = input("enter the first string:")
string02 = input("enter the second string:")
flag = True
n = len(string01)
for i in range(0,n):
    if(string01[i]!=string02[n-i-1]):
        flag =False
        break
    else:
        flag = True

if(flag):
    print("They are palindrom")
else:
    print("They are not palindrom")