# 5. Convert given decimal to binary
"""
Created on Sat Mar  5 19:36:28 2022

@author: fitsum
"""
def DecimalToBinary(num):
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')

dec_val = int(input("enter the decimal number:"))
res = DecimalToBinary(dec_val)
print(f"The binary result : {res} ")