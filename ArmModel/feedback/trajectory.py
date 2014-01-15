# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:33:51 2013

@author: Santiago
"""
import numpy as np

def line(xi,yi,xf,yf,tf,nstep):

    xt=[]
    yt=[]
    xdt=[]
    ydt=[]
    
    xd = (xf - xi) / tf
    yd= (yf - yi) / tf 
    
    for inc in range(nstep):
        t=(tf/nstep)*inc
        x = xi + xd * t
        y = yi + yd * t
        xt.append(x)
        yt.append(y)
        xdt.append(xd)
        ydt.append(yd)
 
    return np.matrix([xt,yt,xdt,ydt])
    
#xy_t=line(0.0,0.0,10.0,10.0,5.0,50)
    