import pandas as pd 
calories ={
    "day1": 1700,
    "day2": 1780,
    "day3": 1900
}
s=pd.Series(calories)
# it will take labels as index
print(s)
s.loc['day3']+=500
print(s)
employye={
    "name":['john','michael','sarah'],
    "age":[25,30,22],
    "city":['new york','los angeles','chicago'],
    "salary":[50000,60000,55000]
}
d=pd.DataFrame(employye)
print(d)