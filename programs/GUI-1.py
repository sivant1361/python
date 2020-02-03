from tkinter import Tk,Label,Button
root=Tk()
root.title("Siva GUI-1")
msg=Label(root,text="Sivant GUI-1!!!")
msg.config(font=("Copperplate Gothic Bold",25,"bold"))
msg.pack()
msgb=Button(root,text="exit",command=root.destroy)
msgb.pack()
root.mainloop()
