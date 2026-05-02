#aggregate functions = reduce the set of
#  values  into a single summary 
# value used to summarize and analyize data
#often used witth the groupby() function
import pandas as pd
df=pd.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\PYTHON\pandasbro\pokemon_data.csv" )
print(df)
print(df.mean(numeric_only=True)) 
# to print mean of all numeric coloumns
print(df["Height"].mean()) # to print mean of height coloumn