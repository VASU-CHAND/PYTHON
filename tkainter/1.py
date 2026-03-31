# used to create gui applications
#gui means text boxes 
#uses of tk  inter
import tkinter as tk
root=tk.Tk()
#title of window
root.title("my first app")
#run the window
root.geometry("400x400")



label=tk.Label(root,text="hello world")
label.pack()
def fun():
    print("button clicked")

btn= tk.Button(root,text="click me",command=fun)
btn.pack()
root.mainloop()