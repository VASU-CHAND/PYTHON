tasks = []

while True:
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Remove Task")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == 2:
        for i in range(len(tasks)):
            print(i + 1, tasks[i])

    elif choice == 3:
        num = int(input("Enter task number to remove: "))
        tasks.pop(num - 1)

    elif choice == 4:
        break

    else:
        print("Invalid choice")
