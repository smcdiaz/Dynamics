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
#from constraints import C
from gmat import g
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Recursive callable function
def deriv(st, t):
    """Define the right-hand side of equation dy/dt = a*y"""
    """
    LFUN=lambdify ([q2,q1,q3,q4,q5,qd1,qd2,qd3,qd4,qd5],FUN)
    print LFUN
    
    a=LFUN(st[0],st[1],st[2],st[3],st[4],st[5],st[6],st[7],st[8],st[9])  
    print a
    """
    B=T-g-b
    M=[]
    M=A.subs(q2,st[0])
    M=M.subs(q1,st[1])
    M=M.subs(q3,st[2])
    M=M.subs(q4,st[3])  
    M=M.subs(q5,st[4]) 
    M=M.subs(qd1,st[5])
    M=M.subs(qd2,st[6])
    M=M.subs(qd3,st[7])
    M=M.subs(qd4,st[8])
    M=M.subs(qd5,st[9])
    
    B=B.subs(q2,st[0])
    B=B.subs(q1,st[1])
    B=B.subs(q3,st[2])
    B=B.subs(q4,st[3])
    B=B.subs(q5,st[4]) 
    B=B.subs(qd1,st[5])
    B=B.subs(qd2,st[6])
    B=B.subs(qd3,st[7])
    B=B.subs(qd4,st[8])
    B=B.subs(qd5,st[9])
    
    A_inv=M.inverse()   
    dp=A_inv*B    
    
    f = [st[5],st[6],st[7],st[8],st[9],dp[0],dp[1],dp[2],dp[3],dp[4]]
    #print f
    return f

T=Matrix([0,0,0,0,0])

#T=(A*qdd)+b+g+C

# Times at which the solution is to be computed.
t = np.linspace(0, 7, 50)
#print t
# Solve the equation.
print ("Integrando...")
st0=[0,0,0.1,0.2,0.3,0,0,0,0,0]

y = odeint(deriv,st0, t)


#Substitution of angles in direct kynematics
XYZ_m3=[]
XYZ_m4=[]
XYZ_m5=[]
XYZ_m6=[]

for i in range(0,y.shape[0]-1):
    xyz_m3=coord_q3
    xyz_m4=coord_q4
    xyz_m5=coord_q5
    xyz_m6=coord_q6
    
    xyz_m3=xyz_m3.subs(q2,y[i][0])
    xyz_m3=xyz_m3.subs(q1,y[i][1])
    xyz_m3=xyz_m3.subs(q3,y[i][2])
    xyz_m3=xyz_m3.subs(q4,y[i][3])
    xyz_m3=xyz_m3.subs(q5,y[i][4])
    XYZ_m3.append(xyz_m3)
    
    xyz_m4=xyz_m4.subs(q2,y[i][0])
    xyz_m4=xyz_m4.subs(q1,y[i][1])
    xyz_m4=xyz_m4.subs(q3,y[i][2])
    xyz_m4=xyz_m4.subs(q4,y[i][3])
    xyz_m4=xyz_m4.subs(q5,y[i][4])
    XYZ_m4.append(xyz_m4)
    
    xyz_m5=xyz_m5.subs(q2,y[i][0])
    xyz_m5=xyz_m5.subs(q1,y[i][1])
    xyz_m5=xyz_m5.subs(q3,y[i][2])
    xyz_m5=xyz_m5.subs(q4,y[i][3])
    xyz_m5=xyz_m5.subs(q5,y[i][4])
    XYZ_m5.append(xyz_m5)
    
    xyz_m6=xyz_m6.subs(q2,y[i][0])
    xyz_m6=xyz_m6.subs(q1,y[i][1])
    xyz_m6=xyz_m6.subs(q3,y[i][2])
    xyz_m6=xyz_m6.subs(q4,y[i][3])
    xyz_m6=xyz_m6.subs(q5,y[i][4])
    XYZ_m6.append(xyz_m6)
 
#Joints trajectory   
tray=[]
for i in range(0,len(XYZ_m3)-1):
    #Scaling factor 0.5
    q_tray=[(y[i][0],y[i][1]),(XYZ_m3[i][0],(XYZ_m3[i][1])),
        (XYZ_m4[i][0],(XYZ_m4[i][1])),(XYZ_m5[i][0],(XYZ_m5[i][1])),
        (XYZ_m6[i][0],(XYZ_m6[i][1]))]
    tray.append(q_tray)
    
