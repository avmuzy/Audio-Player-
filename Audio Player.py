
import pygame
from tkinter import *


def play():
    pygame.mixer.music.load('')
    pygame.mixer.music.play()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()

def stop():
    pygame.mixer.music.stop()


def sound():
    pygame.mixer.Sound.play(sound_effect)


pygame.init()
sound_effect = pygame.mixer.Sound('')
pygame.event.wait()
root = Tk()
root.geometry('150x300')

myframe = Frame(root)
myframe.pack()
# description
mylabel = Label(myframe, text="Python Audio Player")
mylabel.pack()

# setting buttons
button1 = Button(myframe, text="Play", command=play, width=15)
button1.pack(pady=5)
button2 = Button(myframe, text="Sound", command=sound, width=15)
button2.pack(pady=5)
button3 = Button(myframe, text="Unpause", command=unpause, width=15)
button3.pack(pady=5)
button4 = Button(myframe, text="Pause", command=pause, width=15)
button4.pack(pady=5)
button5 = Button(myframe, text="Stop", command=play, width=15)
button5.pack(pady=5)

# insert a image
canvas = Canvas(root, width=300, height=200)
canvas.pack()
img = PhotoImage(file="image1.png")
canvas.create_image(25, 25, anchor=NW, image=img)


root.mainloop()
