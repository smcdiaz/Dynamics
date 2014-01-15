# -*- co0.5*(a111+a111-a111)ng: utf-8 -*-
"""
Created on Thu Sep 26 21:20:19 2013

@author: Santiago
"""

from plant import *
from cristof import *
from sympy import Matrix,simplify
from pseudoinv import Jdc


#Simbolos de Cristofel
b111=0.5*(a111+a111-a111)
b112=0.5*(a112+a121-a121)
b113=0.5*(a113+a131-a131)

b121=0.5*(a121+a112-a211)
b122=0.5*(a122+a122-a221)
b123=0.5*(a123+a132-a231)

b131=0.5*(a131+a113-a311)
b132=0.5*(a132+a123-a321)
b133=0.5*(a133+a133-a331)

b211=0.5*(a211+a211-a112)
b212=0.5*(a212+a221-a122)
b213=0.5*(a213+a231-a132)

b221=0.5*(a221+a212-a212)
b222=0.5*(a222+a222-a222)
b223=0.5*(a223+a232-a232)

b231=0.5*(a231+a213-a312)
b232=0.5*(a232+a223-a322)
b233=0.5*(a233+a233-a332)

b311=0.5*(a311+a311-a113)
b312=0.5*(a312+a321-a123)
b313=0.5*(a313+a331-a133)

b321=0.5*(a321+a312-a213)
b322=0.5*(a322+a322-a223)
b323=0.5*(a323+a332-a233)

b331=0.5*(a331+a313-a313)
b332=0.5*(a332+a323-a323)
b333=0.5*(a333+a333-a333)



#Centrifugal and Coriolis matrix
Bq=Matrix([[2*b112,2*b113,2*b123],
           [2*b212,2*b213,2*b223],
           [2*b312,2*b313,2*b323]])
           
Cq=Matrix([[b111,b122,b133],
           [b211,b222,b233],
           [b311,b322,b333]])
           
qdot2=Matrix([qd3*qd3,qd4*qd4,qd5*qd5])

qdqd=Matrix([qd3*qd4,qd3*qd5,qd4*qd5])

#Coriolix matrix in joint space
b=Bq*qdqd+Cq*qdot2

