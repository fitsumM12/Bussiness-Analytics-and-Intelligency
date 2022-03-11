#Q3. write a python program to calculate the area of the triangle
"""
Created on Tue Feb 22 11:08:51 2022

@author: fitsum
"""
def traingleArea(width, height):
    return 0.5*width*height
height = int(input("enter the height of the traingle:"))
width = int(input("enter the width of the traingle:"))
area = int(traingleArea(width, height))
print("Area : ",area)
