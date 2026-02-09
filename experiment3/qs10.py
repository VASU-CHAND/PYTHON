n = 5
i = n

while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1

    k = 1
    while k <= 2 * (n - i):
        print("*", end="")
        k = k + 1

    j = i
    while j >= 1:
        print(j, end="")
        j = j - 1

    print()
    i = i - 1
