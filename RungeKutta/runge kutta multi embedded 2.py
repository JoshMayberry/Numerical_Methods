import math
import numpy as np

#Functions that can be run
def dy1(t,varList):
    """dy/dt=y*sin^3(t)"""
    global count
    count += 1
    y = varList[0]
    return y*math.sin(t)**3

def dy2(t,varList):
    global count
    count += 1
    x = varList[0]
    y = varList[1]
    return 4-0.1*x-0.2*y

def dx2(t,varList):
    global count
    count += 1
    x = varList[0]
    y = varList[1]
    return  -0.5*x+y*t

#The program
def rkm(fnList,t,varList,tFinal,h=1,ertol=0.00001):
    """This function computes the conditioned function

    'fnList' is a list of the function names, such as [dx2,dy2]
    't' is the starting t value.
    'varList' is a list of the initial variables, such as [1,2] for [x0,y0]
    'tFinal' is how far you want to go on the time (t) axis.
    'h' is the step size. For a higher accuracy, use a smaller step size.
    'ertol' is the error tolerance

    Example Input: rkm([dx2,dy2],0,[1,2],4)
    """
    global count
    count = 0
    tFinal += 1
    for i in range(tFinal):
        k1,k2,k3,k4,k5,k6,varList4,varList5,varListScale = [],[],[],[],[],[],[],[],[]
        for i in range(len(varList)):
            k1.append(fnList[i](t,varList))
        #print('k1',k1)
        for i in range(len(varList)):
            k2.append(fnList[i](t+h/5,[varList[y]+h/5*k1[y] for y in range(len(varList))]))
        #print('k2',k2)
        for i in range(len(varList)):
            k3.append(fnList[i](t+3/10*h,[varList[y]+3/40*k1[y]*h+9/40*k2[i]*h for y in range(len(varList))]))
        #print('k3',k3)
        for i in range(len(varList)):
            k4.append(fnList[i](t+3/5*h,[varList[y]+3/10*k1[y]*h-9/10*k2[i]*h+6/5*k3[y]*h for y in range(len(varList))]))
        #print('k4',k4)
        for i in range(len(varList)):
            k5.append(fnList[i](t+h,[varList[y]-11/54*k1[y]*h+5/2*k2[i]*h-70/27*k3[y]*h+35/27*k4[y]*h for y in range(len(varList))]))
        #print('k5',k5)
        for i in range(len(varList)):
            k6.append(fnList[i](t+7/8*h,[varList[y]+1631/55296*k1[y]*h+175/512*k2[y]*h+575/13824*k3[i]*h+44275/110592*k4[y]*h+253/4096*k5[y]*h for y in range(len(varList))]))
        #print('k6',k6)
        y = 0
        for i in range(len(varList)):
            varList4.append(varList[i]+(37/378*k1[i]+250/621*k3[i]+125/594*k4[i]+512/1771*k6[i])*h)
            varList5.append(varList[i]+(2825/27648*k1[i]+18575/48384*k3[i]+13525/55296*k4[i]+277/14336*k5[i]+1/4*k6[i])*h)
        t += h
        deltaList = [varList5[y]-varList4[y] for y in range(len(fnList))]
        scaleList = [varList5[y]+fnList[y](t,[varList5[y]])*h for y in range(len(fnList))]
        errorList = [ertol*scaleList[y] for y in range(len(fnList))]
        n = np.array(deltaList).argmax()
        if np.abs(deltaList[n])<np.abs(errorList[n]):
            alpha = 0.2
        else:
            alpha = 0.25
        h = np.abs(errorList[n]/deltaList[n])**alpha*h
        varList = varList5[:]
        #print('h',h)
    return (varList,t,count)
















