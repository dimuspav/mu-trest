#!/usr/bin/python3
import pgzero
WIDTH = 700         # width of the window
HEIGHT = 800        # height of the window 
car = Actor("racecar")
car.pos = 350, 560
def draw():             # pygame zero draw function
    screen.fill((128, 128, 128))    # fill the screen with
    car.draw()        
 
