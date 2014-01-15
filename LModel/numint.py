# -*- coding: utf-8 -*-
"""
Created on Wed Oct 02 23:31:31 2013

@author: Santiago
"""
import numpy as np
from dkyn_sym import coord_m3,coord_m4,coord_m5,coord_m6
from sympy import *
from plant import *
from imat import *
from ccmat import b
#from constraints import C
from gmat import g
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Recursive callable function
def cal_fun(st, t, FUN):
    """Define the right-hand side of equation dy/dt = a*y"""
    FUN=FUN.subs(q3,st[0])
    FUN=FUN.subs(q4,st[1])
    FUN=FUN.subs(q5,st[2])     
    FUN=FUN.subs(qd3,st[3])
    FUN=FUN.subs(qd4,st[4])
    FUN=FUN.subs(qd5,st[5])        
    U=st[3]
    V=st[4]
    W=st[5]
    f = [st[0],st[1],st[2],U,V,W,FUN[0],FUN[1],FUN[2]]
    #print f
    return f

F3=Symbol('F3')
F4=Symbol('F4')
F5=Symbol('F5')
T3=Symbol('T3')
T4=Symbol('T4')
T5=Symbol('T5')
q=Matrix([q1,q2,q3])
qdd=Matrix([qdd3,qdd4,qdd5])
Fe=Matrix([F3,F4,F5])
T=Matrix([T3,T4,T5])

#T=(A*qdd)+b+g+C

# Times at which the solution is to be computed.
t = np.linspace(0, 7, 50)

# Solve the equation.
print ("Integrando...")
st0=[0.01,0.01,0.01,0,0,0]
print A.shape
deriv=A.inv()*(-g-b)

y = odeint(cal_fun,st0, t,(deriv,))
print y

#Substitution of angles in direct kynematics
XYZ_m3=[]
XYZ_m4=[]
XYZ_m5=[]
XYZ_m6=[]

for i in range(0,y.shape[0]-1):
    xyz_m3=coord_m3
    xyz_m4=coord_m4
    xyz_m5=coord_m5
    xyz_m6=coord_m6
    
    xyz_m3=xyz_m3.subs(q3,y[i][0])
    xyz_m3=xyz_m3.subs(q4,y[i][1])
    xyz_m3=xyz_m3.subs(q5,y[i][2])
    XYZ_m3.append(xyz_m3)
    
    xyz_m4=xyz_m4.subs(q3,y[i][0])
    xyz_m4=xyz_m4.subs(q4,y[i][1])
    xyz_m4=xyz_m4.subs(q5,y[i][2])
    XYZ_m4.append(xyz_m4)
    
    xyz_m5=xyz_m5.subs(q3,y[i][0])
    xyz_m5=xyz_m5.subs(q4,y[i][1])
    xyz_m5=xyz_m5.subs(q5,y[i][2])
    XYZ_m5.append(xyz_m5)
    
    xyz_m6=xyz_m6.subs(q3,y[i][0])
    xyz_m6=xyz_m6.subs(q4,y[i][1])
    xyz_m6=xyz_m6.subs(q5,y[i][2])
    XYZ_m6.append(xyz_m6)
 
#Joints trajectory   
tray=[]
for i in range(0,len(XYZ_m3)-1):
    #Scaling factor 0.5
    qd=[(XYZ_m3[i][0]*500,XYZ_m3[i][1]*500),(XYZ_m4[i][0]*500,
        (XYZ_m4[i][1])*500),(XYZ_m5[i][0]*500,(XYZ_m5[i][1])*500),
        (XYZ_m6[i][0]*500,(XYZ_m6[i][1])*500),(XYZ_m6[i][0]*500,((XYZ_m6[i][1])+100)*500)]
    tray.append(qd)