from turtle import speed
import pygame, sys
from pygame.locals import *

class Paddle:
    def __init__(self, x, y, length, width, speed, number):
        self.ypos = y
        self.xpos = x
        self.length = length
        self.width = width
        self.speed = speed
        self.number = number

    def move(self, k):
       
        # For Q-learning agent or AI conditional agent
            if k == 0:
                self.ypos -= self.speed  
                if (self.ypos < 0):
                    self.ypos = 0
            if k == 1:
                self.ypos += self.speed
                if(self.ypos > 720):
                    self.ypos = 720 

    def discretePos(self, Bin):
        return int(self.ypos // (720 / Bin+1))