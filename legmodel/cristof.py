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
a111=diff(a[0,0],q1)
a112=diff(a[0,0],q2)
a113=diff(a[0,0],q3)
a114=diff(a[0,0],q4)
a115=diff(a[0,0],q5)

a121=diff(a[0,1],q1)
a122=diff(a[0,1],q2)
a123=diff(a[0,1],q3)
a124=diff(a[0,1],q4)
a125=diff(a[0,1],q5)

a131=diff(a[0,2],q1)
a132=diff(a[0,2],q2)
a133=diff(a[0,2],q3)
a134=diff(a[0,2],q4)
a135=diff(a[0,2],q5)

a141=diff(a[0,3],q1)
a142=diff(a[0,3],q2)
a143=diff(a[0,3],q3)
a144=diff(a[0,3],q4)
a145=diff(a[0,3],q5)

a151=diff(a[0,4],q1)
a152=diff(a[0,4],q2)
a153=diff(a[0,4],q3)
a154=diff(a[0,4],q4)
a155=diff(a[0,4],q5)

a211=diff(a[1,0],q1)
a212=diff(a[1,0],q2)
a213=diff(a[1,0],q3)
a214=diff(a[1,0],q4)
a215=diff(a[1,0],q5)

a221=diff(a[1,1],q1)
a222=diff(a[1,1],q2)
a223=diff(a[1,1],q3)
a224=diff(a[1,1],q4)
a225=diff(a[1,1],q5)

a231=diff(a[1,2],q1)
a232=diff(a[1,2],q2)
a233=diff(a[1,2],q3)
a234=diff(a[1,2],q4)
a235=diff(a[1,2],q5)

a241=diff(a[1,3],q1)
a242=diff(a[1,3],q2)
a243=diff(a[1,3],q3)
a244=diff(a[1,3],q4)
a245=diff(a[1,3],q5)

a251=diff(a[1,4],q1)
a252=diff(a[1,4],q2)
a253=diff(a[1,4],q3)
a254=diff(a[1,4],q4)
a255=diff(a[1,4],q5)

a311=diff(a[2,0],q1)
a312=diff(a[2,0],q2)
a313=diff(a[2,0],q3)
a314=diff(a[2,0],q4)
a315=diff(a[2,0],q5)

a321=diff(a[2,1],q1)
a322=diff(a[2,1],q2)
a323=diff(a[2,1],q3)
a324=diff(a[2,1],q4)
a325=diff(a[2,1],q5)

a331=diff(a[2,2],q1)
a332=diff(a[2,2],q2)
a333=diff(a[2,2],q3)
a334=diff(a[2,2],q4)
a335=diff(a[2,2],q5)

a341=diff(a[2,3],q1)
a342=diff(a[2,3],q2)
a343=diff(a[2,3],q3)
a344=diff(a[2,3],q4)
a345=diff(a[2,3],q5)

a351=diff(a[2,4],q1)
a352=diff(a[2,4],q2)
a353=diff(a[2,4],q3)
a354=diff(a[2,4],q4)
a355=diff(a[2,4],q5)

a411=diff(a[3,0],q1)
a412=diff(a[3,0],q2)
a413=diff(a[3,0],q3)
a414=diff(a[3,0],q4)
a415=diff(a[3,0],q5)

a421=diff(a[3,1],q1)
a422=diff(a[3,1],q2)
a423=diff(a[3,1],q3)
a424=diff(a[3,1],q4)
a425=diff(a[3,1],q5)

a431=diff(a[3,2],q1)
a432=diff(a[3,2],q2)
a433=diff(a[3,2],q3)
a434=diff(a[3,2],q4)
a435=diff(a[3,2],q5)

a441=diff(a[3,3],q1)
a442=diff(a[3,3],q2)
a443=diff(a[3,3],q3)
a444=diff(a[3,3],q4)
a445=diff(a[3,3],q5)

a451=diff(a[3,4],q1)
a452=diff(a[3,4],q2)
a453=diff(a[3,4],q3)
a454=diff(a[3,4],q4)
a455=diff(a[3,4],q5)

a511=diff(a[4,0],q1)
a512=diff(a[4,0],q2)
a513=diff(a[4,0],q3)
a514=diff(a[4,0],q4)
a515=diff(a[4,0],q5)

a521=diff(a[4,1],q1)
a522=diff(a[4,1],q2)
a523=diff(a[4,1],q3)
a524=diff(a[4,1],q4)
a525=diff(a[4,1],q5)

a531=diff(a[4,2],q1)
a532=diff(a[4,2],q2)
a533=diff(a[4,2],q3)
a534=diff(a[4,2],q4)
a535=diff(a[4,2],q5)

a541=diff(a[4,3],q1)
a542=diff(a[4,3],q2)
a543=diff(a[4,3],q3)
a544=diff(a[4,3],q4)
a545=diff(a[4,3],q5)

a551=diff(a[4,4],q1)
a552=diff(a[4,4],q2)
a553=diff(a[4,4],q3)
a554=diff(a[4,4],q4)
a555=diff(a[4,4],q5)
