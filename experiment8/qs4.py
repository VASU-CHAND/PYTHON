import tkinter as tk

tasks = []

def add():
    task = entry.get()
    listbox.insert(tk.END, task)

def delete():
    listbox.delete(tk.ANCHOR)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

listbox = tk.Listbox(root)
listbox.pack()

tk.Button(root, text="Add", command=add).pack()
tk.Button(root, text="Delete", command=delete).pack()

root.mainloop()