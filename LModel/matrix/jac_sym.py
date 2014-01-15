# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:36:36 2013

@author: Santiago
"""
from dkyn_sym import *
from sympy import diff,Matrix

def jac_ij(fun,*args):
    res=diff(fun,*args)
    return res
    
#Jacobian for m3  
j11=jac_ij(x_m3,q3)
j12=jac_ij(x_m3,q4)
j13=jac_ij(x_m3,q5)
j21=jac_ij(y_m3,q3)
j22=jac_ij(y_m3,q4)
j23=jac_ij(y_m3,q5)
j31=jac_ij(z_m3,q3)
j32=jac_ij(z_m3,q4)
j33=jac_ij(z_m3,q5)
Jlm3=Matrix([[j11,j12,j13],[j21,j22,j23],[j31,j32,j33]])


#Jacobian for m4  
j11=jac_ij(x_m4,q3)
j12=jac_ij(x_m4,q4)
j13=jac_ij(x_m4,q5)
j21=jac_ij(y_m4,q3)
j22=jac_ij(y_m4,q4)
j23=jac_ij(y_m4,q5)
j31=jac_ij(z_m4,q3)
j32=jac_ij(z_m4,q4)
j33=jac_ij(z_m4,q5)
Jlm4=Matrix([[j11,j12,j13],[j21,j22,j23],[j31,j32,j33]])
   
#Jacobian for m5  
j11=jac_ij(x_m5,q3)
j12=jac_ij(x_m5,q4)
j13=jac_ij(x_m5,q5)
j21=jac_ij(y_m5,q3)
j22=jac_ij(y_m5,q4)
j23=jac_ij(y_m5,q5)
j31=jac_ij(z_m5,q3)
j32=jac_ij(z_m5,q4)
j33=jac_ij(z_m5,q5)
Jlm5=Matrix([[j11,j12,j13],[j21,j22,j23],[j31,j32,j33]])

#Jacobian for m6 
j11=jac_ij(x_m6,q3)
j12=jac_ij(x_m6,q4)
j13=jac_ij(x_m6,q5)
j21=jac_ij(y_m6,q3)
j22=jac_ij(y_m6,q4)
j23=jac_ij(y_m6,q5)
j31=jac_ij(z_m6,q3)
j32=jac_ij(z_m6,q4)
j33=jac_ij(z_m6,q5)
Jlm6=Matrix([[j11,j12,j13],[j21,j22,j23],[j31,j32,j33]])

#Rotational jacobian m3
Jwm3=Matrix([[0,0,0],[0,0,0],[1,1,1]])

#Rotational jacobian m4
Jwm4=Matrix([[0,0,0],[0,0,0],[0,1,1]])

#Rotational jacobian m3
Jwm5=Matrix([[0,0,0],[0,0,0],[0,0,1]])

#Rotational jacobian m6
Jwm6=Matrix([[0,0,0],[0,0,0],[0,0,0]])
