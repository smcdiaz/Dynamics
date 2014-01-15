# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:59:59 2013

@author: Santiago
"""
import pseudoinv as ps
from dkyn_q import coord_q6
import numpy as np
from plant import q3, q4, q5  
from jacobian import Jlm6
 
def ikin(pf,qi):
    ilimit=5000
    min=0.0008
    q=np.matrix([[0.1],[0.1],[0.1]])#np.zeros((3,1))
    error=1
    count=0
    pf=coord_q6.subs({q3:qi[0,0],q4:qi[1,0],q5:qi[2,0]})/1000
    
    while (error > min):
        jpsi=ps.jac_psi(Jlm6,qi[0,0],qi[1,0],qi[2,0],0,0,0)
        dq=jpsi*pf
        
        qi = qi + 1*dq
        
        pi=coord_q6.subs({q3:qi[0,0],q4:qi[1,0],q5:qi[2,0]})/1000
        
        error=np.linalg.norm((pi-pf),1)
        
        count=count + 1
        if count > ilimit:
            break
    return q