import numpy as np
import scipy 
import pprint
from scipy import linalg
from sympy import *


class matrix:
    """ A matrix class which will contain all the different numerical methods such as ccramer's rule of LU Decomposition of solving 
        system of linear equations."""

    def __init__(self, eqn1, eqn2, eqn3 ):
        """ Initializes a matrix (currently only supporting 3 equations) with relative coefficients into 1 big matrix including A and B
            which will be separated later on in the code to form Matrix A and matrix B 
            (Note capital letters in the matrix represents matrix representation in Sympy notation where as non capitalize in scipy/numpy)
            """

        self.matrixdata = scipy.array([eqn1,eqn2,eqn3])
        self.matrixA = Matrix((self.matrixdata[0][0:3],self.matrixdata[1][0:3],self.matrixdata[2][0:3]))
        self.matrixa = scipy.array(self.matrixA.tolist())

        self.matrixb =np.array([eqn1[-1],eqn2[-1],eqn3[-1]]) 
        self.matrixB =Matrix(self.matrixb)
        

    def uDecompost(self, matrixA):
        """ Decomposes a Sympy Matrix to form a U matrix component"""
        matrixa0 = matrixA.row(0)

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
            print(f"Step 1: Row1 * {l1.tolist()[0]} - Row2")
            print(f"Step 2: Row1 * {l2.tolist()[0]} - Row2 yielding: \n")

        matrixb = Matrix((matrixa0,matrixa1, matrixa2))
        print(f"{scipy.array(matrixb.tolist())} \n")

        matrixb0 = matrixb.row(0)
        matrixb1 = matrixb.row(1)
        matrixb2 = matrixb.row(2) - matrixb.row(2).col(1)/matrixb.row(1).col(1)*matrixb.row(1)
        l3 = matrixb.row(2).col(1)/matrixb.row(1).col(1)

        print(f"Step3: Row2 * {l3.tolist()[0]} - Row 3 \n")
        matrixl = Matrix((matrixb0,matrixb1, matrixb2))
        print(scipy.array(matrixl.tolist()))
        return matrixl, l1.tolist(),l2.tolist(),l3.tolist()

    def uDecompostSym(self, matrixA):
        """ Decomposes a Sympy Matrix to form a U matrix component"""
        matrixa0 = matrixA.row(0)

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
            print(f"Step 1: Row1 * {l1.tolist()[0]} - Row2")
            print(f"Step 2: Row1 * {l2.tolist()[0]} - Row2 yielding: \n")

        matrixb = Matrix((matrixa0,matrixa1, matrixa2))
        self.step1 = matrixb
        print(f"{scipy.array(matrixb.tolist())} \n")

        matrixb0 = matrixb.row(0)
        matrixb1 = matrixb.row(1)
        matrixb2 = matrixb.row(2) - matrixb.row(2).col(1)/matrixb.row(1).col(1)*matrixb.row(1)
        l3 = matrixb.row(2).col(1)/matrixb.row(1).col(1)

        print(f"Step3: Row2 * {l3.tolist()[0]} - Row 3 \n")
        matrixl = Matrix((matrixb0,matrixb1, matrixb2))
        print(scipy.array(matrixl.tolist()))
        self.step2 = matrixl
        return matrixl, l1.tolist(),l2.tolist(),l3.tolist()



    def gaussjordan(self):
        print("Gauss Jordan Elimination")
        x1,x2 ,x3 = symbols('x1, x2, x3')
        
        finalMatrix = self.uDecompostSym(Matrix(self.matrixdata))[0]
        answers = linsolve(Matrix(self.matrixdata), (x1,x2,x3))
        print(scipy.array(finalMatrix.tolist()))
        print("\nAnd the roots are:")
        print(answers)
        return 0


    def gaussjordanSym(self):
        print("Gauss Jordan Elimination")
        x1,x2 ,x3 = symbols('x1, x2, x3')
        
        self.finalMatrix = self.uDecompostSym(Matrix(self.matrixdata))[0]
        print("\nAnd the roots are:")
        return linsolve(Matrix(self.matrixdata), (x1,x2,x3))

    



if __name__ == "__main__":
    test = matrix([5,5, 2, 12],[2, 4, 5, 2],[39, 43, 45, 74])
    test.gaussjordan()