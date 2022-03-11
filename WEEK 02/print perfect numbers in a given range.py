# 7. To print perfect numbers in a given range
"""
Created on Sat Mar  5 20:16:03 2022

@author: fitsum
"""

Number = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, Number):
    if(Number % i == 0):
        Sum = Sum + i
if (Sum == Number):
    print(" %d is a Perfect Number" %Number)
else:
    print(" %d is not a Perfect Number" %Number)