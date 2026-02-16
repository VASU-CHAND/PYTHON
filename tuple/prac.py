tuple=('apple', ' kiwi', 'cherry')
mytup=2*tuple
print(mytup)
tup=(1,1,1,2,3,4,3,5)
x= tup.count(1)
print(x)
t = (1, 4, 7, 4, 9)

i = 0
position = -1

while i < len(t):
    if t[i] == 4:
        position = i
        break
    i = i + 1

print("Position:", position)
