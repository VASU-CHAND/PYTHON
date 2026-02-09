
n = int(input("Enter number of fruits in s1: "))
s1 = set()

for i in range(n):
    fruit = input()
    s1.add(fruit)

m = int(input("Enter number of fruits in s2: "))
s2 = set()

for i in range(m):
    fruit = input()
    s2.add(fruit)

print("Common fruits:", s1 & s2)
print("Only in s1:", s1 - s2)
print("Total fruits count:", len(s1 | s2))
