import pandas as ps

data={
    "name":['john','michael','sarah'],
    "age":[25,30,22],
    "city":['new york','los angeles','chicago'],
    "salary":[50000,60000,55000]
}
newframe=ps.DataFrame(data, index=['emp1','emp2','emp3'])
print(newframe)
print(newframe.loc['emp1'])
newframe["job"]=['engineer','manager','analyst']
print(newframe)
#add a new row
new_row = ps.DataFrame([{'name': 'david', 'age': 28, 'city': 'san francisco', 'salary': 65000, 'job': 'designer'}])
print(new_row)
newframe=ps.concat([newframe , new_row], ignore_index=True)
print(newframe)