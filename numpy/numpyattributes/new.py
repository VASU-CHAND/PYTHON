from tkinter import *
import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
age TEXT,
course TEXT
)
""")

conn.commit()

def add_student():

    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()

    cursor.execute(
    "INSERT INTO students(name,age,course) VALUES(?,?,?)",
    (name,age,course)
    )

    conn.commit()

    name_entry.delete(0,END)
    age_entry.delete(0,END)
    course_entry.delete(0,END)

    display_students()

def display_students():

    listbox.delete(0,END)

    cursor.execute("SELECT * FROM students")

    for row in cursor.fetchall():
        listbox.insert(END,row)

def delete_student():

    selected = listbox.get(ANCHOR)

    cursor.execute("DELETE FROM students WHERE id=?", (selected[0],))

    conn.commit()

    display_students()

root = Tk()
root.title("Student Registration Form")
root.geometry("500x400")

Label(root,text="Name").grid(row=0,column=0,padx=10,pady=10)
Label(root,text="Age").grid(row=1,column=0,padx=10,pady=10)
Label(root,text="Course").grid(row=2,column=0,padx=10,pady=10)

name_entry = Entry(root)
name_entry.grid(row=0,column=1)

age_entry = Entry(root)
age_entry.grid(row=1,column=1)

course_entry = Entry(root)
course_entry.grid(row=2,column=1)

Button(root,text="Add Student",command=add_student,width=15).grid(row=3,column=1,pady=10)

Button(root,text="Delete Student",command=delete_student,width=15).grid(row=4,column=1,pady=10)

Button(root,text="Show Students",command=display_students,width=15).grid(row=5,column=1,pady=10)

listbox = Listbox(root,width=50)
listbox.grid(row=6,column=0,columnspan=3,pady=20)

root.mainloop()