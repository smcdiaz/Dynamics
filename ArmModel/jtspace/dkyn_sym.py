# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:16:04 2013

@author: Santiago
"""

from plant import * 
from sympy import sin,cos

y_m6=L4*sin(q3)+L5*sin(q3+q4)+(L6-l6)*sin(q3+q4+q5)
x_m6=L3+L4*cos(q3)+L5*cos(q3+q4)+(L6-l6)*cos(q3+q4+q5)
z_m6=0
coord_q6=Matrix([x_m6,y_m6])
     
y_m5=L4*sin(q3)+(L5-l5)*sin(q3+q4)
x_m5=L3+L4*cos(q3)+L5*cos(q3+q4)
z_m5=0
coord_q5=Matrix([x_m5,y_m5])

y_m4=(L4-l4)*sin(q3)
x_m4=L3+(L4-l4)*cos(q3)
z_m4=0
coord_q4=Matrix([x_m4,y_m4])
        
y_m3=0
x_m3=L3-l3
z_m3=0
coord_q3=Matrix([x_m3,y_m3])