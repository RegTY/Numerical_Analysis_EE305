import numpy as np



class ODE:
    """
    
    A class containing all the numerical methods for solving ODES.
    
    An example of how to use this in code is first write a function for your equation
    For example
    def equation1(x):
        y = x**2 + -3*x
        return y
    
    From the equation you then initialize the class for the ODE
    
    test = ODE(equation1)
    
    you can then call any of the functions available for example
    test.RK2(0, 1, 0.5, 4)
    
    """

    def __init__(self, equation = callable , *args , **kwargs):
        """
        Integral library containing variables numerical tool for integrations.
        
        Parameters
        ----------
        equation : FUNCTION, optional
             a function which conntains equations. The default is callable.
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.
        
        Returns
        -------
        None.
        
        """
        self.equation =equation
    
    
    def euler(self, yi, xi, b, h ):
        """
        Euler's -cauchy method.

        Parameters
        ----------
        yi : float
            Initial Y value.
        xi : float
            Final Y value.

        Returns
        -------
        yi1 : TYPE
            DESCRIPTION.

        """
        i = 0
        while i <b:
            yi1 =yi+ self.equation(xi,yi)*h
            xi += h
            yi = yi1
            print(f'xi is {xi}, yi is {yi}')
            i += h
        return yi1

    def heun(self, yi,xi,h,b, n1=1):
        """
        Huen method, a combination of euler and some magic stuff.

        Parameters
        ----------
        yi : float
            initial y value.
        xi : float
            initial x value.
        h : TYPE
            step size.
        n1 : TYPE, optional
            internal iteration. The default is 1.

        Returns
        -------
        yi : TYPE
            DESCRIPTION.

        """
        i = 0
        ypredict = yi+ self.equation(xi,yi)*h
        
        i = 0
        j = 0

        # yi = yi1
        # xi += self.h

        while j < b:
            while i < n1 :
                yi1 = yi + (self.equation(xi,yi) + self.equation(xi + h,ypredict))/2*h
                ypredict = yi1
                i += 1
                #print(f"Y-predict  {ypredict} at {i} iteration")
            i = 0
            yi = yi1
            xi += h    
            ypredict = yi + self.equation(xi,yi)*h
            j += h
            # xi += self.h
            # yi = yi1
            print(f'yi {yi} at xi {xi} ')
        return yi    

    def RK2(self, xi,yi,h,b):
        """
        RK2 method.

        Parameters
        ----------
        xi : float
            initial x value.
        yi : float
            initial y value.
        h : float
            step size.
        b : float
            Upper value.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        def incrementalfunction(xi,yi,h):
            k1 = self.equation(xi,yi)
            k2 = self.equation(xi+3/4*h,yi +3/4*k1*h)
            y = 1/3*k1 + 2/3*k2
            return y
        i = 0
        while i < b:
            yi1 = yi + incrementalfunction(xi,yi,h)*h
            
            xi += h
            yi = yi1
            print(f'xi = {xi}, yi1 = {yi1}')
            i += h
        return yi1

    def RK3(self, xi,yi,h,b):
        """
        RK3 method.

        Parameters
        ----------
        xi : float
            initial x value.
        yi : float
            initial y value.
        h : float
            step size.
        b : float
            Upper value.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        def incrementalfunction(xi,yi,h):
            k1 = self.equation(xi,yi)
            k2 = self.equation(xi + 1/2*h, yi + 1/2*k1*h)
            k3 = self.equation(xi+h, yi - k1*h +2*k2*h)
            y =  1/6*(k1 + 4*k2 + k3)
            
            return y
        i = 0
        while i < b:
            yi1 = yi + incrementalfunction(xi,yi,h)*h
            
            xi += h
            yi = yi1
            print(f'xi = {xi}, yi1 = {yi1}')
            i += h
        return yi1
    def RK4(self, xi,yi,h,b):
        """
        RK3 method.

        Parameters
        ----------
        xi : float
            initial x value.
        yi : float
            initial y value.
        h : float
            step size.
        b : float
            Upper value.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        def incrementalfunction(xi,yi,h):
            #print(xi)
            k1 = self.equation(xi,yi)
            k2 = self.equation(xi + 1/2*h, yi + 1/2*k1*h)
            k3 = self.equation(xi + 1/2*h, yi + 1/2*k2*h)
            k4 = self.equation(xi+h, yi + k3*h)
            y =  1/6*(k1 + 2*k2 + 2*k3 + k4)
            print(y)
            #print(f" k1 {k1}, k2 {k2}, k3 {k3}, k4 {k4}")
            return y
        i = 0
        while i < b:
            yi1 = yi + incrementalfunction(xi,yi,h)*h
            
            xi += h
            yi = yi1
            print(f'xi = {xi}, yi1 = {yi1}')
            i += h
        return yi1

    def RK5(self, xi,yi,h,b):
        """
        RK3 method.

        Parameters
        ----------
        xi : float
            initial x value.
        yi : float
            initial y value.
        h : float
            step size.
        b : float
            Upper value.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
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
        while i < b:
            yi1 = yi + incrementalfunction(xi,yi,h)*h
            
            xi += h
            yi = yi1
            print(f'xi = {xi}, yi1 = {yi1}')
            i += h
        return yi1
if __name__ == "__main__":
    def equation(x,y):
        ydot = -2*x**3 + 12*x**2 - 20*x + 8.5
        return ydot
    data = ODE(equation = equation)
    print("RK2")
    print(data.RK2(0, 1, 0.5, 4))
    print("RK3")
    print(data.RK3(0, 1, 0.5, 4))
    print("RK4")
    print(data.RK4(0, 1, 0.5, 4))
    print("RK5")
    print(data.RK5(0, 1, 0.5, 4))


