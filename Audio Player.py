# importing required modules
import pygame
from tkinter import *

# defining functions

def play():
    pygame.mixer.music.load('sample2.wav')
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()


pygame.init()
root = Tk()
root.title('Audio Player') #title window
root.geometry('400x500')

myframe = Frame(root)
myframe.pack()

mylabel = Label(myframe, text="Python Music Player") #description
mylabel.pack()

#setting buttons

button1 = Button(myframe, text="Play", command=play(), width=18)
button1.pack(pady=5)
button2 = Button(myframe, text="stop", command=stop(), width=18)
button2.pack(pady=5)

root.mainloop()
