from tkinter import *
root = Tk()
photo = PhotoImage(file = "13.gif")
w = Label(root, image=photo)
w.pack()
ent = Entry(root)
ent.pack()
ent.focus_set()
root.configure(background = 'black')
root.mainloop()

