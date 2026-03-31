# a layout manager in tk inter is
#  used to 
#tkinter provides 3 layout managers 
# first is pac second is grid third is grid
#
import tkinter as tk
root=tk.Tk()

root.title("pack layout ")
root.geometry("400x400")

button1=tk.Button(root,text="top")
button2=tk.Button(root,text="left")
button3=tk.Button(root,text="right")
button4=tk.Button(root,text="bottom")

button1.pack(side=tk.TOP)
button2.pack(side=tk.LEFT)
button3.pack(side=tk.RIGHT)
button4.pack(side=tk.BOTTOM)
grid

root.mainloop()