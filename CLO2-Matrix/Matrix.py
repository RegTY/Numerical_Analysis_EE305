import numpy as np
import scipy 
import pprint
from scipy import linalg
#from sympy import Matrix
from sympy import *
class matrix:
    """ A matrix class which will contain all the different numerical methods such as ccramer's rule of LU Decomposition of solving 
        system of linear equations."""

    def __init__(self, eqn1, eqn2, eqn3 ):
        """ Initializes a matrix (currently only supporting 3 equations) with relative coefficients into 1 big matrix including A and B
            which will be separated later on in the code to form Matrix A and matrix B 
            (Note capital letters in the matrix represents matrix representation in Sympy notation where as non capitalize in scipy/numpy)
            """
        np.set_printoptions(precision=4, suppress=True)
        if eqn1[0] == 0:
            temp = eqn1
            eqn1 = eqn2
            eqn2 = temp

        self.matrixdata = scipy.array([eqn1,eqn2,eqn3])

        self.matrixA = Matrix((self.matrixdata[0][0:3],self.matrixdata[1][0:3],self.matrixdata[2][0:3]))
        self.matrixa = scipy.array(self.matrixA.tolist())

        self.matrixb =np.array([eqn1[-1],eqn2[-1],eqn3[-1]]) 
        self.matrixB =Matrix(self.matrixb)
    def x1func(self,x2,x3):
        x1 = (test.matrixb[0] - test.matrixa[0][1] * x2 -  test.matrixa[0][2] * x3)/test.matrixa[0][0]
        return x1
    def x2func(self,x1,x3):
        x2 = (test.matrixb[1] - test.matrixa[1][0] * x1 -  test.matrixa[1][2] * x3)/test.matrixa[1][1]
        return x2   
    def x3func(self,x1,x2):
        x3 = (test.matrixb[2] - test.matrixa[2][0] * x1 -  test.matrixa[2][1] * x2)/test.matrixa[2][2]
        return x3

    def uDecompost(self, matrixA):
        """ Decomposes a Sympy Matrix to form a U matrix component"""
        matrixa0 = matrixA.row(0)
        print("U DECOMPOSITION")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if(np.array(matrixA.row(0).col(0).tolist()).astype(np.float64) == 0):
            matrixa1 = matrixA.row(1)
            matrixa2 = matrixA.row(2)
            l1 = Matrix([0])
            l2 = Matrix([0])

        else:
            matrixa1 = matrixA.row(1) - matrixA.row(1).col(0)/matrixA.row(0).col(0)*matrixA.row(0)
            matrixa2 =matrixA.row(2) - matrixA.row(2).col(0)/matrixA.row(0).col(0)*matrixA.row(0)
            l1 = Matrix(matrixA.row(1).col(0)/matrixA.row(0).col(0))
            l2 = Matrix(matrixA.row(2).col(0)/matrixA.row(0).col(0))
            print(f"Step 1: -Row1 * {l1.tolist()[0]} + Row2")
            print(f"Step 2: -Row1 * {l2.tolist()[0]} + Row2 yielding: \n")

        matrixb = Matrix((matrixa0,matrixa1, matrixa2))
        self.step1 = matrixb
        print(f"{scipy.array(matrixb.tolist())} \n")

        matrixb0 = matrixb.row(0)
        matrixb1 = matrixb.row(1)
        matrixb2 = matrixb.row(2) - matrixb.row(2).col(1)/matrixb.row(1).col(1)*matrixb.row(1)
        l3 = matrixb.row(2).col(1)/matrixb.row(1).col(1)

        print(f"Step3: -Row2 * {l3.tolist()[0]} + Row 3 \n")
        matrixl = Matrix((matrixb0,matrixb1, matrixb2))
        self.step2 = matrixl
        print(scipy.array(matrixl.tolist()))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        return matrixl, l1.tolist(),l2.tolist(),l3.tolist()


    def lDecompost(self,l1,l2,l3):
        """ Decomposes a Sympy Matrix to form a L matrix component"""
        matrixl = np.identity(3)
        matrixl[1][0] = l1[0][0]
        matrixl[2][0] = l2[0][0]
        matrixl[2][1] = l3[0][0]
        return Matrix(matrixl)

    def gaussjordan(self):
        """ Shows a step by step solution on how gaussjordan elimination is done"""
        print("Gauss Jordan Elimination")
        x1,x2 ,x3 = symbols('x1, x2, x3')
        
        self.finalMatrix = self.uDecompost(Matrix(self.matrixdata))[0]
        print("\nAnd the roots are:")
        return linsolve(Matrix(self.matrixdata), (x1,x2,x3))



    def LUDecomposition(self):
        """ Shows a step by step solution on how LU Decomposition elimination is done"""

        matrixu, l1,l2,l3 = test.uDecompost(test.matrixA)
        matrixl = test.lDecompost(l1,l2,l3)
        matrixd = linalg.solve(np.array(matrixl.tolist()).astype(np.float64), test.matrixb)
        ans= linalg.solve(np.array(matrixu.tolist()).astype(np.float64), matrixd)
        return ans
    
    def LUInverse(self):
        """ Shows a step by step solution on how LU Decomposition elimination to determine the inverse of a matrix is done"""
        matrixu, l1,l2,l3 = test.uDecompost(test.matrixA)
        matrixl = test.lDecompost(l1,l2,l3)
        matrixI = np.identity(3)
        matrixd1= linalg.solve(np.array(matrixl.tolist()).astype(np.float64), matrixI[: , 0])

        Imatrix1= linalg.solve(np.array(matrixu.tolist()).astype(np.float64), matrixd1)
        matrixd2= linalg.solve(np.array(matrixl.tolist()).astype(np.float64), matrixI[: , 1])
        Imatrix2= linalg.solve(np.array(matrixu.tolist()).astype(np.float64), matrixd2)
        matrixd3= linalg.solve(np.array(matrixl.tolist()).astype(np.float64), matrixI[: , 2])
        Imatrix3= linalg.solve(np.array(matrixu.tolist()).astype(np.float64), matrixd3)
        InverseMatrix = np.array((Imatrix1,Imatrix2,Imatrix3))

        pprint(f"Intermediate Matrix D1 {matrixd1}")
        pprint(f"Intermediate Matrix D2 {matrixd2}")
        pprint(f"Intermediate Matrix D3 {matrixd3}")

        pprint(Matrix(np.transpose(InverseMatrix)))
        return Matrix(np.transpose(InverseMatrix))
    
    def Gauss_Seidal(self ,x1,x2,x3,n):
        """ Shows a step by step solution on using Gauss-seidal's method of solving system of linear equations"""
        # the iterative equations for the different x


        def solver(x1,x2,x3 , n):
            iterations = n

            #Initial Values
            x1 = x1
            x2 = x2
            x3 =x3
            for i in range(0,iterations):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"{i+1} iteration")
                print (f"X1 is {x1}, X2 is {x2}, x3 is {x3}\n")
                x1 = self.x1func(x2,x3)
                print("calculating for x1 using formula\n")
                #print( f"(({test.matrixb[0]})-({test.matrixa[0][1]})*({x2})-({test.matrixa[0][2]})*({x3})/{test.matrixa[0][0]} ")
                
                print (f"X1 is {x1}, X2 is {x2}, x3 is {x3}\n")       
                x2 = self.x2func(x1,x3)
                print("calculating for x2 using formula")
                print (f"X1 is {x1}, X2 is {x2}, x3 is {x3}\n")       
                x3 = self.x3func(x1,x2)
                print("calculating for x3 using formula")
                
                print (f"X1 is {x1}, X2 is {x2}, x3 is {x3}\n")
            return x1,x2,x3

        return solver(x1,x2,x3 , n)
    
    def Jacobi_Iterative(self,x1,x2,x3,n):

        
        def solver(x1,x2,x3 , n):
            iterations = n

            #Initial Values
            x1 = x1
            x2 = x2
            x3 = x3
            
            x1new = 0
            x2new = 0 
            x3new = 0
            for i in range(0,iterations):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"{i+1} iteration")
                
                
                print("calculating for x1,x2,x3 using formula") 
                x1new = self.x1func(x2,x3)
                x2new = self.x2func(x1,x3)
                x3new = self.x3func(x1,x2)
                
                print (f"X1 is {x1new}, X2 is {x2new}, x3 is {x3new}\n")
                x1 = x1new
                x2 = x2new
                x3 = x3new
                
                
            return x1,x2,x3
        return solver(x1,x2,x3,n)

if __name__ == "__main__":
    test = matrix([0, 8, 2, -7], [3, 5, 2, 8],[6, 2, 8 , 26])
    test.Jacobi_Iterative(0,0,0,3)
    #print(Matrix(linalg.inv(test.matrixa.astype(np.float64))))