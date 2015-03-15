import math
from equations import *

def function(fn,x):
    fx = fn(x)
    return fx

def se(fn,xbounds):
    """This equation finds the roots (solutions) of equations using the secant methood.

    Limitations: Easily skips over roots, Gets stuck in local minimums for a while, Wanders until it finds somthing.

    Note: Can be modified to only need 1 xbound if it finds the second one as a pnt. 0.00001 away from the first one.

    'fn' is the name of the equation in 'equations.py'
    'xbounds' is [Left bound, Right Bound]

    Example Input: se(eq4,[0,0])
    """
    xold = xbounds[0]
    xo = xbounds[1]
    for i in range(3+1):
        xnew = xo - (function(fn,xo)*(xold-xo))/(function(fn,xold)-function(fn,xo))
        error = abs((xo-xnew)/xnew)*100
        xold = xo
        xo = xnew
        #print(error)
    return xold,error
