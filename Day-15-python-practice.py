12/feb/2026

import pandas as pd

calories = pd.array([[6,7,8],[3,2,1]])
#myvar = pd.DataFrame(calories, columns=[1, 2,3,4],index=[1,"hi"])

#print(myvar)

calories.reshape((2,1))

#Statistical operations on 1D array.
""" 
max()
min()
sum()
mean()
np.median(variable)
prod()
var()
std()
"""
import numpy as np
x = np.array([[2,3,4],[7,5,8]])
print("1",x.max())
print("2",x.min())
print("3",x.sum())
print("4",x.mean())
print("5",np.median(x))
print("6",x.prod())
print("7",x.var())
print("8",x.std())
