import numpy as np
import equations as eq
import math

def f(fn,val):
    fx = fn(var)
    return fx

def gauss(eqns,mylist,erdes=0.1):
    """
    'eqns' is the equation names. [eq1,eq2,eq3].
    'mylist' is [x,y,z]. If you want to solve for x, y and z must be constant.
    'erdes' is the desired error.

    Example Input: gauss([eq.eq6,eq.eq7],[[Left Bound,Right Bound],yConstant,zConstant],0.01)
    """ 
    noFun = len(eqns)
    for i in len(mylist)
        if type(mylist[i]) == list:
            bound1 = mylist[i][0]
            bound2 = mylist[i][1]
            break
        elif i == len(mylist):
            print('You missed the wombat. The rebel aliance has died. shoot again, for the wombat has escaped.')
    
    error = 10000
    while error > erdes:
        for i in range(noFun)
            #solve each function
            f(eqns[i],mylist)
            

        
            
            error = [abs((xnew-xo)/xnew),abs((ynew-yo)/ynew),abs((znew-zo)/znew)]
            error to compare: max(error)

            #check for divergence


    















