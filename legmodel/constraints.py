# -*- coding: utf-8 -*-
"""
Created on Sat Oct 05 05:23:56 2013

@author: Santiago
"""
from gmat import *
from ccmat import *
from sympy import *

"""
Constraints
     x=q2
     y=q1
"""
q1=Symbol('q1')
q2=Symbol('q2')

Jc11=0
Jc12=q2
Jc21=q1
Jc22=0
Jc=Matrix([[Jc11,Jc12],[Jc21,Jc22]])

Jc_T=Jc.inv()
#Lbd=Jc_T*
#Lbd=Matrix(Lbd)
print b.shape
print g.shape
C=Jc_T*(b+g)*Jc 
#*Lbd
print C