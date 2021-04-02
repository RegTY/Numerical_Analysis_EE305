
import sympy as sp
sp.interactive.init_printing(use_latex=True) #just to format our answers
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

fig , (xforce, yforce) = plt.subplots(2,1 ,figsize = (15,15), sharex = True)

angle = np.linspace(0 , np.pi, 100)

fx = 0.1875*np.pi*np.cos(angle - np.deg2rad(90)) 
fy = -1630.98878695209*np.pi*(15328.125*np.sin(angle -np.deg2rad(90)) -5.518125*np.sin(angle -np.deg2rad(90)) -  45990.17)

xforce.plot(angle, fx, marker = '2', color = 'red')
yforce.plot(angle, fy, marker = '2')
xforce.set(ylabel="Force Exerted on X-axis, N" , title = "Relationship between Inclination angle and force on x-axis" )
yforce.set(ylabel="Force Exerted on Y-axis, N" , title = "Relationship between Inclination angle and force on y-axis",xlabel="Angle in Radians")


plt.show()

