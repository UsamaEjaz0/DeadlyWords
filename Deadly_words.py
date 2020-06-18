import pygame

from pygame.locals import *
import os

import random
import tkinter
from tkinter import *
from tkinter import messagebox

def game():
    
    pygame.init()

    Width, Height = 800, 437
    win = pygame.display.set_mode((Width,Height))
    pygame.display.set_caption('DEADLY WORDS')

    background = pygame.image.load(os.path.join('images','bg.png')).convert()
    background_X = 0
    background_X2 = background.get_width()

    clock = pygame.time.Clock()

    class Khan(object):
        run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
        jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
        
        fall = pygame.image.load(os.path.join('images','0.png'))
        jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]

        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.in_air = False
        
            self.falling = False
          
            self.jumpCount = 0
            self.runCount = 0
            

        def create(self, win):
            if self.falling:
                win.blit(self.fall, (self.x, self.y ))
                    
            elif self.in_air:
                self.y -= self.jumpList[self.jumpCount] * 1.3
                print(self.jumpCount)
                win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
                self.jumpCount += 1
                if self.jumpCount > 108:
                    self.jumpCount = 0
                    self.in_air = False
                    self.runCount = 0
                self.hitbox = (self.x+15,self.y,self.width-30,self.height-10)
                
            else:
                if self.runCount > 42:
                    self.runCount = 0
                win.blit(self.run[self.runCount//6], (self.x,self.y))
                self.runCount += 1
                self.hitbox = (self.x+ 15,self.y,self.width-30,self.height-13)
     
            #pygame.draw.rect(win, (255,0,0),self.hitbox, 2)

    class blades(object):
        rotate = [pygame.image.load(os.path.join('images', 'SAW0.PNG')),pygame.image.load(os.path.join('images', 'SAW1.PNG')),pygame.image.load(os.path.join('images', 'SAW2.PNG')),pygame.image.load(os.path.join('images', 'SAW3.PNG'))]
        def __init__(self,x,y,width,height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.rotateCount = 0
            self.vel = 1.4

        def create(self,win):
            self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
            #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
            if self.rotateCount >= 8:
                self.rotateCount = 0
            win.blit(pygame.transform.scale(self.rotate[self.rotateCount//2], (64,64)), (self.x,self.y))
            self.rotateCount += 1
            
        def collide(self, rect):
            if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
                if rect[1] + rect[3] > self.hitbox[1]:
                    
                    return True
            return False




   



    

            

    def deadly_word():
     win=Tk()
     win.title("Deadly Words")
     words=['hello','movie']
     word=random.choice(words)
     guess="entry"
     list=[]
     guesses=10
     for k in range(len(word)):
          list.append('_')
     
     def Main_logic():
         global guess
         
         nonlocal guesses
       
         guess=entry.get()
         nonlocal word
         nonlocal list
         num=len(word)
         
         for i in range(len(word)):
             
             for p in range(len(word)):
                 if word[p]==guess:
                     list[p]=guess
                     
                 if not(guess in word):
                      guesses=guesses-1/(num*num)
                 if int(guesses)==0:
                      messagebox.showinfo('Oops','Game Over')
                      pygame.QUIT()
                 
               
                      
             z=(' '.join(list))
             
         print(int(guesses))
         if not('_' in list):
              win.destroy()
         else:
              guess_label=Label(win,text=str(z))
              guess_label.grid(row=1,column=0)
         

         
     entry=Entry(win)
     entry.grid(row=0,column=0,columnspan=1)

     guess=Label(win,text="Guess the word to continue!")
     guess.grid(row=2,column=0)   

     guessb=Button(win,text="Guess",command=Main_logic)
     guessb.grid(row=3,column=0,rowspan=5)

     
     win.mainloop()



    def newWindow():
        largeFont = pygame.font.SysFont('comicsans', 30)
        win.blit(background, (background_X, 0))
        win.blit(background, (background_X2,0))
        text = largeFont.render('Score: ' + str(score), 1, (255,255,255))
        runner.create(win)
        for hurdle in hurdles:
            hurdle.create(win)

        win.blit(text, (700, 10))
        pygame.display.update()


    pygame.time.set_timer(USEREVENT+1, 500)
    pygame.time.set_timer(USEREVENT+2, 3000)
    speed = 100

    score = 0

    run = True
    runner = Khan(200, 313, 64, 64)

    hurdles = []
    
    fallSpeed = 0
    
    check=0
    print("P")
    while run:
        
        score = speed//10 - 3  
        
        for hurdle in hurdles:
            if hurdle.collide(runner.hitbox):
                if check==0:   
                    deadly_word()
                    check=1
             
                
                    
                
                
               
                
                
                
                
            if hurdle.x < -64:
                hurdles.pop(hurdles.index(hurdle))
                check=0
                
            else:
                hurdle.x -= 1.5
                
        
        background_X -= 1.5
        background_X2 -= 1.5

        if background_X < background.get_width() * -1:
            background_X = background.get_width()
        if background_X2 < background.get_width() * -1:
            background_X2 = background.get_width() 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
                
            if event.type == USEREVENT+1:
                speed += 1
                
            if event.type == USEREVENT+2:
                r = random.randrange(0,2)
                if r == 0:
                    hurdles.append(blades(810, 310, 64, 64))
              
                    
        if runner.falling == False:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                if not(runner.in_air):
                    runner.in_air = True

         

        clock.tick(speed)
        newWindow()


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
win.geometry(("350x350"))
intro=Label(win,text="Welcome to Deadly words!!")
intro.pack()
intro.config(bg='yellow',fg='black')
win.configure( background =  'black')
l=Label(win,text="        ")
l.pack()
l.config(bg='black',fg='black')

photo = PhotoImage(file = "SAW0.gif")
w = Label(win, image=photo)
w.pack()


l=Label(win,text="        ")
l.pack()
l.config(bg='black',fg='black')
#Buttons

play_button=Button(win,text="Play",command=play)
play_button.pack()
play_button.config(bg='brown',fg='black')
l=Label(win,text="        ")
l.pack()
l.config(bg='black',fg='black')
help_button=Button(win,text="Help",command=help)
help_button.pack()
help_button.config(bg='brown',fg = 'black')

l=Label(win,text="        ")
l.pack()
l.config(bg='black',fg='black')
quit=Button(win,text="Quit",command=end)
quit.pack()
quit.config(bg='brown' ,fg ='black')





#Main_Loop
win.mainloop()



