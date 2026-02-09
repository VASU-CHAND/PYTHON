n = int(input("Enter number of students: "))
scores = []

for i in range(n):
    x = int(input())
    scores.append(x)

max1 = max(scores)

new_list = []
for i in scores:
    if i != max1:
        new_list.append(i)

runner_up = max(new_list)

print("Runner up score is:", runner_up)
