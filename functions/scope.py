# global scope -- avariable created in the main body of the python code is a gloabal variable and 
# belongs to the global scope 
# a gloabal varibale can be accesed in whole code
# for ex - a variable create doutside of afunction is gloabal
#  and can be used by anyone 
x=20
def funcname():
    print(x)

funcname()
print(x)
