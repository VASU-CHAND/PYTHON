from tkinter import *
from PIL import Image, ImageTk
#button you click it does some work
count=0
def click():
    global count
    count+=1
    print("you clicked the button "+str(count)+" times")


window=Tk()
window.geometry('300x300')
img=Image.open(r"C:\Users\vaibh\Downloads\wp2567396-tony-stark-hd-wallpapers.jpg")
img=img.resize((300,300))
photo=ImageTk.PhotoImage(img)

button=Button(window,text="click me",command=click,font=('Arial',20,'bold'),fg='red',bg='yellow' , image=photo,compound='bottom'    )
button.pack()
window.mainloop()