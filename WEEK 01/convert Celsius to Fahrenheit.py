# Q4.Write a python program to convert Celsius to Fahrenheit
"""
Created on Tue Feb 22 11:17:38 2022

@author: fitsum
"""

def celcius_to_farenheit(celcius):
    return celcius*9.0/5.0+32.0

celcius = int(input("Enter the temprature in celcius:"))
farenheit = int(celcius_to_farenheit(celcius))
print("The temprature in farenheit: ", farenheit)
