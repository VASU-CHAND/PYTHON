
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

result = messagebox.askyesno("Question", "Do you want to continue?")

print(result)

root.mainloop()