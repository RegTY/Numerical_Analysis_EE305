
import matplotlib
import sympy
from matplotlib.widgets import Slider,Button
import seaborn as sns
import numpy as np
import scipy
import pandas as pd
import matplotlib.pyplot as plt
sns.set(style="ticks")


def main():
    
    eqn = input("Enter an equation here (\"f(x) = 3*x\"): ")

    print(eqn)
    equationf = definition_to_function(eqn)
    equationf(10)


def definition_to_function(x):
    lhs, rhs = x.split("=", 1)
    rhs = rhs.rstrip('; ')
    args = sympy.sympify(lhs).args
    f = sympy.sympify(rhs)
    def f_func(*passed_args):
        argdict = dict(zip(args, passed_args))
        result = f.subs(argdict)
        return float(result)
    return f_func

if __name__ == "__main__":
    main()