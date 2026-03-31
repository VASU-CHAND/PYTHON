
import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

items = ["Python", "Java", "C++", "JavaScript"]

for item in items:
    listbox.insert(tk.END, item)

root.mainloop()