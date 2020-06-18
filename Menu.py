from tkinter import*
from tkinter import messagebox

def end():
    win.destroy()



def play():
    win.destroy()
    game()


def help():
    messagebox.showinfo("Instructions",'Hi ! You can jump using space-bar and UP-arrow key \
to avoid the hurdles. If you crash into a hurdle , you will have to guess a word to continue')




win=Tk()
win.title("Deadly Words")
intro=Label(win,text="Welcome to Deadly words!!")
intro.grid(row=0,column=0)


#Buttons

play_button=Button(win,text="Play",command=play)
play_button.grid(row=1,column=0)

help_button=Button(win,text="Help",command=help)
help_button.grid(row=2,column=0)


quit=Button(win,text="Quit",command=end)
quit.grid(row=3,column=0)





#Main_Loop
win.mainloop()

