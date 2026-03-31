
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

combo = ttk.Combobox(root)
combo['values'] = ("Python", "Java", "C++")

combo.pack()
combo.current(0)

root.mainloop()