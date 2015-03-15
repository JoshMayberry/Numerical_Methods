import math
from equations import *
from my_functions import *
import numpy as np

def function(fn,x):
    x = [x]
    fx = fn(x)
    return fx

def bip(fn,xaxis=[-1,1],inc=0.1,edes=0.01):
    """This function runs bi(), but first shows you a plot and lets you choose the roots you want.
    'fn' is the name of an equation in 'equations.py'
    'coeff' are the coefficents for the function as a list
    'xaxis' is [min x on graph, max x on graph]. The default is [-1,1]
    'inc' is what the tickmarks(increments) will increase by. The default is 0.1.
    'edes' is the desired margin of error. The default is 1% error.

    Example Input: bip(eq1,0.001)
"""
    plot(fn,xaxis,inc)
    xbounds = [0,0]
    xbounds[0] = eval(input(' Left Bound: '))
    xbounds[1] = eval(input('Right Bound: '))
    #print(fn,'\n','\n',co,'\n','\n',xbounds,'\n',edes)
    bi(fn,xbounds,edes)
    print('Have a good day.')

def bi(fn,xbounds,edes=0.01):
    """This function finds roots (solves the equation) by steadily homing in on a single root.

Limitations: Can only find one root. It misses all others.

'fn' is the name of an equation in 'equations.py'
'xbounds' is [Left Bound,Right Bound], and should be x-axis values, not y-axis values.
'edes' is the desired margin of error. If you do not put a value here, it will default to 1% error.

Example Input: bi(eq1,[0.6,1.2],0.001)
"""
    x1 = xbounds[0]         #left bound
    x2 = xbounds[1]         #right bound
    edes = edes/100         #desired %error
    n = math.ceil(math.log(abs(x1-x2)/edes)/math.log(2))
    #print('edes: ',edes,'\nn: ',n,'\nfn',fn,'\ncoeff',coeff)
    i = 0
    print('Just one moment...')
    for i in range(int(n)):
        xnew = (x1+x2)/2
        error = abs((x1-xnew)/xnew)*100
        check = function(fn,x1)*function(fn,xnew)
        if check > 0:
            x1 = xnew
        elif check < 0:
            x2 = xnew
        else:
            print("You broke something. I'm surprised.")
            break
        #print('x1: ',x1,'\nx2: ',x2,'\nxnew: ',xnew,'\nerror: ',error,'\ncheck: ',check)
    print('approx. root: ',xnew,'\n%error: ',error)
