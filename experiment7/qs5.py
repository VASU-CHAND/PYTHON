try:
    f = open("file.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")
finally:
    print("Done")