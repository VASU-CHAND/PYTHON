import pandas as hihi
print(hihi.__version__)
df=hihi.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\PYTHON\pandasbro\pokemon_data.csv" , index_col="Name")
#selection by coloumn
#print(df['Name']) # to print only name coloumn
#print(df['Name'].to_string()) # to print complete dtata
#print(df["Height"])
#print(df[["Name","Type 1","HP"]]) # to print multiple coloumns


#selection by row
#print(df.loc[0]) # to print first row
print(df.loc["Pikachu"]) # to print row 
#with name pikachu after changing index coloumn to name
print(df.loc["Charizard":"Blastoise", ["Height","Weight"]]) # to print height and weight of charizard
print(df.iloc[0:11:2 , 0:3]) # to print first row