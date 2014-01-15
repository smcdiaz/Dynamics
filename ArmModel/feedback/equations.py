# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:10:22 2013

@author: Santiago
"""
import numpy as np

class PD:
	"""
	Discrete PD control
	"""

	def __init__(self, P, D, Derivator=0):

		self.Kp=P
		self.Kd=D
		self.Derivator=Derivator
		
		self.set_point=[]
		self.error=[]

	def update(self,current_value):
      
          self.error = self.set_point - current_value.T
                
          P_value = [self.Kp * self.error[0,0], self.Kp * self.error[0,1],0] 
          P_value = np.matrix(P_value)
          
          D_param = self.error - self.Derivator
          
          D_value = [self.Kd * D_param[0,0], self.Kd * D_param[0,1],0]
          D_value = np.matrix(D_value)          
  
          self.Derivator = self.error
          
          PD = P_value + D_value
           
          return PD

	def setPoint(self,set_point):
		"""
		Initilize the setpoint of PD
		"""
		self.set_point = set_point
		

	def setDerivator(self, Derivator):
		self.Derivator = Derivator

	def setKp(self,P):
		self.Kp=P

	def setKd(self,D):
		self.Kd=D

	def getPoint(self):
		return self.set_point

	def getError(self):
		return self.error

	def getDerivator(self):
		return self.Derivator
  
######	Example	#########
#
"""
p=PD(3.0,1.2)
p.setPoint(5.0)
for i in range(50):
     pid = p.update(10)
     print pid
"""
#Simplified dynamic control equation
#T=Jlm6 * A * (Kp * (xdes-x) + Kv * (xddes-xd)) + g