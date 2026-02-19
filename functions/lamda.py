square = lambda x: x*x
print(square(5))
add = lambda a, b : a+b
print(add(3, 9))
def factorial(n) :
    if n==0:
        return 1
    return n*factorial(n-1)
 

factorial(4)