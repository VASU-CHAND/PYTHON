def func(a,b,c):
    return a + b +c
numbers = [1, 2, 3]
result = func(*numbers)
print(result)
# unpacking arguments 
# * and ** operators can be used
#  calling a function to unpack a list or dictionary to soerate
#  arguments if you have value stored in a list 
# you can use * to unpack them into individual 
#arguments 