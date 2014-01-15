# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:57:43 2013

@author: Santiago
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:16:04 2013

@author: Santiago
"""

from plant import * 
from sympy import sin,cos


x_m3=L5*sin(q5)+L4*sin(q4+q5)+L3*sin(q3+q4+q5)+q2
y_m3=L6+L5*cos(q5)+L4*cos(q4+q5)+L3*cos(q3+q4+q5)+q1
z_m3=0
coord_q3=Matrix([x_m3,y_m3,z_m3])
     
x_m4=L5*sin(q5)+L4*sin(q4+q5)+q2
y_m4=L6+L5*cos(q5)+L4*cos(q4+q5)+q1
z_m4=0
coord_q4=Matrix([x_m4,y_m4,z_m4])

x_m5=L5*sin(q5)+q2
y_m5=L6+L5*cos(q5)+q1
z_m5=0
coord_q5=Matrix([x_m5,y_m5,z_m5])
        
x_m6=0+q2
y_m6=L6+q1
z_m6=0
coord_q6=Matrix([x_m6,y_m6,z_m6])