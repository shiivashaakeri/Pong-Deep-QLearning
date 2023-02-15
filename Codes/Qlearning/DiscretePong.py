from random import randint
from Paddle import *
from Ball import *
import numpy as np


class DiscretePong():
    

    def __init__(self, p1bin, ballXbin, ballYbin, ballXvelbin, ballYvelbin, ballXvelmax, ballYvelmax):
        
        #in_person = 1
        bot = 2

        #Paddle (x,y,length,width,speed,playernumber)

        self.paddle_AIconditional = Paddle(740, 300, 120, 20, 10, bot)
        self.paddle_Qlearner = Paddle(20, 300, 120, 20, 10, bot)
        
        #Ball (x,y,xvel,yvel,size)
        self.pongball = Ball(780/2, 720/2 , 8, 6,20)


        #Variables for dicretizing
        self.paddleBin = p1bin
        self.ballXBin = ballXbin
        self.ballYBin = ballYbin
        self.ballxvelBin = ballXvelbin
        self.ballyvelBin = ballYvelbin
        self.ballxvelMax = ballXvelmax
        self.ballyvelMax = ballYvelmax

    
    def update(self, action):        #Take action and update environment  #Return new state of environment

        running = True
        reward = 0
        hit = 0

        #Move paddle based on action
        self.paddle_Qlearner.move(action)
       
        #Follow Ball Y cord AI_conditional
        
        if (self.paddle_AIconditional.ypos + 60 > self.pongball.ypos):
            action = 0 #move down
        else:
            action = 1 #move up
        
        self.paddle_AIconditional.move(action)


        hit = self.pongball.move(self.pongball.xpos, self.pongball.ypos, self.pongball.xspeed, 
                                self.pongball.yspeed, self.paddle_Qlearner, self.paddle_AIconditional)

        
        #Punish if ball is missed (Concede a Goal)
        if (self.pongball.xpos < 0):
            reward = -100
            running = False

        #Reward if successful (Score a Goal) 
        if (self.pongball.xpos > 780):
            reward = 100
            running = False

        #discreatise
        ball_xvelocity, ball_yvelocity = self.pongball.discreteVel(self.ballxvelBin, self.ballyvelBin, 
                                                                    self.ballxvelMax, self.ballyvelMax)

        ball_xposition, ball_yposition = self.pongball.discretePos(self.ballXBin, self.ballYBin)
        paddle_position = self.paddle_Qlearner.discretePos(self.paddleBin)

        return (paddle_position, ball_xposition, ball_yposition, ball_xvelocity, ball_yvelocity), reward, running, hit    

