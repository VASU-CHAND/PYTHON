from tkinter import *
from PIL import ImageTk,Image
window = Tk() #instabtiate an instance of a window
window.geometry("800x420") #set the size of the window
window.title("vasu Code First GUI") #set the title of the window
img=Image.open(r"C:\Users\vaibh\OneDrive\Pictures\marvels-spider-man-4096x1738-13276.jpeg") #open the image
img=img.resize((400,300)) #resize the image
photo=ImageTk.PhotoImage(img) #convert the image to a photoimage
label=Label(window,image=photo) #create a label and set the image as the label
label.pack() #place the label on the window
window.mainloop() #rplace window on the screen ,;istem for events