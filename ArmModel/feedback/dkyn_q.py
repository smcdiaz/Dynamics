# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:57:43 2013

@author: Santiago
"""
from plant import * 
from sympy import sin,cos


y_m6=L4*sin(q3)+L5*sin(q3+q4)+L6*sin(q3+q4+q5)
x_m6=L3+L4*cos(q3)+L5*cos(q3+q4)+L6*cos(q3+q4+q5)
o_m6=q3+q4+q5
coord_q6=Matrix([x_m6,y_m6,o_m6])
     
y_m5=L4*sin(q3)+L5*sin(q3+q4)
x_m5=L3+L4*cos(q3)+L5*cos(q3+q4)
o_m5=q3+q4
coord_q5=Matrix([x_m5,y_m5,o_m5])

y_m4=L4*sin(q3)
x_m4=L3+L4*cos(q3)
o_m4=q3
coord_q4=Matrix([x_m4,y_m4,o_m4])
        
y_m3=0
x_m3=L3
o_m3=0
coord_q3=Matrix([x_m3,y_m3,o_m3])