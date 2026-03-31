import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()

name = simpledialog.askstring("Input", "Enter your name")

print(name)


root.mainloop()
#they allow user to input data selct files and confirm the action