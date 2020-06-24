
import matplotlib
import sympy
from matplotlib.widgets import Slider,Button
import seaborn as sns
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
sns.set(style="ticks")


class graphical1:
	""" A graphical class which will contain all the different graphical methods of finding roots"""

	def __init__(self, equation = 1 , numIterations = 10, upper = 5, lower = 1, deltax = None ):
		""" Initializes the class, by default the equation used will be 3Cos  x + 5Cos x with 10 iterations """
		self.upper = upper
		self.lower = lower
		self.numIterations = numIterations
		self.x =np.linspace(0, 10 ,1000)
		self.deltax = deltax

	def equationf(self, x):
		""" The F(x) function to which the calculation will be operated under"""
		f = np.exp(-x) - x
		return f	
	# def equationf2(x):
	# 	""" The F(x) function to which the calculation will be operated under"""
	# 	f = 3*x**2 - 25*x - 2
	# 	return f

	# def equationf3(x):
	# 	""" The F(x) function to which the calculation will be operated under"""
	# 	g = 9.81
	# 	m = 68.1
	# 	t = 10
	# 	v = 40
	# 	f = ((g*m)/x)*(1-np.exp(-(x/m)*t))-v
	# 	return f

	def falsePosition(self):
		# Plotting settings
		# Figure is the "window" of the plot, with size 8 and 8, what is the unit? idk i just change until its nice
		fig= plt.figure(figsize=(8,8))

		# ax or axes in matlab term is the "plot" or "image" in the figure, so you can have a figure with 8 plots called axes (different from axis)
		ax = plt.subplot()


		# Spines in matlab term pretty much means like "edge line" or "axis lines" of the plot, so like the "top line, bottom like etc"
		#I made the top and right line invisible so we will only have 2 lines which will be the x and y axis
		# i set the position of the line to be at 0,0 cuz origin
		ax.spines['left'].set_position(('data', 0))
		ax.spines['bottom'].set_position(('data', 0))
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)


		# our boundaries

		xlower = self.lower
		xupper = self.upper

		#This time i want to plot the equation of like so Y = mX + C , where m is gradient and C is y-intercept

		# finding y1, and y2 so that i can use to find gradient
		y1 = self.equationf(xlower) # f(Xl)
		y2 = self.equationf(xupper) # f(Xu)

		# Finding the gradient here
		m = (y1-y2)/(xlower-xupper) # gradient

		# Finds the Y-intercept C based on the equation (y1-y2) = m(x1-x2)
		# So expanding that equation will get y1 -y2 = m*x1 - m*x2
		# Since its y- intercept, x1 = 0
		#  y1 = -m*x2 - y2

		# Since formula for c from Y = mX + c when X =0 is C = Y
		# Therefore C = y1 = -m*X2 - y2
		# Math in programming


		C = -m*xupper + y2
		y = m*self.x + C # Equation of line


		# This is the Xr equation from the notes, is derived from the gradient formula
		xmid = xupper - (y2*(xlower-xupper))/(y1-y2)

		# Main Equation Line
		line1, = plt.plot(self.x,self.equationf(self.x) ,label="Sin 10x + Cos3x")

		# This plots the equation of line between the 2 points,
		lineeqn, = plt.plot(self.x, y, label = "Equation of line")

		# This plots the XL and Xu point but show them with respect to on the curve so you can see it better
		lowerpointoncurve,= plt.plot(xlower, self.equationf(xlower), label="Lower Boundary on Curve",marker='o', markerfacecolor='red', markersize=6)
		upperpointoncurve, = plt.plot(xupper, self.equationf(xupper), label="Upper Boundary on Curve",marker='o', markerfacecolor='orange', markersize=6)

		# The usual 3 big boi points
		lowerpoint,= plt.plot(xlower, 0, label="Lower Boundary",marker='o', markerfacecolor='red', markersize=6)
		upperpoint, = plt.plot(xupper, 0, label="Upper Boundary", marker='o', markerfacecolor='orange', markersize=6)
		midpoint, = plt.plot(xmid, 0, label="Mid Point", marker='o', markerfacecolor='blue', markersize=6)



		# Labels the axis, title and show the legend
		plt.title("False Position Method")
		plt.ylabel("Y axis")
		plt.xlabel("X axis")
		plt.legend()




		# slider functionality
		# This create the slider axe, (again remember that an axe is pretty much like a "plot" or "image" on a figure)
		# The first 2 numbers are like the where the left and bottom part of the slider starts, so 0.1 and 0.01 so its pretty low
		# the last 2 numer is the width and height of the slider
		axSlider1 = plt.axes([0.3,0.01,0.4, 0.05])

		# this line will turn the axe into an actual slider instead of a blank "plot" or image"
		# If you want to icnrease the total number of iteration available change valmax
		iterationSlider = Slider(axSlider1, "# of iterations", valmin = 1, valmax = 10, valinit = 1, valstep = 1)



		# This is the function that the slider will use when you change the slider value, will be explained later
		# What this function do is like what you read in the textbook the f(xl)*f(xu) < 0 and blah blah rule



		def newPoint(val):
			iteration = int(iterationSlider.val)
			xlownew = self.lower
			xupnew = self.upper
			xmid = xupnew - (self.equationf(xupnew)*(xlownew-xupnew))/(self.equationf(xlownew)-self.equationf(xupnew))

			y1new = self.equationf(xlownew)
			y2new = self.equationf(xupnew)

			m = (y1new-y2new)/(xlownew-xupnew) 
			C = -m*xupnew + y2new
			y = m*self.x + C # Equation of line
			
			
			# Based on the # of iteration you choose, this will do the condition process n times
			# so if you choose 2 iterations, it does the calculation 2 times
			for i in range(1,iteration):
				
				# This is the f(xl)*f(xu) condition checker from the textbook
				check = self.equationf(xlownew)*self.equationf(xmid)
				
				# this is condition one from the notes, if f(xl)*f(xu)  > 0, set your Xl = Xr
				if check>0:
					print(f"f(Xl)*f(Xr) = {check} > 0,")
					
					# Based on condition, change Xl, and update everything
					xlownew = xmid
					
					# New value of y1 and y2 for gradient and xr calc
					y1new = self.equationf(xlownew)
					y2new = self.equationf(xupnew)

					# calculate new Xr value
					xmid = xupnew - (y2new*(xlownew-xupnew))/(y1new-y2new)
					
					# Calculates new values of C and M to make new equation of line
					m = (y1new-y2new)/(xlownew-xupnew)
					C = -m*xupnew + y2new
					y = m*self.x + C 
				
				# this is condition one from the notes, if f(xl)*f(xu)  < 0, set your Xu = Xr
				elif check<0:
					
					print(f"f(Xl)*f(Xr) = {check} < 0,")
					
					# Based on condition, change Xl, and update everything
					xupnew = xmid
					
					# New value of y1 and y2 for gradient and xr calc
					y1new = self.equationf(xlownew)
					y2new = self.equationf(xupnew)
					xmid =  xupnew - (y2new*(xlownew-xupnew))/(y1new-y2new)
					
					# calculate new Xr value
					m = (y1new-y2new)/(xlownew-xupnew)
					C = -m*xupnew + y2new
					y = m*self.x + C 
			
			# Once everything is done, update the points with the new x values 
			lowerpoint.set_xdata(xlownew)
			upperpoint.set_xdata(xupnew)
			midpoint.set_xdata(xmid)

			# Same thing update the x and y values of the new points
			lowerpointoncurve.set_xdata(xlownew)
			lowerpointoncurve.set_ydata(y1new)
			upperpointoncurve.set_xdata(xupnew)
			upperpointoncurve.set_ydata(y2new)

			# Update the equation of line with the new equation
			lineeqn.set_ydata(y)
			# Redraw everything
			plt.draw()



		# So iterationSlider is what i call my slider object, and the .on_changed() will be what the slider will do when it changed
		# the format is like this   sliderName.on_changed(Functiontocall)
		# Meaning when i change my slider values, so when it changes, it calls the function newPoint() that i did.
		iterationSlider.on_changed(newPoint)

		# Finally show all the things, plot, sliders, and etc
		plt.show()






	def bracketing(self):
		# Plotting settings
		# Figure is the "window" of the plot, with size 8 and 8, what is the unit? idk i just change until its nice
		fig= plt.figure(figsize=(8,8))

		# ax or axes in matlab term is the "plot" or "image" in the figure, so you can have a figure with 8 plots called axes (different from axis)
		ax = plt.subplot()


		# Spines in matlab term pretty much means like "edge line" or "axis lines" of the plot, so like the "top line, bottom like etc"
		#I made the top and right line invisible so we will only have 2 lines which will be the x and y axis
		# i set the position of the line to be at 0,0 cuz origin
		ax.spines['left'].set_position(('data', 0))
		ax.spines['bottom'].set_position(('data', 0))
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)





		# Plots the equation and names the thing "line1" for coding variable, 
		# format of code is plt.plot( x, y, label= "bla blah blah" , color = " blah blah blah" ) etc

		xlower = self.lower
		xupper = self.upper
		xmid = (xupper + xlower)/2


		# Plots the equation and points and names the thing "line1, lowerpoint and etc" for coding variable, 
		# format of code is plt.plot( x, y, label= "bla blah blah" , color = " blah blah blah" ) etc


		line1, = plt.plot(self.x,self.equationf(self.x) ,label="Parachutist Equation")
		lowerpoint,= plt.plot(xlower, 0, label="Lower Boundary",marker='o', markerfacecolor='red', markersize=6)
		upperpoint, = plt.plot(xupper, 0, label="Upper Boundary", marker='o', markerfacecolor='orange', markersize=6)
		midpoint, = plt.plot(xmid, 0, label="Mid Point", marker='o', markerfacecolor='blue', markersize=6)




		# Labels the axis, title and show the legend
		plt.title("Bracketing Method")
		plt.ylabel("Y axis")
		plt.xlabel("X axis")
		plt.legend()



		# slider functionality
		# This create the slider axe, (again remember that an axe is pretty much like a "plot" or "image" on a figure)
		# The first 2 numbers are like the where the left and bottom part of the slider starts, so 0.1 and 0.01 so its pretty low
		# the last 2 numer is the width and height of the slider

		axSlider1 = plt.axes([0.3,0.01,0.4, 0.05])

		# this line will turn the axe into an actual slider instead of a blank "plot" or image"
		iterationSlider = Slider(axSlider1, "# of iterations", valmin = 1, valmax = self.numIterations, valinit = 1, valstep = 1)



		# This is the function that the slider will use when you change the slider value, will be explained later
		# What this function do is like what you read in the textbook the f(xl)*f(xu) < 0 and blah blah rule


		def newPoint(val):
			#Sets the iteration value as whatever the value you set the slider at
			iteration = int(iterationSlider.val)
			
			# Creates local variable that is used in the function only
			xlower = self.lower
			xupper = self.upper
			xmid = (xlower+xupper)/2
			
			
			# Based on the # of iteration you choose, this will do the condition process n times
			# so if you choose 2 iterations, it does the calculation 2 times
			for i in range(1,iteration):
				# This is the f(xl)*f(xu) equation, so i put that value as check
				check = self.equationf(xlower)*self.equationf(xmid)
				
				# this is condition one from the notes, if f(xl)*f(xu)  > 0, set your Xl = Xr
				if check>0:
					# This print is for me to check the values to make sure everything makes sense
					print(f"f(Xl)*f(Xr) = {check} > 0")
					print("So Xl = Xr")
					
					# Applying the condition
					xlower = xmid
						
					# calculate new value of mid
					xmid = (xupper + xlower)/2
				# This one is if f(xl)*f(xu)  < 0, so Xu = Xr
				elif check<0:
					print(f"f(Xl)*f(Xr) = {check} < 0")
					print("So Xu = Xr")
					# turning Xu = Xr      
					xupper = xmid
					# Calculate new value
					xmid = (xupper + xlower)/2

			# After everything is done, update the values of Xu, Xr and stuff to all the plots
			# Like updating the x coordinate for the lower point, mid point and etc
			lowerpoint.set_xdata(xlower)
			upperpoint.set_xdata(xupper)
			midpoint.set_xdata(xmid)
			# Draw the plot again
			plt.draw()


		# So iterationSlider is what i call my slider object, and the .on_changed() will be what the slider will do when it changed
		# the format is like this   sliderName.on_changed(Functiontocall)
		# Meaning when i change my slider values, so when it changes, it calls the function newPoint() that i did.
		iterationSlider.on_changed(newPoint)

		# Finally show all the things, plot, sliders, and etc
		plt.show()

