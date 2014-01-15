# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 11:32:34 2013

@author: Santiago
"""

import numpy as np
import lambmat as lm
from sympy import *
import pseudoinv as ps
import ccmat as ccm
import gmat as gm
from jacobian import *
from imat import A

def MU(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5):
    jdc=ps.Jdc(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5)  
    #jdc_t=np.transpose(jdc)
    
    b=ccm.b.subs(q3,ang3)
    b=b.subs(q4,ang4)  
    b=b.subs(q5,ang5) 
    b=b.subs(qd3,acc3)
    b=b.subs(qd4,acc4)    
    b=b.subs(qd5,acc5)
    
    #Conversion to numpy matrix
    B=matrix2numpy(b)
      
    mu=np.dot(jdc,B)
    return mu
    
def RO(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5):
    jdc=ps.Jdc(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5)  
    #jdc_t=np.transpose(jdc)
    g=gm.g.subs(q3,ang3)
    g=g.subs(q4,ang4)  
    g=g.subs(q5,ang5) 
    g=g.subs(qd3,acc3)
    g=g.subs(qd4,acc4)
    g=g.subs(qd5,acc5)
    #Conversion to numpy matrix
    G=matrix2numpy(g)

    ro=np.dot(jdc.T,G)
    return ro
    
def Fwd_Dyn(st,F):
    """Define the right-hand side of equation dy/dt = a*y"""
    mu=MU(A,Jlm6,st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])    
    ro=RO(A,Jlm6,st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])
    jdc=ps.Jdc(A,Jlm6,st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])  
    perturbation=mu+ro 

    (L,Li)=lm.mass2lamb(A,Jlm6,st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])
 
    Fd=F#-perturbation    

    xdd=Fd*Li
       
    return xdd
    
def Inv_Dyn(st,F,xdd):
    """Define the right-hand side of equation dy/dt = a*y"""
    #mu=MU(A,Jlm6,st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])    
    #ro=RO(A,Jlm6,st[0],st[1],st[2],st[3],st[4],st[5])
    jdc=ps.Jdc(A,Jlm6,st[0],st[1],st[2],st[3],st[4],st[5])  
    jdc=np.matrix(jdc)
    #perturbation=ro#+mu 
        
    #(L,Li)=lm.mass2lamb(A,Jlm6,st[0],st[1],st[2],st[3],st[4],st[5])
    print jdc.shape,F.shape
    #F=L*xdd.T#+perturbation
    T=np.dot(jdc,F.T)
    
    return T