import tkinter as tk

root = tk.Tk()

spin = tk.Spinbox(root, from_=1, to=10)
spin.pack()

root.mainloop()