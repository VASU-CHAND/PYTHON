
import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Draw shapes
canvas.create_line(0, 0, 200, 100)
canvas.create_rectangle(50, 50, 150, 120, fill="blue")
canvas.create_oval(160, 50, 250, 120, fill="red")

root.mainloop