import pandas as pd 
df=pd.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\PYTHON\pandasbro\pokemon_data.csv" , index_col="Name")
pokemon=input("Enter the name of pokemon you want to search : ")
 
try:
    print(df.loc[pokemon])  
except KeyError:
    print("Pokemon not found in the dataset.")