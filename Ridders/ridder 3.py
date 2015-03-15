import numpy as np
import math
import equations as eq

def f(fn,val):
    global solvefor
    if solvefor == 'x':
        var = [val,eq.y,eq.z]
    elif solvefor == 'y':
        var = [eq.x,val,eq.z]
    elif solvefor == 'z':
        var = [eq.x,eq.y,val]
   
    fx = fn(var)
    return fx

def ri(eq,guess,edes=0.01):
    """This version of Ridder's methood solves a 3 variable eqn.

    Gaurntees the root stays bracketed (unlike secant)
    Has similar efficency to secant methood.

    Limitation: requires endpoints to have opposite signs for the functional values (ex: x1 is + and x2 is -).

    'eq' is the name of the equation.
    'guess' is [[left bound, right bound],y,z] or [x,[left bound, right bound],z] or [x,y,[left bound, right bound]].
    'edes' is the desired error.

    Example Input: ri(eq.eq5,[1.4,1.6])
    """
    #Find out what is being solved for.
    global solvefor
    if type(guess[0]) == list:
        solvefor = 'x'
    elif type(guess[1]) == list:
        solvefor = 'y'
    elif type(guess[2]) == list:
        solvefor = 'z'
        
    #Check that they put in a left and right bound.
    answer = input('Did you put the left bound and right bound in as your guess?')
    if answer == 'yes':
        print('Good job. I will now calculate your root.')
    elif answer == 'no':
        guess = [0,0]
        guess[0] = eval(input('What is the left bound?'))
        guess[1] = eval(input('What is the right bound?'))
    else:
        print('I do not understand, but will assume that you did.')

    #Run Ridder's Methood
    x1 = guess[0]
    x2 = guess[1]
    edes = edes/100
    n = math.ceil(math.log(abs(x1-x2)/edes)/math.log(2))
    for i in range(int(n)):
        f1 = f(eq,x1)
        f2 = f(eq,x2)
        x3 = (x1+x2)/2
        f3 = f(eq,x3)
        x4 = x3+(x3-x1)*np.sign(f1-f2)*f3/math.sqrt(f3**2-f1*f2)
        f4 = f(eq,x4)
        if f3*f4<0:
            x1 = x3
            x2 = x4
        elif f1*f4<0:
            x1 = x1
            x2 = x4
        elif f2*f4<0:
            x1 = x4
            x2 = x2
        else:
            print('You broke something.')
            break
    error = abs((x1-x2)/x2)*100
    print('approx. root: ',x4,'\n%error: ',error)










                                                       
