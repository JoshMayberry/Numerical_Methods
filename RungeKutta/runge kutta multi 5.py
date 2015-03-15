import math

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
def rkm(fnList,t,varList,tFinal,h=1):
    """This function computes the conditioned function

    'fnList' is a list of the function names, such as [dx2,dy2]
    't' is the starting t value.
    'varList' is a list of the initial variables, such as [1,2] for [x0,y0]
    'tFinal' is how far you want to go on the time (t) axis.
    'h' is the step size. For a higher accuracy, use a smaller step size.

    Example Input: rkm([dx2,dy2],0,[1,2],4)
    """
    global count
    count = 0
    tFinal += 1
    for i in range(tFinal):
        k1,k2,k3,k4 = [],[],[],[]
        for i in range(len(varList)):
            k1.append(fnList[i](t,varList))
        for i in range(len(varList)):
            k2.append(fnList[i](t+h/2,[varList[y]+h/2*k1[y] for y in range(len(varList))]))
        for i in range(len(varList)):
            k3.append(fnList[i](t+h/2,[varList[y]+h/2*k2[y] for y in range(len(varList))]))
        for i in range(len(varList)):
            k4.append(fnList[i](t+h,[varList[y]+h*k3[y] for y in range(len(varList))]))
        t += h
        for i in range(len(varList)):
            varList[i] += h/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])
    return (varList,t,count)
















