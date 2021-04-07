import numpy as np
import pandas as pd



class Integral:
    """
    
    A class containing all the numerical methods for solving Integrals.
    
    An example of how to use this in code is first write a function for your equation
    For example
    def equation1(x):
        y = x**2 + -3*x
        return y
    
    From the equation you then initialize the class for the ODE
    
    test = ODE(equation1)
    
    you can then call any of the functions available for example
    test.simpson38(5,6,10)
    
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

#     
    # def differential(self, xval):
    #     x = sp.symbols('x')
    #     y = sp.Subs(sp.diff(self.equation(x) , x),x,xval).doit()
    #     return y
 
    def trapezoidalRule(self, visualizer= False, tabular = False , x = None, y = None, b = None, a = None, n = 10):
        """
    
        Parameters.
        
        ----------
        visualizer : TYPE, optional
            NOT USABLE FOR NOW
        tabular : TYPE, optional
            For cases where data is given in a table.
        x : ARRAY, optional
            Array of x values. Only Input data is given in tabular form and not equation form. The default is None.
        y : TYPE, optional
            Array of x values. Only Input data is given in tabular form and not equation form. The default is None.
        b : float, optional
            Highest secondary value. The default is None.
        a : float, optional
            First initial point. The default is None.
        n : int, optional
            Number of iterations. The default is 10.

        Returns
        -------
        I : float
            numerical integral.

        """
        if tabular == True:
            n = len(x) - 1
            slicedy = y[1:n]
            print(np.sum(slicedy))
            I = (x[n]-x[0])*(y[0] + 2*np.sum(slicedy)+ y[n])/(2*n)
        else:
            h = (b-a)/n
            xi = h + a
            sumval = 0
            while xi < b:
                sumval += self.equation(xi)
                xi += h
            print(f"the initial value is {xi}")
            I = (b-a)*(self.equation(a) + 2*sumval+ self.equation(b))/(2*n)
            print(f'(f({a})={self.equation(a)} + 2*{sumval} + f{a}={self.equation()})/(2*{n}) ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        return I
    
    def simpson13(self, a, b,tabular = False , x = None, y = None, n = 10,):
        """
        
        Parameters.
        
        ----------
        tabular : Boolean, optional
            DESCRIPTION. The default is False.
        x : array, optional
            DESCRIPTION. The default is None.
        y : array, optional
            DESCRIPTION. The default is None.
        n : int, optional
            Number of iterations required for the rule. The default is 10.
        a : float, optional
            initial value (low number). The default is None.
        b : float, optional
            second initial value ( higher number). The default is None.

        Returns
        -------
        I : float
            final integrated value..

        """
        if tabular == True:
            n = len(x) -1
            slicedodd = y[2:n:2]
            slicedeven = y[1:n:2]
            print(slicedeven)
            print(slicedodd)
            I = (x[n]-x[0])*(y[0] + 4*np.sum(slicedeven) +2*np.sum(slicedodd)+ y[n])/(3*n)
        else:

            h = (b-a)/n
            xi = h + a
            xj = 2*h + a
            sumodd = 0
            sumeve = 0
            
            while xj < b-h:
                sumodd += self.equation(xj)
                xj += 2*h
            while xi<b:
                    sumeve += self.equation(xi)
                    xi += 2*h
            I = (b-a)*((self.equation(a) + 4*sumeve+ +2*sumodd + self.equation(b)) /(3*n))
            df = pd.DataFrame({
                'x' : [i for i in np.linspace(a,b,int((b-a)/h)+1)],
                'y' : [self.equation(x) for x in np.linspace(a,b,int((b-a)/h)+1)]
            })
            print(df)
        return I 

    def simpson38(self, b, a, visualizer= False, tabular = False , x = None, y = None, n = 10):
        """

        Parameters.
        
        ----------
        visualizer : boolean, optional
            DEFUNCT. The default is False.
        tabular : boolean, optional
            DESCRIPTION. The default is False.
        x : TYPE, optional
            DESCRIPTION. The default is None.
        y : TYPE, optional
            DESCRIPTION. The default is None.
        b : TYPE, optional
            DESCRIPTION. The default is None.
        a : TYPE, optional
            DESCRIPTION. The default is None.
        n : TYPE, optional
            DESCRIPTION. The default is 10.

        Returns
        -------
        I : TYPE
            Final Integrated value.

        """
        if tabular == True:
            n = len(x) -1
            slicedodd = y[2:n:2]
            slicedeven = y[1:n:2]
            print(slicedeven)
            print(slicedodd)
            I = (x[n]-x[0])*(y[0] + 4*np.sum(slicedeven) +2*np.sum(slicedodd)+ y[n])/(3*n)
        else:
            h = (b-a)/n
            xi = h + a
            xj = 2*h + a
            # xk = b
            sumodd = 0
            sumeve = 0
            
            while xj < b-h:
                sumodd += self.equation(xj)
                xj += 2*h
            while xi<b:
                    sumeve += self.equation(xi)
                    xi += 2*h
            I = (3*h/8)*((self.equation(a) + 4*sumeve+ +2*sumodd + self.equation(b)))
            df = pd.DataFrame({
                'x' : [i for i in np.linspace(a,b,int((b-a)/h)+1)],
                'y' : [self.equation(x) for x in np.linspace(a,b,int((b-a)/h)+1)]
            })
            print(df)
        return I 

    def rhomberg(self, j,k, b, a):
        """
        SEE JUPYTER NOTEBOOK FOR BETTER USAGE
        
        Parameters.
        
        ----------
        j : TYPE
            DESCRIPTION.
        k : TYPE
            DESCRIPTION.
        b : float
            DESCRIPTION.
        A : TYPE
            DESCRIPTION.

        Returns
        -------
        I2 : TYPE
            DESCRIPTION.

        """    
        I = np.empty((4,4),  dtype=np.float64)
        I[0][0] = self.trapezoidalRule(b =b,a =a, n=1) 
        print(f"I11 is {I[0][0]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        I[0][1] = self.trapezoidalRule(b =b,a =a, n=2)
        print(f"I12 is {I[0][1]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        I[0][2] = self.trapezoidalRule(b =b,a =a, n=4)
        print(f"I14 is {I[0][2]}")
        print("~~~~~~~~~~~~~~~~~~~~~~~")
        I2 = I[j-1-1][k] + (I[j-1-1][k] - I[j-1-1][k-1-1 + 1])/3
        return  I2


if __name__ == "__main__":
    def equation(x):  
     # y =  0.2 + 25*x - 200*x**2 + 675*x**3 -900*x**4 +400*x**5
     y = 2000*np.log(140000/(140000-2100*x))-9.8*x
     return y
    data = Integral(equation)
    print(data.rhomberg(2,1, 30 ,8))
 


