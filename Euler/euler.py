import math
import numpy as np
yo = 1

def slope(t,y):
    """dy/dt=y*sin^3(t)"""
    global count
    count +=1
    return y*math.sin(t)**3

def ex5(eqn,told,yold,tfinal,stepSize=1):
    """Euler's Methood
    'eqn' is the name of the dy/dx equation.
    'told' is your first time step.
    'yold' is your first y step.
    't final' is what your final time step is.
    'stepSize' is the size of steps to get from told to tfinal.

    Psudocode:
    Input Eqn, Initial Conditions, Step Size, & either '# of steps' or 'final value t (# of steps must be calculated)'     
    For i in '# of steps':
        Calculate Slope
        Calculate y new and y t
    Return final value

    Example Input: ex5(slope,0,1,3,0.5)"""
    global count
    count = 0
    time = (tfinal-told)/stepSize
    for i in range(int(np.ceil(time))):
        dy = eqn(told,yold)
        ynew = yold + dy*stepSize
        tnew = told + stepSize
        error = (ynew-yold)/ynew
        told = tnew
        yold = ynew
    return(ynew,error,count)
