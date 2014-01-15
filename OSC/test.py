# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:50:36 2013

@author: Santiago
"""

from scipy import *
from pylab import *    # Not needed if you use ipython -pylab
a = zeros(1000)
a[:100]=1
b = fft(a)
plot(abs(b))
show()    