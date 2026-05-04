# names.txt should contain one name per line

with open("names.txt", "r") as f:
    names = f.read().splitlines()

# a) Count names
print("Total names:", len(names))

# b) Names starting with vowel
vowel_names = [n for n in names if n[0].lower() in 'aeiou']
print("Names starting with vowel:", len(vowel_names))

# c) Longest name
print("Longest name:", max(names, key=len))