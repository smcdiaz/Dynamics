# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:21:42 2013

@author: Santiago
"""
import sympy as sp
import numpy as np
from imat import A
from jacobian import Jlm6
from plant import *

def masinv(mat,ang3,ang4,ang5,acc3,acc4,acc5):
    #Value substitution into mass matrix
    mat=mat.subs(q3,ang3)
    mat=mat.subs(q4,ang4)  
    mat=mat.subs(q5,ang5) 
    mat=mat.subs(qd3,acc3)
    mat=mat.subs(qd4,acc4)
    mat=mat.subs(qd5,acc5)
    #Conversion to numpy matrix
    mat1=sp.matrix2numpy(mat)
    #matrix inversion    
    num_inv=mat1**-1
    return num_inv
    
def mass2lamb(mat,jac,ang3,ang4,ang5,acc3,acc4,acc5):
    
    num_inv=masinv(mat,ang3,ang4,ang5,acc3,acc4,acc5)
    lmat=jac*num_inv*jac.T
    
    #Value substitution into lambda matrix
    lmat=lmat.subs(q3,ang3)
    lmat=lmat.subs(q4,ang4)  
    lmat=lmat.subs(q5,ang5) 
    lmat=lmat.subs(qd3,acc3)
    lmat=lmat.subs(qd4,acc4)
    lmat=lmat.subs(qd5,acc5)
    #Conversion to numpy matrix
    mat2=sp.matrix2numpy(lmat)
    lmat_inv=mat2**-1
    
    return lmat,lmat_inv
    
#(L,Li)=mass2lamb(A,Jlm6,0.2,0.2,0.2,0,0,0)

