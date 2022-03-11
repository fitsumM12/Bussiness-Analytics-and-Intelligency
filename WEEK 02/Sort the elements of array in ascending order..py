# 10. Sort the elements of array in ascending order.
"""
Created on Sun Mar  6 11:16:30 2022

@author: fitsum
"""
def swap(num1, num2):
    temp = num1
    num1 = num2 
    num2 = temp
def sorting(arr, n):
    for i in range(1,n):
        for j in range(0,i):
            if arr[i]<arr[j]:
                temp = arr[i]
                arr[i] = arr[j] 
                arr[j] = temp
    for i in range(0,n):
        print(arr[i])

list01 = []
n = int(input("enter the size of the array:"))
for i in range(0,n):
    element = int(input())
    list01.append(element)
sorting(list01,n)