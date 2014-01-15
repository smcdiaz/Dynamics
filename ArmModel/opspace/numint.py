# -*- coding: utf-8 -*-
"""
Created on Wed Oct 02 23:31:31 2013

@author: Santiago
"""
import numpy as np
from dkyn_q import coord_q3,coord_q4,coord_q5,coord_q6
from sympy import *
from plant import *
from imat import A
from ccmat import b
from jacobian import Jlm6
#from constraints import C
from gmat import g
from scipy.integrate import odeint
import dynamics as dy
import lambmat as lm

#T=Matrix([5000,500,50])
#T=Matrix([0,0,0])

#Recursive callable function
def deriv(st, t, F, xdd):
    """Define the right-hand side of equation dy/dt = a*y"""
    T=dy.Inv_Dyn(st,F,xdd) 
    
    B=T-g-b
    M=[]
    M=A.subs(q3,st[0])
    M=M.subs(q4,st[1])  
    M=M.subs(q5,st[2]) 
    M=M.subs(qd3,st[3])
    M=M.subs(qd4,st[4])
    M=M.subs(qd5,st[5])
    
    B=B.subs(q3,st[0])
    B=B.subs(q4,st[1])
    B=B.subs(q5,st[2]) 
    B=B.subs(qd3,st[3])
    B=B.subs(qd4,st[4])
    B=B.subs(qd5,st[5])
    
    A_inv=M**-1
    dp=A_inv*B    
    
    (L,Li)=lm.mass2lamb(A,Jlm6,st[0],st[1],st[2],st[3],st[4],st[5])
    
    xdd=Li*F.T
    #print A_inv
    f = [st[3],st[4],st[5],dp[0],dp[1],dp[2]]
    #print f
    return f
    
def grad(st):
    J=[]
    J=Jlm6.subs(q3,st[0])
    J=Jlm6.subs(q4,st[1])  
    J=Jlm6.subs(q5,st[2]) 
    return J
    
def integ():
    xdd=[0,0]
    F=np.matrix([0,0,0])
    # Times at which the solution is to be computed.
    t = np.linspace(0, 5,100)
    #print t
    # Solve the equation.
    print ("Integrating...")
    st0=[-pi/2,0,0,0,0,0]
        
    y = odeint(deriv,st0, t,(F,xdd))#, Dfun=grad(st0),rtol=0.1,atol=0.1)
    return y

#y=integ()