class graphical12:
	""" A graphical class which will contain all the different graphical methods of finding roots"""

	def __init__(self, equation = 1 , numIterations = 10, back =1, initial = 4, deltax = 0.01 ):
		""" Initializes the class, by default the equation used will be 3Cos  x + 5Cos x with 10 iterations """
		self.back = back
		self.initial = initial
		self.numIterations = numIterations
		self.x =np.linspace(0, 10 ,1000)
		self.deltax = deltax

	def equationf(self, x):
		""" The F(x) function to which the calculation will be operated under"""
		f = np.exp(x)*np.sin(x)-1
		return f
	def derivative(self,x):
		f =  -np.exp(-x) - 1
		return f	
	# def equationf2(x):
	# 	""" The F(x) function to which the calculation will be operated under"""
	# 	f = 3*x**2 - 25*x - 2
	# 	return f

	# def equationf3(x):
	# 	""" The F(x) function to which the calculation will be operated under"""
	# 	g = 9.81
	# 	m = 68.1
	# 	t = 10
	# 	v = 40
	# 	f = ((g*m)/x)*(1-np.exp(-(x/m)*t))-v
	# 	return f



	def newtonRaphson(self):
		""" The newton Raphson Method of finding the roots of a numerical graph."""
		# Plotting settings
		# Figure is the "window" of the plot, with size 8 and 8, what is the unit? idk i just change until its nice
		fig= plt.figure(figsize=(8,8))

		# ax or axes in matlab term is the "plot" or "image" in the figure, so you can have a figure with 8 plots called axes (different from axis)
		ax = plt.subplot()

		ax.set_ylim([-1.5,2])

		#ax.set_xlim([0,2])
		# Spines in matlab term pretty much means like "edge line" or "axis lines" of the plot, so like the "top line, bottom like etc"
		#I made the top and right line invisible so we will only have 2 lines which will be the x and y axis
		# i set the position of the line to be at 0,0 cuz origin
		ax.spines['left'].set_position(('data', 0))
		ax.spines['bottom'].set_position(('data', 0))
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)



		# Initial Val

		initialval = self.initial

		#This time i want to plot the equation of like so Y = mX + C , where m is gradient and C is y-intercept

		# finding y1 so that i can use to find gradient
		y1 = self.equationf(initialval)

		# Finding the gradient here
		m = self.derivative(initialval) # gradient

		# Finds the Y-intercept C based on the equation (y1-y2) = m(x1-x2)
		# So expanding that equation will get y1 -y2 = m*x1 - m*x2
		# Since its y- intercept, x1 = 0
		#  y1 = -m*x2 - y2

		# Since formula for c from Y = mX + c when X =0 is C = Y
		# Therefore C = y1 = -m*X2 - y2
		# Math in programming

		nextval = initialval - y1/m

		C = -m*nextval

		y = m*self.x + C # Equation of line

		# Main Equation Line
		line1, = plt.plot(self.x,self.equationf(self.x) ,label="Function")

		# This plots the equation of line between the 2 points,
		lineeqn, = plt.plot(self.x, y, label = "Equation of line")

		# This plots the XL and Xu point but show them with respect to on the curve so you can see it better
		initialpointoncurve,= plt.plot(initialval, self.equationf(initialval), label="Initial Point on Curve",marker='o', markerfacecolor='red', markersize=6)
		nextpointoncurve, = plt.plot(nextval, self.equationf(nextval), label="Next Point on Curve",marker='o', markerfacecolor='orange', markersize=6)

		# The usual 3 big boi points
		firstpoint,= plt.plot(initialval, 0, label="Initial Point",marker='o', markerfacecolor='red', markersize=6)
		nextpoint, = plt.plot(nextval, 0, label="Final Point", marker='o', markerfacecolor='orange', markersize=6)



		# Labels the axis, title and show the legend
		plt.title("Newton- Raphson Method")
		plt.ylabel("Y axis")
		plt.xlabel("X axis")
		plt.legend()




		# slider functionality
		# This create the slider axe, (again remember that an axe is pretty much like a "plot" or "image" on a figure)
		# The first 2 numbers are like the where the left and bottom part of the slider starts, so 0.1 and 0.01 so its pretty low
		# the last 2 numer is the width and height of the slider
		axSlider1 = plt.axes([0.3,0.01,0.4, 0.05])

		# this line will turn the axe into an actual slider instead of a blank "plot" or image"
		# If you want to icnrease the total number of iteration available change valmax
		iterationSlider = Slider(axSlider1, "# of iterations", valmin = 1, valmax = 10, valinit = 1, valstep = 1)



		# This is the function that the slider will use when you change the slider value, will be explained later
		# What this function do is like what you read in the textbook the f(xl)*f(xu) < 0 and blah blah rule



		def newPoint(val):
			iteration = int(iterationSlider.val)
			initialval = self.initial
			y1 = self.equationf(initialval)
			m = self.derivative(initialval)
			nextval = initialval - y1/m
			C = -m*nextval
			y = m*self.x + C 
			# Based on the # of iteration you choose, this will do the condition process n times
			# so if you choose 2 iterations, it does the calculation 2 times
			for i in range(1,iteration):
				initialval = nextval
				y1 = self.equationf(initialval)
				m = self.derivative(initialval)
				nextval = initialval - y1/m
				C = -m*nextval
				y = m*self.x + C 
			# Once everything is done, update the points with the new x values 
			print(f"X value is {initialval}")
			firstpoint.set_xdata(initialval)
			nextpoint.set_xdata(nextval)

			# Same thing update the x and y values of the new points
			initialpointoncurve.set_xdata(initialval)
			initialpointoncurve.set_ydata(self.equationf(initialval))
			nextpointoncurve.set_xdata(nextval)
			nextpointoncurve.set_ydata(self.equationf(nextval))

			# Update the equation of line with the new equation
			lineeqn.set_ydata(y)
			# Redraw everything
			plt.draw()
			



		# So iterationSlider is what i call my slider object, and the .on_changed() will be what the slider will do when it changed
		# the format is like this   sliderName.on_changed(Functiontocall)
		# Meaning when i change my slider values, so when it changes, it calls the function newPoint() that i did.
		iterationSlider.on_changed(newPoint)

		# Finally show all the things, plot, sliders, and etc
		plt.show()



	def Secant(self):
		# Plotting settings
		# Figure is the "window" of the plot, with size 8 and 8, what is the unit? idk i just change until its nice
		fig= plt.figure(figsize=(8,8))

		# ax or axes in matlab term is the "plot" or "image" in the figure, so you can have a figure with 8 plots called axes (different from axis)
		ax = plt.subplot()

		ax.set_ylim([-20,20])
		# Spines in matlab term pretty much means like "edge line" or "axis lines" of the plot, so like the "top line, bottom like etc"
		#I made the top and right line invisible so we will only have 2 lines which will be the x and y axis
		# i set the position of the line to be at 0,0 cuz origin
		ax.spines['left'].set_position(('data', 0))
		ax.spines['bottom'].set_position(('data', 0))
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)



		# Initial Val

		initialval = self.initial
		backval = self.back

		#This time i want to plot the equation of like so Y = mX + C , where m is gradient and C is y-intercept

		# finding y1 so that i can use to find gradient
		y0 = self.equationf(backval)
		y1 = self.equationf(initialval)

		newval = initialval - (y1*(backval - initialval))/(y0-y1)

		# Finding the gradient here
		m = (y0-y1)/(backval-initialval) # gradient

		# Finds the Y-intercept C based on the equation (y1-y2) = m(x1-x2)
		# So expanding that equation will get y1 -y2 = m*x1 - m*x2
		# Since its y- intercept, x1 = 0
		#  y1 = -m*x2 - y2

		# Since formula for c from Y = mX + c when X =0 is C = Y
		# Therefore C = y1 = -m*X2 - y2
		# Math in programming


		C = -m*newval

		y = m*self.x + C # Equation of line

		# Main Equation Line
		line1, = plt.plot(self.x,self.equationf(self.x) ,label="Function")

		# This plots the equation of line between the 2 points,
		lineeqn, = plt.plot(self.x, y, label = "Equation of line")

		# This plots the XL and Xu point but show them with respect to on the curve so you can see it better
		backpointoncurve, = plt.plot(backval, self.equationf(backval), label="Back Point on Curve",marker='o', markerfacecolor='green', markersize=6)
		initialpointoncurve,= plt.plot(initialval, self.equationf(initialval), label="Initial Point on Curve",marker='o', markerfacecolor='red', markersize=6)
		nextpointoncurve, = plt.plot(newval,self.equationf(newval), label="Next Point on Curve",marker='o', markerfacecolor='orange', markersize=6)

		# The usual 3 big boi points
		backpoint,= plt.plot(backval, 0, label="Initial Point",marker='o', markerfacecolor='green', markersize=6)
		firstpoint,= plt.plot(initialval, 0, label="Initial Point",marker='o', markerfacecolor='red', markersize=6)
		nextpoint, = plt.plot(newval, 0, label="Final Point", marker='o', markerfacecolor='orange', markersize=6)



		# Labels the axis, title and show the legend
		plt.title("Secant Method")
		plt.ylabel("Y axis")
		plt.xlabel("X axis")
		plt.legend()




		# slider functionality
		# This create the slider axe, (again remember that an axe is pretty much like a "plot" or "image" on a figure)
		# The first 2 numbers are like the where the left and bottom part of the slider starts, so 0.1 and 0.01 so its pretty low
		# the last 2 numer is the width and height of the slider
		axSlider1 = plt.axes([0.3,0.01,0.4, 0.05])

		# this line will turn the axe into an actual slider instead of a blank "plot" or image"
		# If you want to icnrease the total number of iteration available change valmax
		iterationSlider = Slider(axSlider1, "# of iterations", valmin = 1, valmax = 10, valinit = 1, valstep = 1)



		# This is the function that the slider will use when you change the slider value, will be explained later
		# What this function do is like what you read in the textbook the f(xl)*f(xu) < 0 and blah blah rule



		def newPoint(val):
			iteration = int(iterationSlider.val)
			initialval = self.initial
			backval = self.back

			y0 = self.equationf(backval)
			y1 = self.equationf(initialval)
			newval =initialval - (y1*(backval - initialval))/(y0-y1)
			m = (y0-y1)/(backval-initialval)
			C = -m*newval
			y = m*self.x + C
			# Based on the # of iteration you choose, this will do the condition process n times
			# so if you choose 2 iterations, it does the calculation 2 times
			for i in range(1,iteration):
				backval = initialval
				initialval = newval
				y0 = self.equationf(backval)
				y1 = self.equationf(initialval)
				newval = initialval - (y1*(backval - initialval))/(y0-y1)
				m = (y0-y1)/(backval-initialval)
				C = -m*newval
				y = m*self.x + C
			print(f"the X value is {initialval}")
			# Once everything is done, update the points with the new x values 
			firstpoint.set_xdata(initialval)
			nextpoint.set_xdata(newval)
			backpoint.set_xdata(backval)
			# Same thing update the x and y values of the new points
			initialpointoncurve.set_xdata(initialval)
			initialpointoncurve.set_ydata(self.equationf(initialval))
			nextpointoncurve.set_xdata(newval)
			nextpointoncurve.set_ydata(self.equationf(newval))
			backpointoncurve.set_xdata(backval)
			backpointoncurve.set_ydata(self.equationf(backval))
			
			
			# Update the equation of line with the new equation
			lineeqn.set_ydata(y)
			# Redraw everything
			plt.draw()



		# So iterationSlider is what i call my slider object, and the .on_changed() will be what the slider will do when it changed
		# the format is like this   sliderName.on_changed(Functiontocall)
		# Meaning when i change my slider values, so when it changes, it calls the function newPoint() that i did.
		iterationSlider.on_changed(newPoint)

		# Finally show all the things, plot, sliders, and etc
		plt.show()



	def modifiedSecant(self):
		""" Modified Secant Method of finding roots"""
		# Plotting settings
		# Figure is the "window" of the plot, with size 8 and 8, what is the unit? idk i just change until its nice
		fig= plt.figure(figsize=(8,8))

		# ax or axes in matlab term is the "plot" or "image" in the figure, so you can have a figure with 8 plots called axes (different from axis)
		ax = plt.subplot()

		ax.set_ylim([-20,20])
		# Spines in matlab term pretty much means like "edge line" or "axis lines" of the plot, so like the "top line, bottom like etc"
		#I made the top and right line invisible so we will only have 2 lines which will be the x and y axis
		# i set the position of the line to be at 0,0 cuz origin
		ax.spines['left'].set_position(('data', 0))
		ax.spines['bottom'].set_position(('data', 0))
		ax.spines['top'].set_visible(False)
		ax.spines['right'].set_visible(False)



		# Initial Val

		initialval = self.initial
		deltaval = self.deltax

		#This time i want to plot the equation of like so Y = mX + C , where m is gradient and C is y-intercept

		# finding y1 so that i can use to find gradient
		y0 = self.equationf(initialval + deltaval*initialval)
		y1 = self.equationf(initialval)

		newval = self.initial - (deltaval*initialval*y1)/(y0-y1)

		# Finding the gradient here
		m = (y0-y1)/(deltaval) # gradient

		# Finds the Y-intercept C based on the equation (y1-y2) = m(x1-x2)
		# So expanding that equation will get y1 -y2 = m*x1 - m*x2
		# Since its y- intercept, x1 = 0
		#  y1 = -m*x2 - y2

		# Since formula for c from Y = mX + c when X =0 is C = Y
		# Therefore C = y1 = -m*X2 - y2
		# Math in programming


		C = -m*newval

		y = m*self.x + C # Equation of line

		# Main Equation Line
		line1, = plt.plot(self.x,self.equationf(self.x) ,label="Function")

		# This plots the equation of line between the 2 points,
		lineeqn, = plt.plot(self.x, y, label = "Equation of line")

		# This plots the XL and Xu point but show them with respect to on the curve so you can see it better
		initialpointoncurve,= plt.plot(initialval, self.equationf(initialval), label="Initial Point on Curve",marker='o', markerfacecolor='red', markersize=6)
		nextpointoncurve, = plt.plot(newval, self.equationf(newval), label="Next Point on Curve",marker='o', markerfacecolor='orange', markersize=6)

		# The usual 3 big boi points
		firstpoint,= plt.plot(initialval, 0, label="Initial Point",marker='o', markerfacecolor='red', markersize=6)
		nextpoint, = plt.plot(newval, 0, label="Next Point", marker='o', markerfacecolor='orange', markersize=6)



		# Labels the axis, title and show the legend
		plt.title("Secant Modified Method")
		plt.ylabel("Y axis")
		plt.xlabel("X axis")
		plt.legend()




		# slider functionality
		# This create the slider axe, (again remember that an axe is pretty much like a "plot" or "image" on a figure)
		# The first 2 numbers are like the where the left and bottom part of the slider starts, so 0.1 and 0.01 so its pretty low
		# the last 2 numer is the width and height of the slider
		axSlider1 = plt.axes([0.3,0.01,0.4, 0.05])

		# this line will turn the axe into an actual slider instead of a blank "plot" or image"
		# If you want to icnrease the total number of iteration available change valmax
		iterationSlider = Slider(axSlider1, "# of iterations", valmin = 1, valmax = 20, valinit = 1, valstep = 1)



		# This is the function that the slider will use when you change the slider value, will be explained later
		# What this function do is like what you read in the textbook the f(xl)*f(xu) < 0 and blah blah rule



		def newPoint(val):
			iteration = int(iterationSlider.val)
			initialval = self.initial
			deltaval = self.deltax

			y0 = self.equationf(initialval + deltaval*initialval)
			y1 = self.equationf(initialval)
			newval = self.initial - (deltaval*initialval*y1)/(y0-y1)
			print(f" The x0 value is {initialval}, f(x0) = {y1}, f(x1) = {y0}, newval = {newval}")
			m = (y0-y1)/(deltaval)
			C = -m*newval
			y = m*self.x + C
			# Based on the # of iteration you choose, this will do the condition process n times
			# so if you choose 2 iterations, it does the calculation 2 times
			for i in range(1,iteration):
				initialval = newval
				y0 = self.equationf(initialval + deltaval*initialval)
				y1 = self.equationf(initialval)
				newval = self.initial - (deltaval*initialval*y1)/(y0-y1)
				print(f" The x0 value is {initialval}, f(x0) = {y1}, f(x1) = {initialval + deltaval*initialval}{y0}, newval = {newval} and test = {deltaval*initialval}")
				m = (y0-y1)/(deltaval)
				C = -m*newval
				y = m*self.x + C
			# Once everything is done, update the points with the new x values 
			print(f" The X value is {newval}")
			firstpoint.set_xdata(initialval)
			nextpoint.set_xdata(newval)
			# Same thing update the x and y values of the new points
			initialpointoncurve.set_xdata(initialval)
			initialpointoncurve.set_ydata(self.equationf(initialval))
			nextpointoncurve.set_xdata(newval)
			nextpointoncurve.set_ydata(self.equationf(newval))
			
			# Update the equation of line with the new equation
			lineeqn.set_ydata(y)
			# Redraw everything
			plt.draw()



		# So iterationSlider is what i call my slider object, and the .on_changed() will be what the slider will do when it changed
		# the format is like this   sliderName.on_changed(Functiontocall)
		# Meaning when i change my slider values, so when it changes, it calls the function newPoint() that i did.
		iterationSlider.on_changed(newPoint)

		# Finally show all the things, plot, sliders, and etc
		plt.show()







if __name__ == "__main__":
	
		data = graphical12()
		data.modifiedSecant()
		# print(""" 
		# 1: False Position
		# 2: Bracketing
		# 3: Newton Fuck
		# """)
		# option = int(input("What methods do you want to use? Please Type the number: "))

		# if option == 1:
		# 	data.falsePosition()
		# elif option == 2:
		# 	data.bracketing()
		
	