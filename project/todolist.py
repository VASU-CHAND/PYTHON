import tkinter as tk
from tkinter import messagebox
import os

# File path (same folder as script)
FILE_NAME = os.path.join(os.path.dirname(__file__), "tasks.txt")

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showerror("Error", "Select a task")

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(selected, "✔ " + task)
    except:
        messagebox.showerror("Error", "Select a task")

def clear_all():
    listbox.delete(0, tk.END)

def save_tasks():
    tasks = listbox.get(0, tk.END)
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:   # ✅ FIXED
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:   # ✅ FIXED
            for task in file:
                listbox.insert(tk.END, task.strip())

# ---------------- UI ---------------- #

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")
root.configure(bg="#1e1e2f")

# Title
tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task,
          bg="#4CAF50", fg="white", width=15).pack(pady=5)

tk.Button(root, text="Delete Task", command=delete_task,
          bg="#f44336", fg="white", width=15).pack(pady=5)

tk.Button(root, text="Mark Done", command=mark_done,
          bg="#2196F3", fg="white", width=15).pack(pady=5)

tk.Button(root, text="Save Tasks", command=save_tasks,
          bg="#FF9800", fg="white", width=15).pack(pady=5)

tk.Button(root, text="Clear All", command=clear_all,
          bg="#9C27B0", fg="white", width=15).pack(pady=5)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10)
listbox.pack(pady=20)

# Load saved tasks
load_tasks()

# Run app
root.mainloop()