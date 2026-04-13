import pandas as pd
data={
    "name":['a' , 'b' , 'c'],
    "age":[20 , 21 , 22]
}
df= pd.DataFrame(data)
print(df)
print(df["name"])
df["marks"]=[12 , 12 ,13]
print(df)
df.drop("marks",axis=1 , inplace=True)
print(df)
print(df.tail(1))
print(df.info())
print(df.describe())
filtered_data = df[df["age"]>20] 
# the first df means its pandas to 
# filter the dataframe we want 
#secomd dataframe specify name of
# the column dataframe 
print(filtered_data)
