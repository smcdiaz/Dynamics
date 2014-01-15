# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:21:42 2013

@author: Santiago
"""
import sympy as sp
from imat import A
import numpy as np
from jacobian import Jlm6
from plant import q3,q4,q5,qd3,qd4,qd5
import pseudoinv as ps

def mas_inv(mat,ang3,ang4,ang5,acc3,acc4,acc5):
    #Value substitution into mass matrix
    M=mat.subs({q3:ang3,q4:ang4,q5:ang5,qd3:acc3,qd4:acc4,qd5:acc5})
   
    #Conversion to numpy matrix
    M=sp.matrix2numpy(M)
    
    #matrix inversion    
    #Minv=np.linalg.inv(M)
     #Conversion to numpy matrix
    u,s,v = np.linalg.svd(M)
    if s[abs(s)<.0025].shape[0] == 0: 
        # if we're not near a singularity
        Minv = np.linalg.inv(M)
    else: 
        # in the case that the robot is near a singularity
        for i in range(len(s)):
            if s[i] < .0025: s[i] = 0
            else: s[i] = 1.0/float(s[i])
        Minv = np.dot(v, np.dot(np.diag(s), u.T))
        
    return M,Minv
    
def mass2lamb(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5):
    #Mass matrix
    (M,Minv)=mas_inv(mat,ang3,ang4,ang5,acc3,acc4,acc5)
 
    J=jac.subs({q3:ang3,q4:ang4,q5:ang5})
    J=sp.matrix2numpy(J)
    #Jacobian pseudoinverse    
    #jpsi=ps.jac_psi(jac,ang3,ang4,ang5,acc3,acc4,acc5)
       
    aux=np.dot(J,Minv)
    aux=np.dot(aux,J.T)
    #Lambda matrix
    u,s,v = np.linalg.svd(aux)
    if s[abs(s)<.0025].shape[0] == 0: 
        # if we're not near a singularity
        lmat = np.linalg.inv(aux)
    else: 
        # in the case that the robot is near a singularity
        for i in range(len(s)):
            if s[i] < .0025: s[i] = 0
            else: s[i] = 1.0/float(s[i])
        lmat = np.dot(v, np.dot(np.diag(s), u.T))

    
    #Lambda matrix inversion
    u,s,v = np.linalg.svd(lmat)
    if s[abs(s)<.00005].shape[0] == 0: 
        # if we're not near a singularity
        lmat_inv = np.linalg.inv(lmat)
    else: 
        # in the case that the robot is near a singularity
        for i in range(len(s)):
            if s[i] < .00005: s[i] = 0
            else: s[i] = 1.0/float(s[i])
        lmat_inv = np.dot(v, np.dot(np.diag(s), u.T))
    
    return lmat,lmat_inv
    
#(L,Li)=mass2lamb(A,Jlm6,0.2,0.2,0.2,0,0,0)

