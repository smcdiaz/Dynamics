# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:31:43 2013

@author: Santiago
"""

from jac_sym import *
from imat import *
import sympy as sp

Js=Jlm3
Js=sp.nsimplify(Js)
NS=Js.nullspace()
print NS
