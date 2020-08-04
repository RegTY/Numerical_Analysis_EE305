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

	def __init__(self, numIterations=4, upper=0.8, lower=0):
		""" Initializes the class, by default the equation used will be 3Cos  x + 5Cos x with 10 iterations """
		self.upper = upper
		self.lower = lower
		self.numIterations = numIterations
		self.x = np.linspace(0, 10, 1000)
		self.h = (upper-lower)/numIterations

		#plt.ioff()
		#fig, ax = plt.subplots()
	
	def equation(self , x):
		#y =  0.2 + 25*x - 200*x**2 + 675*x**3 -900*x**4 +400*x**5
		y = 1/(1+x**5)
		return y
	
	# def differential(self, xval):
	# 	x = sp.symbols('x')
	# 	y = sp.Subs(sp.diff(self.equation(x) , x),x,xval).doit()
	# 	return y
 
	def trapezoidalRule(self, visualizer= False, tabular = False , x = None, y = None, b = None, a = None, n = 10):
		if tabular == True:
			n = len(x) - 1
			slicedy = y[1:n]
			I = (x[n]-x[0])*(y[0] + 2*np.sum(slicedy)+ y[n])/(2*n)
		else:
			h = (b-a)/n
			xi = h + a
			sumval = 0
			while xi < b:
				sumval += self.equation(xi)
				xi += self.h
			I = (b-a)*(self.equation(a) + 2*sumval+ self.equation(b))/(2*n)
		return I
	
	def simpson13(self, visualizer= False, tabular = False , x = None, y = None):

		if tabular == True:
			n = len(x) -1
			slicedodd = y[2:n:2]
			slicedeven = y[1:n:2]
			print(slicedeven)
			print(slicedodd)
			I = (x[n]-x[0])*(y[0] + 4*np.sum(slicedeven) +2*np.sum(slicedodd)+ y[n])/(3*n)
		else:
			n = self.numIterations
			b = self.upper
			a = self.lower
			xi = self.h + a
			xj = 2*self.h + a
			sumodd = 0
			sumeve = 0
			
			while xj < b-self.h:
				sumodd += self.equation(xj)
				xj += 2*self.h
			while xi<b:
					sumeve += self.equation(xi)
					xi += 2*self.h
			I = (b-a)*((self.equation(a) + 4*sumeve+ +2*sumodd + self.equation(b)) /(3*n))
			df = pd.DataFrame({
				'x' : [i for i in np.linspace(a,b,int((b-a)/self.h)+1)],
				'y' : [self.equation(x) for x in np.linspace(a,b,int((b-a)/self.h)+1)]
			})
			print(df)
		return I 

	def simpson38(self, visualizer= False, tabular = False , x = None, y = None):

		if tabular == True:
			n = len(x) -1
			slicedodd = y[2:n:2]
			slicedeven = y[1:n:2]
			print(slicedeven)
			print(slicedodd)
			I = (x[n]-x[0])*(y[0] + 4*np.sum(slicedeven) +2*np.sum(slicedodd)+ y[n])/(3*n)
		else:
			n = self.numIterations
			b = self.upper
			a = self.lower
			xi = self.h + a
			xj = 2*self.h + a
			sumodd = 0
			sumeve = 0
			
			while xj < b-self.h:
				sumodd += self.equation(xj)
				xj += 2*self.h
			while xi<b:
					sumeve += self.equation(xi)
					xi += 2*self.h
			I = (b-a)*((self.equation(a) + 4*sumeve+ +2*sumodd + self.equation(b)) /(3*n))
			df = pd.DataFrame({
				'x' : [i for i in np.linspace(a,b,int((b-a)/self.h)+1)],
				'y' : [self.equation(x) for x in np.linspace(a,b,int((b-a)/self.h)+1)]
			})
			print(df)
		return I 

	def rhomberg(self, j,k, B, A):
		I = np.empty((4,4),  dtype=np.float64)
		I[0][0] = self.trapezoidalRule(b =B,a =A, n=1) 
		I[0][1] = self.trapezoidalRule(b =B,a =A, n=2)
		I[0][2] = self.trapezoidalRule(b= B,a =A, n=4)
		I2 = I[j-1-1][k] + (I[j-1-1][k] - I[j-1-1][k-1-1 + 1])/3
		return  I2



if __name__ == "__main__":
	 data = ODE()
	 data.equation(5)
	 a = 0
	 b = 0.8
	 print(data.rhomberg(3,1, 1 ,0 ))


