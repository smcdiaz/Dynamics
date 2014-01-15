# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:35:51 2013

@author: Santiago
"""
from sympy import Symbol, Matrix

# Links lengths milimeters
L3=100
L4=330
L5=300
L6=120
    
# Link COMs location from corresponding joint milimeters
l3=L3/2
l4=L4/2
l5=L5/2
l6=L6/2
 
# Links mass in kilograms
m3=1
m4=1
m5=1
m6=1

q1=Symbol('q1')
q2=Symbol('q2')
q3=Symbol('q3')
q4=Symbol('q4')
q5=Symbol('q5')

qd1=Symbol('qd1')
qd2=Symbol('qd2')
qd3=Symbol('qd3')
qd4=Symbol('qd4')
qd5=Symbol('qd5')

qdd1=Symbol('qdd1')
qdd2=Symbol('qdd2')
qdd3=Symbol('qdd3')
qdd4=Symbol('qdd4')
qdd5=Symbol('qdd5')

g0=10
    
#Rotational inertia of m3
Im3=Matrix([[0.1,0,0],[0,0.1,0],[0,0,0.1]])

#Rotational inertia of m4
Im4=Matrix([[0.1,0,0],[0,0.1,0],[0,0,0.1]])

#Rotational inertia of m5
Im5=Matrix([[0.1,0,0],[0,0.1,0],[0,0,0.1]])

#Rotational inertia of m6
Im6=Matrix([[0.1,0,0],[0,0.1,0],[0,0,0.1]])
    