# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:12:03 2013

@author: Santiago
"""
import numpy as np
from dkyn_q import coord_q3,coord_q4,coord_q5,coord_q6
from sympy import *
from plant import *
import pseudoinv as ps
from jacobian import *
from imat import A
from dynamics import Inv_Dyn
from scipy.integrate import odeint

qpar=[]

class OPSP:
    
        def __init__(self,q0,qd0):
            #Initial robot conditions
            self.q0=q0
            self.qd0=qd0
            self.qst0=np.vstack((self.q0,self.qd0))
            
            self.qst0.astype('float64')
            Td=np.array([0,0,0]) 
            Td=np.transpose(Td)
            
            jdc0=Jlm6.subs({q3:self.qst0[0,0],q4:self.qst0[0,1],q5:self.qst0[0,2],
                            qd3:self.qst0[1,0],qd4:self.qst0[1,1],qd5:self.qst0[1,2]})
            jdc0=matrix2numpy(jdc0)
            jdc0=np.matrix(jdc0)
            
            self.x0=coord_q6.subs({q3:self.q0[0,0],q4:self.q0[0,1],q5:self.q0[0,2]})
            self.x0=matrix2numpy(self.x0)
            
            self.xd0=np.array(np.dot(jdc0,self.qd0.T))
            self.xdd0=np.array(([0,0],))
            self.xst0=np.concatenate((self.xd0.T,self.xdd0),axis=1)
            
            self.st0=self.xst0
            
        
        def deriv(self,st, t, qpar):
            """Define the right-hand side of equation dy/dt = a*y"""
            #Resulting desired torque 
            Td=np.matrix([0,0,0])     
                        
            XDD=Inv_Dyn(qpar,Td)
            
            jdc=ps.Jdc(A,Jlm6,qpar[0],qpar[1],qpar[2],qpar[3],qpar[4],qpar[5])
            jdc_i=jdc**-1
            jdc_i=matrix2numpy(jdc_i.T)
            jdc_i=np.matrix(jdc_i)
            qdi=np.dot(jdc_i,XDD)

            qpar=[qpar[3],qpar[4],qpar[5],qdi[0],qdi[1],qdi[2]] 
            
            f = np.array([st[2],st[3],XDD[0,0],XDD[1,0]])
            
            return f
    
        def grad(self,st,t):

            jdc=ps.Jdc(A,Jlm6,self.st[0],self.st[1],self.st[2],
                       self.st[3],self.st[4],self.st[5])  
            
            return jdc
    
        def integ(self):
            # Times at which the solution is to be computed.
            t = np.linspace(0, 0.1, 10)
            
            # Numerical integration to obtain qdd
            print ("Integrating...")
            print self.st0.shape
            y = odeint(self.deriv,self.st0, t,(self.qst0,))
            #, Dfun=self.grad,rtol=0.01,atol=0.001,printmessg=1)
                       
            return y
            
           
q0=np.array(([0.1],[0.1],[0]))
qd0=np.array(([0],[0],[0]))          
op=OPSP(q0.T,qd0.T)
y=op.integ()  
X=y[:,0]
Y=y[:,1]
plt.plot(X)

