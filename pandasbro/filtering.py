import pandas as pd

df=pd.read_csv(r"C:\Users\vaibh\OneDrive\Desktop\PYTHON\pandasbro\pokemon_data.csv" , index_col="Name")
#filtering + keeping the rows that match a condition
tall_pokemon=df[df["Height"]>=2]
print(tall_pokemon)
heavypokemon=df[df["Weight"]>=100]
print(heavypokemon)
legand=df[df["Legendary"]==True]
print(legand)
waterpokemon=df[(df["Type1"]=="Water")|(df["Type2"]=="Water")]
print(waterpokemon)