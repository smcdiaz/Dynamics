# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:55:57 2013

@author: Santiago
"""
#from imat import A
import numpy as np
import scipy.integrate as itg

Jsea=np.matrix([[3,0,0],[0,2,0],[0,0,1]])

def deriv(st,t,Tq):
    #u=np.matrix([st[0],st[1],st[2]]) 
    ud=np.matrix([st[3],st[4],st[5]])
    udd=np.matrix((np.linalg.inv(Jsea))*Tq)
    res=np.concatenate((ud.T,udd),axis=0)
    res=np.matrix(res.T)
    #print res
    return [res[0,0],res[0,1],res[0,2],res[0,3],res[0,4],res[0,5]]

def plnt(T,q,qd):
      
    st0=[q[0,0],q[0,1],q[0,2],qd[0,0],qd[0,1],qd[0,2]]
   # print st0
     # Times at which the solution is to be computed.
    t = np.linspace(0, 0.2,50)
    y = itg.odeint(deriv,st0,t,(T,))
    udd=np.matrix((np.linalg.inv(Jsea))*T)
    result=y[len(y[:,0])-1]
    #print result
    #print '----------------------------------------------------------'
    return result,udd
"""    
T=np.matrix([0.5,3,0.2])
qd=np.matrix([0,0,0])
qpar=plnt(T.T,qd)
"""