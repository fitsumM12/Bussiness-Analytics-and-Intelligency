# 6. Find the largest number of an array
"""
Created on Sat Mar  5 19:45:50 2022

@author: fitsum
"""
i=0
def largest(arr,n):
    max = arr[0]
    for i in range(1, n):
        if arr[i]>max:
            max = arr[i]
    return max

n = int(input("enter the size of the array:"))
arr = []
for i in range(0,n):
    element= int(input())
    arr.append(element)
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)