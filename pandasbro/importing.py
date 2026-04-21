import pandas as hihi
print(hihi.__version__)
df=hihi.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\PYTHON\pandasbro\pokemon_data.csv" , index_col="Name")
#selection by coloumn
#print(df['Name']) # to print only name coloumn
#rint(df['Name'].to_string()) # to print complete dtata
#print(df["Height"])


#selection by row
#print(df.loc[0]) # to print first row
print(df.loc["Pikachu"]) # to print row with name bulbasaur
