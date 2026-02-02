#02/02/2026
import numpy as np

arr = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
print(arr)
print(arr.ndim)

arr.dtype

arr.ndim

arr.shape

#using  array functions:-
gg=np.zeros((2,5))
print(gg.shape)

#using arange:-
np.arange(15)#n-1

#Axis
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
x

#Axis
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
x.sum(axis=0)

#Axis
x.T

#using flat and printing the values 
x.flat
for a in x.flat:
  print(a)

#counting of elements:-
x.size

x.nbytes

x 

#.argmax() and .argmin()
print(x.argmax())
print(x.argmin())

#.argsort()
x.argsort()
/
