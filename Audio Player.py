# importing required modules
import pygame
from tkinter import *

# defining functions

def play():
    pygame.mixer.music.load('')
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()
