total_area = 0

with open("city.txt", "r") as f:
    for line in f:
        name, pop, area = line.split()
        pop = float(pop)
        area = float(area)

        print(name, pop, area)

        if pop > 10:
            print("Population >10L:", name)

        total_area += area

print("Total area:", total_area)