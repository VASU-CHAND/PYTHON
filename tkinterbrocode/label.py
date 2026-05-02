# label is an area widget that holds text and /ot an img within a window
from tkinter import *
from PIL import Image, ImageTk
from matplotlib import image
window=Tk()
window.geometry('600x600')
img=Image.open(r"C:\Users\vaibh\Downloads\wp2567396-tony-stark-hd-wallpapers.jpg")
img=img.resize((300,300))
photo=ImageTk.PhotoImage(img)
label=Label(window ,text="i'm ironman",font=('Arial',20,'bold'),fg='red',bg='yellow' , image=photo,compound='bottom')

label.pack()
#we can use place fn too
#label.place(x=0,y=0)
window.mainloop()       