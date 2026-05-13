import numpy as np
arr=np.array([[1,2,3,4,5,],[6,7,8,9,10]])
print(np.sum(arr , axis=0)) #axis =0 to all coloumns
print(np.sum(arr,axis=1)) #axis =1 to all rows
ages=np.array([[21,17,18,19,20,65,80],[45,66,8,99,71,44,12]])
teen=ages[ages<18]
print(teen)
adults=ages[(ages>18)&(ages<65)]
print(adults)
#to prserve orignal shape
adult=np.where(ages>=18,ages,0)
print(adult)