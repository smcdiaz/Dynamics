# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:43:56 2013

@author: Santiago
"""
import numpy as np

class control:

    def __init__(self,Kp,Kv):
        self.Kp=Kp
        self.Kv=Kv
        
    def P(self,x_des,y_des,x,y):
        inc_x=self.Kp*(x_des - x) 
        inc_y=self.Kp*(y_des - y) 
        
        return np.matrix([inc_x, inc_y])
         
    def D(self,xd_des,yd_des,xd,yd):
        acc_x=self.Kv*(xd_des - xd)
        acc_y=self.Kv*(yd_des - yd)
        
        return [acc_x, acc_y]
        
    def PD(self,x_des,y_des,o_des,xd_des,yd_des,od_des,x,y,o,xd,yd,od):
        acc_x=self.Kp*(x_des - x) + self.Kv*(xd_des - xd)
        acc_y=self.Kp*(y_des - y) + self.Kv*(yd_des - yd)
        acc_o=self.Kp*(o_des - o) + self.Kv*(od_des - od)
        return np.matrix([acc_x, acc_y,acc_o])