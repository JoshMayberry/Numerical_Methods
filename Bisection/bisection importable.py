import math
from equations import *

def function(fn,x,coeff):
    x = [x]
    x.extend(coeff)
    fx = fn(x)
    return fx

def bi(fn,coeff,xbounds,edes=0.01):
    """This function finds roots (solves the equation) by steadily homing in on a single root.

Limitations: Can only find one root. It misses all others.

'fn' is the name of an equation in 'equations.py'
'coeff' are the coefficents for the function as a list
'xbounds' is [Left Bound,Right Bound], and should be x-axis values, not y-axis values.
'edes' is the desired margin of error. If you do not put a value here, it will default to 1% error.

Example Input: bi(eq1,[10,1-],[0.6,1.2],0.001)
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
        check = function(fn,x1,coeff)*function(fn,xnew,coeff)
        if check > 0:
            x1 = xnew
        elif check < 0:
            x2 = xnew
        else:
            print("You broke something. I'm surprised.")
            break
        #print('x1: ',x1,'\nx2: ',x2,'\nxnew: ',xnew,'\nerror: ',error,'\ncheck: ',check)
    print('approx. root: ',xnew,'\n%error: ',error)
