# -*- coding: utf-8 -*-
"""
Created on Tue Oct 08 04:29:22 2013

@author: Santiago
"""
from numint import *
import pygame
import matplotlib.pyplot as plt

class Animation:
  def __init__(self, (q3_i ,q4_i, q5_i)):
    self.L3 = 100
    self.L4 = 330
    self.L5 = 300
    self.L6 = 120
    self.Q3 = q3_i
    self.Q4 = q4_i
    self.Q5 = q5_i
    self.colour = (0, 0, 255)
    self.thickness = 5  
    
  def display(self,rob):
    L6i=(width/2,height-20)
    L6f=(rob[3][0]+L6i[0],L6i[1]-rob[3][1])
    L5i=L6f
    L5f=(rob[2][0]+L6i[0],L6i[1]-rob[2][1])
    L4i=L5f
    L4f=(rob[1][0]+L6i[0],L6i[1]-rob[1][1])
    L3i=L4f
    L3f=(rob[0][0]+L6i[0],L6i[1]-rob[0][1])
    #Ground
    pygame.draw.line(screen, (103,64,58), (0,height), (width,height), self.thickness+35)
    #Foot
    pygame.draw.line(screen, self.colour, (L6i[0]-50,L6i[1]), (L6i[0]+50,L6i[1]), self.thickness)
    #Link 6     
    pygame.draw.line(screen, self.colour, L6i, L6f, self.thickness)
    #Joint 5 + Link 5    
    pygame.draw.circle(screen, self.colour,(int(L6f[0]),int(L6f[1])),15,self.thickness)
    pygame.draw.line(screen, self.colour, L5i, L5f, self.thickness)
    #Joint 4 + Link 4
    pygame.draw.circle(screen, self.colour,(int(L5f[0]),int(L5f[1])),15,self.thickness)    
    pygame.draw.line(screen, self.colour, L4i, L4f, self.thickness)
    #Joint 3 + Link 3
    pygame.draw.circle(screen, self.colour,(int(L4f[0]),int(L4f[1])),15,self.thickness)    
    pygame.draw.line(screen, self.colour, L3i, L3f, self.thickness)
    pygame.draw.circle(screen, self.colour,(int(L3f[0]),int(L3f[1])),15,self.thickness)    
    
#Ploting Q, Qd and Qdd
plt.figure(1)
plt.subplot(311)
plt.plot(y[:][0])
plt.plot(y[:][1])
plt.plot(y[:][2])
plt.ylabel('Q')
plt.subplot(312)
plt.plot(y[:][3])
plt.plot(y[:][4])
plt.plot(y[:][5])
plt.ylabel('Qd')
plt.subplot(313)
plt.plot(y[:][6])
plt.plot(y[:][7])
plt.plot(y[:][8])
plt.ylabel('Qdd')
plt.show()

#Ploting XY coordinates of joints
plt.figure(2)
plt.subplot(311)
plt.plot(XYZ_m3)
plt.subplot(312)
plt.plot(XYZ_m4)
plt.subplot(313)
plt.plot(XYZ_m6)
plt.show()

#Model animation
(width,height)=(800,500)
background_colour = (255,255,255)
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('ROBOT 1')
screen.fill(background_colour)
anime = Animation((0,0,0))
for p in range(0,len(tray)-1):
    anime.display(tray[p])
    pygame.display.flip()
    pause(0.1)
    screen.fill(background_colour)
