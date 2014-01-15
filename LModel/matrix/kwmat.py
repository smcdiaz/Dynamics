# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:20:08 2013

@author: Santiago
"""

import jac_sym as js
from plant import Im3,Im4,Im5,Im6

#Rotational kinetic energy for m3
Kwe_m3=js.Jwm3.T*Im3*js.Jwm3

#Rotational kinetic energy for m4
Kwe_m4=js.Jwm4.T*Im4*js.Jwm4

#Rotational kinetic energy for m5
Kwe_m5=js.Jwm5.T*Im5*js.Jwm5

#Rotational kinetic energy for m3
Kwe_m6=js.Jwm6.T*Im6*js.Jwm6
