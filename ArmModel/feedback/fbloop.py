# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:11:22 2013

@author: Santiago
"""
import numpy as np
import sympy as sp
import dkyn_sym as dk
import ikyn_q as ik
from plant import q3,q4,q5,qd3,qd4,qd5
import dynamics as dy
import model as md
from trajectory import line
import equations as eq
from jacobian import Jlm6, Jlm6_dot
import control as ct
import matplotlib.pyplot as plt

tf=10.0
nstep=50
Kp=0.1
Kd=0.1
errorx=[]
errory=[]
mov=[]

#Initial arm status
q0=np.matrix([0.1,0,0])
qd0=np.matrix([0,0,0])
xy0=dk.coord_q6.subs({q3:q0[0,0],q4:q0[0,1],q5:q0[0,2]})
xy0=sp.matrix2numpy(xy0)
xy0=np.matrix(xy0)

#Target position
q_f=np.matrix([-0.1,-0.1,0.1])
#xy_f=np.matrix([0.600,0.0170])
xy_f=dk.coord_q6.subs({q3:q_f[0,0],q4:q_f[0,1],q5:q_f[0,2]})
xy_f=sp.matrix2numpy(xy_f)
xy_f=np.matrix(xy_f.T)
xyd_f=np.matrix((0,0))


#Straight line trajectory
traj=line(xy0[0,0],xy0[1,0],xy_f[0,0],xy_f[0,1],tf,nstep)
x=traj[0]
y=traj[1]
xd=traj[2]
yd=traj[3]


#First iteration
PD=eq.PD(Kp,Kd,1)    
PD.setKp(0.1)
PD.setKd(0.001)
ctl=ct.control(Kp,Kd)
qi=q0
qdi=qd0
xyi=xy0
xyd_des=np.matrix([0.01,0.01,0])
xydi=np.matrix([0,0,0])
xyddi=np.matrix([0,0,0])
O_des=np.matrix(np.cumsum(q_f))
Od_des=np.matrix(qd0)
T0=np.matrix([0,0,0]).T
error=1
count=0
for i in range(1,x.size-1):
#while (error>0.01):
    #Parameter update
    xy_des=np.matrix([x[0,i-1],y[0,i-1]])
    #print xyi    
    #xy_des=xy_f
    O_act=np.matrix(np.cumsum(qi))
    Od_act=np.matrix(np.cumsum(qdi))
    xy_act=np.matrix(xyi)
    xyd_act=np.matrix(xydi)
    print xy_act.T
    q_act=np.concatenate((qi.T,qdi.T),axis=0)
    #print xy_des.shape,xyd_des.shape,xy_act.shape,xyd_act.shape
    #PD compensation
    cmd=ctl.PD(xy_des[0,0],xy_des[0,1],O_des[0,0],
               xyd_des[0,0],xyd_des[0,1],Od_des[0,0],
               xy_act[0,0],xy_act[1,0],O_act[0,0],
               xyd_act[0,0],xyd_act[0,1],Od_act[0,0])
    #PD.setPoint(xy_des)
    #cmd=PD.update(xy_act)
    #T0=dy.T0(qi,q_f,Kd,qdi)
    T0=np.matrix([0,0,0])
    #SEA applied torque  
    T=dy.Inv_Dyn(q_act,-cmd,T0.T)
    #print T
    #SEA model
    (act_qpar,qdd_updt)=md.plnt(T,qi,qdi)  
    act_qpar=np.matrix(act_qpar)
    qdd_updt=np.matrix(qdd_updt)
    
    #Position and velocity feedback data
    q_updt=np.matrix([act_qpar[0,0],act_qpar[0,1],act_qpar[0,2]])
    qd_updt=np.matrix([act_qpar[0,3],act_qpar[0,4],act_qpar[0,5]])
    xy_updt=dk.coord_q6.subs({q3:q_updt[0,0],q4:q_updt[0,1],q5:q_updt[0,2]})
    jac_updt=Jlm6.subs({q3:q_updt[0,0],q4:q_updt[0,1],q5:q_updt[0,2]})
    jac_updt=sp.matrix2numpy(jac_updt)
    jac_updt=np.matrix(jac_updt)
    jac_dot_updt=Jlm6_dot.subs(({q3:q_updt[0,0],q4:q_updt[0,1],q5:q_updt[0,2],
                                 qd3:q_updt[0,0],qd4:q_updt[0,1],qd5:q_updt[0,2]}))
    jac_dot_updt=sp.matrix2numpy(jac_dot_updt)
    jac_dot_updt=np.matrix(jac_dot_updt)
    xyd_updt=jac_updt*qd_updt.T
    qi=q_updt
    qdi=qd_updt
    error1=np.matrix([xy_des[0,0]-xyi[0,0],xy_des[0,1]-xyi[1,0]])
    xyi=xy_updt
    xydi=xyd_updt.T
    xyddi=np.dot(jac_updt,qdd_updt)+np.dot(jac_dot_updt,qd_updt.T)
    T0=T
        
    #Trajectory
    mov.append(xy_updt)

    #Errors
    #error=np.max(np.abs(xy_des[0,0]-xy_updt.T[0,0]),np.abs(xy_des[0,1]-xy_updt.T[0,1]))
    
    errorx.append(error1[0,0])
    errory.append(error1[0,1])
    #print error1[0,0],error1[0,1]
    count=count+1
    if count>500:
        print 'End'
        break
    
X=[]
Y=[]
print xyi    
for i in range(0,len(mov)-1):
    X.append(mov[i][0])
    Y.append(mov[i][1])
plt.figure(1)
plt.plot(X,Y)    
    
plt.figure(2)
plt.plot(errorx)
plt.plot(errory)


