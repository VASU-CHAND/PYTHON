# it is possible to use list constructor when creating a new list
#use list constructor to make a list
list1= list(('apple','banana','cherry'))
print(list1)
print(type(list1))
#access list items  
#indexing in list 
list8=['mango','apple', 'pineapple']
print(list8[1])
print(list8[-1])
#range of indexes
#u can specify range of indexes where to start and where to end the range for example
# return third 4th and 5th item of li
print(list8[0:2])
#check if mange is presnt in the list or not
list11=['mango','apple','cherry']
if 'ga' in list11:
    print('yes')
else:
    print('no')