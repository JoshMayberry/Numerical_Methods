import numpy as np
import equations as eq
import math
import sys

#def f1(xlist):
    #"""Solves x = 2y+z-s+sqrt(t)"""
    #return 2*x[1]+x[2]-x[3]+math.sqrt(x[4])

def f1(myList):
    """Solves x = Sqrt((120-y)/8)"""
    return math.sqrt((120-myList[1])/8)
    #return 120-8*myList[0]**2

def f2(myList):
    """Solves y = x^3-1"""
    return myList[0]**3-1
    #return (myList[1]+1)**(1/3)

def f3(mylist)

def f(fn,var):
    return fn(var)

def gauss(eqns,erdes=0.025):
    """
    'eqns' is the equation names. [eq1,eq2,eq3].
    'erdes' is the desired error.

    Example Input: gauss([f1,f2],0.01)
    """
    noFun = len(eqns)
    var = [3.14688]*noFun #[x,y,z]
    varNew = var[:]
    error = [10000]*noFun
    varDif=[3.14688]*noFun
    nHistory =[]
    count = 0

    while max(error) > erdes:
        for i in range(noFun):
            #solve each function
            varNew[i] = f(eqns[i],var)

        for i in range(noFun):
            error[i] = abs((varNew[i]-var[i])/varNew[i])
            varDif[i]=(abs(varNew[i]-var[i])/2)
            #print('i:',i,'varNew[i]:',varNew[i],'var[i]:',var[i])
            #print('varDif:',varDif)

        for i in range(noFun):
            if varDif[i]==max(varDif):
                n=i
                nHistory.append(varNew[n])
                #print('n:',n)
        
        #print('count:',count,'error:',error)
        count += 1
        var = varNew[:]
        if count == 6: #This Must always be an even Number. #It hasn't converged within 10 iterations. So, Is it diverging?
            var = [3.14688]*noFun #[x,y,z]
            varNew = var[:]
            halfLength = len(nHistory)/2
            firstHalf = 0
            secondHalf = 0
            for i in range(int(halfLength)):
                firstHalf = firstHalf + nHistory[i]
                secondHalf = secondHalf + nHistory[i+int(halfLength)]
            half1 = firstHalf/halfLength
            half2 = secondHalf/halfLength
            if abs(half1) < abs(half2):
                print('This function Diverges. Re-do.')
                sys.exit(0)
            else:
                print('It converges. I shall continue.')
    return varNew,count,error

    















