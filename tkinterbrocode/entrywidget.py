from tkinter import *
from PIL import Image, ImageTk
def submit():
    user=entry.get()
    print("you entered "+user)
    entry.config(state=DISABLED) #disable the entry widget after submitting the data

def delete():
    entry.delete(0,END) #delete from 0 to end

def backspace():
    entry.delete(len(entry.get())-1,END) #delete the last character   
window=Tk()
window.geometry('600x600')
entry=Entry(window,font=('Arial',20,'bold'),fg='red',bg='yellow',show="*") #show is used to hide the text entered in the entry widget   
entry.pack(side=LEFT)    
submitbutton=Button(window,text="submit",font=('Arial',20,'bold'),fg='red',bg='yellow',command=submit   )
submitbutton.pack(side=RIGHT)
deletebutton=Button(window,text="delete",font=('Arial',20,'bold'),fg='red',bg='yellow',command=delete   )
deletebutton.pack(side=RIGHT)
backspacebutton=Button(window,text="backspace",font=('Arial',20,'bold'),fg='red',bg='yellow',command=backspace   )
backspacebutton.pack(side=RIGHT)

window.mainloop()