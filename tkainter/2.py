import tkinter as tk

root = tk.Tk()

var = tk.StringVar()

r1 = tk.Radiobutton(root, text="Male", variable=var, value="Male")
r2 = tk.Radiobutton(root, text="Female", variable=var, value="Female")

r1.pack()
r2.pack()

root.mainloop()