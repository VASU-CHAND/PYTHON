try:
    with open("count.txt", "r") as f:
        count = int(f.read())
except:
    count = 0

count += 1

with open("count.txt", "w") as f:
    f.write(str(count))

print("Program executed", count, "times")