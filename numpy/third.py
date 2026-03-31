import numpy as np
arr = np.array([1,2,3,4])
print(arr)
print(arr.dtype)
ar= np.array([True, False,True,False])
print(ar)
print(ar.dtype)
arra= np.array([2+3j,4+5j])
print(arra)
print(arra.dtype)
#converting datatypes in numpy
#numpy allows converting datatype using astype
array=np.array([])
newarr=array.astype(int)
print(newarr)
print(newarr.dtype)