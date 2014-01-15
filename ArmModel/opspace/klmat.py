# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:05:30 2013

@author: Santiago
"""
from sympy import *
import jacobian as js
from plant import *
#Linear kinetic energy m3
Kle_m3=js.Jlm3.T*m3*js.Jlm3

#Linear kinetic energy m4
Kle_m4=m4*js.Jlm4.T*js.Jlm4

#Linear kinetic energy m5
Kle_m5=m5*js.Jlm5.T*js.Jlm5

#Linear kinetic energy m6
Kle_m6=m6*js.Jlm6.T*js.Jlm6

