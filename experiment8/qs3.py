import tkinter as tk
import sqlite3

conn = sqlite3.connect("students.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, course TEXT)")

def save():
    c.execute("INSERT INTO students VALUES (?,?)", (e1.get(), e2.get()))
    conn.commit()

root = tk.Tk()

e1 = tk.Entry(root)
e1.pack()
e2 = tk.Entry(root)
e2.pack()

tk.Button(root, text="Save", command=save).pack()

root.mainloop()