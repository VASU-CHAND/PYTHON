print("for the quadratic equation ax^2+bx+c=0 ")
a= int(input("enter the value of a\n"))
b= int(input("enter the value of b\n"))
c= int(input("enter the value of c\n")) 
d= b*b-4*a*c
if (d>=0):
    x1= (-b+pow(d,0.5))/(2*a)
    x2= (-b-pow(d,0.5))/(2*a)
    print(x1)
    print(x2)
else:
 print("roots are imaginary")