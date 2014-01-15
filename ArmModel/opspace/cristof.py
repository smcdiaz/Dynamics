# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:50:52 2013

@author: Santiago
"""
import imat as im
from plant import *
from sympy import diff,simplify,together

a=simplify(im.A)

#Simbolos de Cristofel
a111=diff(a[0,0],q3)
a112=diff(a[0,0],q4)
a113=diff(a[0,0],q5)

a121=diff(a[0,1],q3)
a122=diff(a[0,1],q4)
a123=diff(a[0,1],q5)

a131=diff(a[0,2],q3)
a132=diff(a[0,2],q4)
a133=diff(a[0,2],q5)

a211=diff(a[1,0],q3)
a212=diff(a[1,0],q4)
a213=diff(a[1,0],q5)

a221=diff(a[1,1],q3)
a222=diff(a[1,1],q4)
a223=diff(a[1,1],q5)

a231=diff(a[1,2],q3)
a232=diff(a[1,2],q4)
a233=diff(a[1,2],q5)

a311=diff(a[2,0],q3)
a312=diff(a[2,0],q4)
a313=diff(a[2,0],q5)

a321=diff(a[2,1],q3)
a322=diff(a[2,1],q4)
a323=diff(a[2,1],q5)

a331=diff(a[2,2],q3)
a332=diff(a[2,2],q4)
a333=diff(a[2,2],q5)
