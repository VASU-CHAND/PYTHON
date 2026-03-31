
import tkinter as tk

root = tk.Tk()

scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(root, yscrollcommand=scroll.set)

for i in range(50):
    listbox.insert(tk.END, "Item " + str(i))

listbox.pack()
scroll.config(command=listbox.yview)

root.mainloop()