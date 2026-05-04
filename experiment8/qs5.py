import tkinter as tk

def login():
    if user.get() == "admin" and pwd.get() == "123":
        print("Login success")
    else:
        print("Invalid")

root = tk.Tk()

user = tk.Entry(root)
user.pack()

pwd = tk.Entry(root, show="*")
pwd.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()