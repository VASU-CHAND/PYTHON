# LifeOS Analytics - Single File Project

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from tkinter import *
from tkinter import messagebox

# ---------------- DATABASE ---------------- #

def connect():
    return sqlite3.connect("lifeos.db")

def create_table():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS activity(
        date TEXT,
        study REAL,
        sleep REAL,
        exercise REAL,
        screen REAL
    )
    """)
    
    conn.commit()
    conn.close()

def insert_data(data):
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO activity VALUES (?,?,?,?,?)", data)
    
    conn.commit()
    conn.close()

def fetch_all():
    conn = connect()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM activity")
    rows = cur.fetchall()
    
    conn.close()
    return rows

# ---------------- UTILITIES ---------------- #

def validate_date(date):
    pattern = r"\d{4}-\d{2}-\d{2}"
    return re.fullmatch(pattern, date)

def safe_float(value):
    try:
        return float(value)
    except:
        return 0.0

# ---------------- ANALYTICS ---------------- #

def get_dataframe():
    data = fetch_all()
    df = pd.DataFrame(data, columns=["date","study","sleep","exercise","screen"])
    return df

def calculate_productivity(df):
    df["score"] = (df["study"]*2 + df["exercise"]) - (df["screen"]/2)
    return df

def show_stats():
    df = get_dataframe()
    
    if df.empty:
        messagebox.showinfo("Info", "No data available")
        return
    
    df = calculate_productivity(df)
    
    avg = np.mean(df["score"])
    max_score = np.max(df["score"])
    min_score = np.min(df["score"])
    
    messagebox.showinfo("Statistics",
        f"Average Score: {avg:.2f}\nMax Score: {max_score:.2f}\nMin Score: {min_score:.2f}")

def plot_graph():
    df = get_dataframe()
    
    if df.empty:
        messagebox.showinfo("Info", "No data to plot")
        return
    
    df = calculate_productivity(df)
    
    plt.figure()
    plt.plot(df["date"], df["score"], marker='o')
    plt.title("Productivity Trend")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------------- GUI ---------------- #

create_table()

root = Tk()
root.title("LifeOS Analytics")
root.geometry("400x450")

# Labels & Entries

Label(root, text="Date (YYYY-MM-DD)").pack()
date_entry = Entry(root)
date_entry.pack()

Label(root, text="Study Hours").pack()
study_entry = Entry(root)
study_entry.pack()

Label(root, text="Sleep Hours").pack()
sleep_entry = Entry(root)
sleep_entry.pack()

Label(root, text="Exercise Hours").pack()
exercise_entry = Entry(root)
exercise_entry.pack()

Label(root, text="Screen Time").pack()
screen_entry = Entry(root)
screen_entry.pack()

# Submit Function

def submit():
    date = date_entry.get()
    
    if not validate_date(date):
        messagebox.showerror("Error", "Invalid Date Format (YYYY-MM-DD)")
        return
    
    study = safe_float(study_entry.get())
    sleep = safe_float(sleep_entry.get())
    exercise = safe_float(exercise_entry.get())
    screen = safe_float(screen_entry.get())
    
    try:
        insert_data((date, study, sleep, exercise, screen))
        messagebox.showinfo("Success", "Data Saved!")
        
        # Clear fields
        date_entry.delete(0, END)
        study_entry.delete(0, END)
        sleep_entry.delete(0, END)
        exercise_entry.delete(0, END)
        screen_entry.delete(0, END)
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Buttons

Button(root, text="Add Data", command=submit).pack(pady=10)

Button(root, text="Show Statistics", command=show_stats).pack(pady=10)

Button(root, text="Show Graph", command=plot_graph).pack(pady=10)

# Run App

root.mainloop()