# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:24:47 2013

@author: Santiago
"""
import sympy as sp
import numpy as np
from plant import q3, q4, q5, qd3, qd4, qd5
from imat import A
from jacobian import Jlm6
import lambmat as lm

def jac_psi(ang3,ang4,ang5,acc3,acc4,acc5):
    
    #Value substitution into product matrix
   
    mat=A.subs({q3:ang3,q4:ang4,q5:ang5,qd3:acc3,qd4:acc4,qd5:acc5})
    
    mult=np.dot(mat,mat.T)
 
    #Conversion to numpy matrix
    mat1=sp.matrix2numpy(mult)
    
    #Matrix inversion    
    Pinv=np.linalg.inv(mat1)
    
    #Jacobian pseudoinverse
    J_psi=np.dot(Pinv,mat1)

    return J_psi
  
def Jdc(ang3,ang4,ang5,acc3,acc4,acc5):
    (M,Minv)=lm.mas_inv(ang3,ang4,ang5,acc3,acc4,acc5)
    (L,Li)=lm.mass2lamb(ang3,ang4,ang5,acc3,acc4,acc5)
    jac=Jlm6.subs({q3:ang3,q4:ang4,q5:ang5,qd3:acc3,qd4:acc4,qd5:acc5})
    
    jdc=Minv*jac.T
    #Conversion to numpy matrix
    jdc=sp.matrix2numpy(jdc)
    jdc=np.matrix(jdc)  
    jdc=np.dot(jdc,L)
    
    return jdc
    
#jp=Jdc(A,Jlm6,0.2,0.2,0.2,1,1,1)
#print jp
#print jp.shape