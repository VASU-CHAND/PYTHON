import tkinter as tk

def click(val):
    entry.insert(tk.END, val)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.insert(0, "Error")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

for i in range(10):
    tk.Button(root, text=str(i), command=lambda i=i: click(i)).pack()

tk.Button(root, text="+", command=lambda: click("+")).pack()
tk.Button(root, text="=", command=calculate).pack()
tk.Button(root, text="C", command=clear).pack()

root.mainloop()