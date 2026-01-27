x= float(input("enter the first side \n"))
y= float(input("enter the second side \n"))
z= float(input("enter the third side \n"))
s= (x+y+z)/2
area= pow((s*(s-x)*(s-y)*(s-z)),0.5)
print("the area of triangle is " , area)