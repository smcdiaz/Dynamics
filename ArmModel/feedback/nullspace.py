# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:31:43 2013

@author: Santiago
"""

from jacobian import Jlm6
from imat import A
from pseudoinv import Jdc
import sympy as sp

def NS(mat,ang3,ang4,ang5,acc3,acc4,acc5):
    I=sp.Identity(3)
    I=sp.matrix2numpy(I)
    
    jdc=Jdc(A,Jlm6,ang3,ang4,ang5,acc3,acc4,acc5)

    jac=Jlm6.T
    #Value substitution into product jacrix
    jac=jac.subs(q3,ang3)
    jac=jac.subs(q4,ang4)  
    jac=jac.subs(q5,ang5) 
    jac=jac.subs(qd3,acc3)
    jac=jac.subs(qd4,acc4)
    jac=jac.subs(qd5,acc5)
    #Conversion to numpy matrix
    jac=sp.matrix2numpy(jac)
    
    ns=I-np.dot(jac,jdc)
    return ns
    
#nspace=NS(A,0.2,0.2,0.2,1,1,1)