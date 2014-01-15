# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 23:09:35 2013

@author: Santiago
"""

from plant import *
from jac_sym import *

p3=Matrix([0,m3*g0,0])
g3=Jlm3.T*p3

p4=Matrix([0,m4*g0,0])
g4=Jlm4.T*p4

p5=Matrix([0,m5*g0,0])
g5=Jlm5.T*p5

p6=Matrix([0,m6*g0,0])
g6=Jlm6.T*p6

#G vector
g=g3+g4+g5+g6
print g.shape