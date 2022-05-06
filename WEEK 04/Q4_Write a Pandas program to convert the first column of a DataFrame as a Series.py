# Q4_Write a Pandas program to convert the first column of a DataFrame as a Series
"""
Created on Fri Mar 25 09:41:41 2022

@author: fitsum
"""

import pandas as pd
d = {'col1':[1,2,3,4,7,11],
     'col2':[0,9,8,7,4,33],
     'col3':[1,3,4,5,7,22]}
df = pd.DataFrame(data = d)
print("Original DataFrame:")
print(df)
s1 = df.iloc[:,0]  #iloc[row,colummn]
print("\n1st column as a Series:")
print(s1)
print(type(s1))