import matplotlib
import sympy as sp
from matplotlib.widgets import Slider, Button
import seaborn as sns
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
sns.set(style="ticks")


class ODE:
	""" A class containing all the numerical methods for solving ODES"""

	def __init__(self, numIterations=4, upper=4, lower=0, stepsize = 0.5 , xinitial = 0, yinitial = 1):
		""" Initializes the class, by default the equation used will be 3Cos  x + 5Cos x with 10 iterations """
		self.upper = upper
		self.lower = lower
		self.xi = xinitial
		self.yi = yinitial
		self.numIterations = numIterations
		self.x = np.linspace(0, 10, 1000)
		self.h = stepsize

		#plt.ioff()
		#fig, ax = plt.subplots()
	
	def equation(self , x,y = 0):
		f =y - 2*x/y
		return f
	
	def euler(self):
		yi = self.yi 
		xi = self.xi
		i = 0
		while i < self.upper:
			yi1 =yi+ self.equation(xi,yi)*self.h
			xi += self.h
			yi = yi1
			print(f'xi is {xi}, yi is {yi}')
			i += self.h 
		return yi1

	def heun(self, n1=1):
		yi = self.yi
		xi = self.xi
		i = 0
		ypredict = yi+ self.equation(xi,yi)*self.h
		
		i = 0
		j = 0

		# yi = yi1
		# xi += self.h

		while j < self.upper:
			while i < n1 :
				yi1 = yi + (self.equation(xi,yi) + self.equation(xi + self.h,ypredict))/2*self.h
				ypredict = yi1
				i += 1
				#print(f"Y-predict  {ypredict} at {i} iteration")
			i = 0
			yi = yi1
			xi += self.h	
			ypredict = yi + self.equation(xi,yi)*self.h
			j += self.h
			# xi += self.h
			# yi = yi1
			print(f'yi {yi} at xi {xi} ')
		return yi	

	def RK2(self):
		xi = self.xi
		yi = self.yi
		h = self.h
		def incrementalfunction(xi,yi,h):
			k1 = self.equation(xi,yi)
			k2 = self.equation(xi+3/4*h,yi +3/4*k1*h)
			y = 1/3*k1 + 2/3*k2
			return y
		i = 0
		while i < self.upper:
			yi1 = yi + incrementalfunction(xi,yi,h)*h
			
			xi += self.h
			yi = yi1
			print(f'xi = {xi}, yi1 = {yi1}')
			i += self.h
		return yi1

	def RK3(self):
		xi = self.xi
		yi = self.yi
		h = self.h
		def incrementalfunction(xi,yi,h):
			k1 = self.equation(xi,yi)
			k2 = self.equation(xi + 1/2*h, yi + 1/2*k1*h)
			k3 = self.equation(xi+h, yi - k1*h +2*k2*h)
			y =  1/6*(k1 + 4*k2 + k3)
			
			return y
		i = 0
		while i < self.upper:
			yi1 = yi + incrementalfunction(xi,yi,h)*h
			
			xi += self.h
			yi = yi1
			print(f'xi = {xi}, yi1 = {yi1}')
			i += self.h
		return yi1
	def RK4(self):
		xi = self.xi
		yi = self.yi
		h = self.h
		def incrementalfunction(xi,yi,h):
			#print(xi)
			k1 = self.equation(xi,yi)
			k2 = self.equation(xi + 1/2*h, yi + 1/2*k1*h)
			k3 = self.equation(xi + 1/2*h, yi + 1/2*k2*h)
			k4 = self.equation(xi+h, yi + k3*h)
			y =  1/6*(k1 + 2*k2 + 2*k3 + k4)
			print(y)
			print(f" k1 {k1}, k2 {k2}, k3 {k3}, k4 {k4}")
			return y
		i = 0
		while i < self.upper:
			yi1 = yi + incrementalfunction(xi,yi,h)*h
			
			xi += self.h
			yi = yi1
			print(f'xi = {xi}, yi1 = {yi1}')
			i += self.h
		return yi1

	def RK5(self):
		xi = self.xi
		yi = self.yi
		h = self.h
		def incrementalfunction(xi,yi,h):
			k1 = self.equation(xi,yi)
			k2 = self.equation(xi + 1/4*h, yi + 1/4*k1*h)
			k3 = self.equation(xi + 1/4*h, yi + 1/8*k1*h + 1/8*k2*h)
			k4 = self.equation(xi +1/2*h , yi - 1/2*k2*h + k3*h)
			k5 = self.equation(xi+3/4*h, yi + 3/16*k1*h + 9/16*k4*h)
			k6 = self.equation(xi + h, yi - 3/7*k1*h +2/7*k2*h + 12/7*k3*h -12/7*k4*h +8/7*k5*h)
			y =  1/90*(7*k1 + 32*k3 + 12*k4 + 32*k5 + 7*k6)
			return y
		i = 0
		while i < self.upper:
			yi1 = yi + incrementalfunction(xi,yi,h)*h
			
			xi += self.h
			yi = yi1
			print(f'xi = {xi}, yi1 = {yi1}')
			i += self.h
		return yi1
if __name__ == "__main__":
	 data = ODE(upper = 0.2 , stepsize = 0.1 , xinitial = 0, yinitial = 1)
	 print(data.rk3())
	 #print(data.heun())


