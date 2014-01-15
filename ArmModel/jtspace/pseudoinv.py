# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:24:47 2013

@author: Santiago
"""
import lambmat as lm
import sympy as sp
import numpy as np
from plant import q3, q4, q5, qd3, qd4, qd5

def jac_psi(mat,ang3,ang4,ang5,acc3,acc4,acc5):
    #Value substitution into product matrix
   
    mat=mat.subs({q3:ang3,q4:ang4,q5:ang5,qd3:acc3,qd4:acc4,qd5:acc5})
    
    mult=mat*mat.T
    #print mult
    #Conversion to numpy matrix
    mat1=sp.matrix2numpy(mult)
    #Matrix inversion    
    Pinv=mat1**-1
  
    #Jacobian pseudoinverse
    J_psi=mat.T*Pinv

    return J_psi
  
def Jdc(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5):
    M_inv=lm.masinv(mat,ang3,ang4,ang5,acc3,acc4,acc5)
    (L,Li)=lm.mass2lamb(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5)
       
    jac=M_inv*jac.T
    #Value substitution into product jacrix
    jac=jac.subs({q3:ang3,q4:ang4,q5:ang5,qd3:acc3,qd4:acc4,qd5:acc5})
  
    #Conversion to numpy matrix
    jac=sp.matrix2numpy(jac)
    L=sp.matrix2numpy(L)
    
    jdc=np.dot(jac,L)
    return jdc
    
#jp=Jdc(A,Jlm6,0.2,0.2,0.2,1,1,1)
#print jp.shape