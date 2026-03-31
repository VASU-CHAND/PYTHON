import tkinter as tk

root = tk.Tk()

var1 = tk.IntVar()

check = tk.Checkbutton(root, text="Python", variable=var1)
check.pack()

root.mainloop()