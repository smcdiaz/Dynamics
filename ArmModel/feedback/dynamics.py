# -*- coding: utf-8 -*-
"""
Created on Fri Nov 01 11:32:34 2013

@author: Santiago
"""

import numpy as np
import lambmat as lm
import sympy as sp
import pseudoinv as ps
import ccmat as ccm
import gmat as gm
from jacobian import Jlm6
from imat import A
from plant import q3,q4,q5,qd3,qd4,qd5

def MU(ang3,ang4,ang5,acc3,acc4,acc5):
    jdc=ps.Jdc(ang3,ang4,ang5,acc3,acc4,acc5)  
    #jdc_t=np.transpose(jdc)
    
    b=ccm.b.subs(q3,ang3)
    b=b.subs(q4,ang4)  
    b=b.subs(q5,ang5) 
    b=b.subs(qd3,acc3)
    b=b.subs(qd4,acc4)    
    b=b.subs(qd5,acc5)
    
    #Conversion to numpy matrix
    B=sp.matrix2numpy(b)
      
    mu=np.dot(jdc,B)
    return mu
    
def RO(ang3,ang4,ang5,acc3,acc4,acc5):
    jdc=ps.Jdc(ang3,ang4,ang5,acc3,acc4,acc5)  
    #jdc_t=np.transpose(jdc)
    g=gm.g.subs(q3,ang3)
    g=g.subs(q4,ang4)  
    g=g.subs(q5,ang5) 
    g=g.subs(qd3,acc3)
    g=g.subs(qd4,acc4)
    g=g.subs(qd5,acc5)
    #Conversion to numpy matrix
    G=sp.matrix2numpy(g)

    ro=np.dot(jdc.T,G)
    return ro
    
def T0(qi,q_des,Kd,qdi):
    dif=np.matrix(qi-q_des)
    pot=np.matrix([dif[0,0]**2,dif[0,1]**2,dif[0,2]**2])
    aux=Kd*qdi
    res=np.matrix(pot-aux)
    T0=-A*res.T
    return T0
    
def Fwd_Dyn(st,Td):
   
    mu=MU(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])    
    ro=RO(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])
    jdc=ps.Jdc(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])  
   
    perturbation=mu+ro 
    F=np.dot(jdc,Td.T)
    
    T=F-perturbation
        
    (L,Li)=lm.mass2lamb(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])
    
    xdd=np.dot(Li,T)
        
    return xdd
    
def Inv_Dyn(st,F,xdd):
   
    #mu=MU(A,Jlm6,st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])    
    #ro=RO(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])
    J=Jlm6.subs({q3:st[0,0],q4:st[1,0],q5:st[2,0],qd3:st[3,0],qd4:st[4,0],qd5:st[5,0]})
    J=sp.matrix2numpy(J)
    J=np.matrix(J)
    jdc=ps.Jdc(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0]) 
    #print J.shape,F.shape
    T0=np.dot(J.T,F.T)    
    #T0=np.matrix(T0)    
    #perturbation=ro#+mu 
        
    (L,Li)=lm.mass2lamb(st[0,0],st[1,0],st[2,0],st[3,0],st[4,0],st[5,0])
    
    #F=np.dot(L,xdd.T)#+perturbation
    
    #Null Space computing
    I=np.eye(3)
    I=np.matrix(I)    
    aux=np.dot(J.T,jdc.T)
    Ns=np.dot((I-aux),T0)

    T=np.dot(J.T,F.T)+Ns
    print T
    #print T
    return T