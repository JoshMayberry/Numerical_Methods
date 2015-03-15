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
    'ertol' is the error tolerance.

    Example Input: rkm([dx2,dy2],0,[1,2],4)
    """
    global count
    count = 0
    tFinal += 1
    for k in range(tFinal):
        hList = [h,h/2,h/2]
        tList = [t,t,t+h/2]
        yList = []
        print('new step')
        for j in range(3):
            k1,k2,k3,k4 = [],[],[],[]
            for i in range(len(fnList)):
                print(t,varList)
                k1.append(fnList[i](tList[j],varList))
            print('k1',k1)
            for i in range(len(fnList)):
                k2.append(fnList[i](tList[j]+hList[j]/2,[varList[y]+hList[j]/2*k1[y] for y in range(len(varList))]))
            print('k2',k2)
            for i in range(len(fnList)):
                k3.append(fnList[i](tList[j]+hList[j]/2,[varList[y]+hList[j]/2*k2[y] for y in range(len(varList))]))
            print('k3',k3)
            for i in range(len(fnList)):
                k4.append(fnList[i](tList[j]+hList[j],[varList[y]+hList[j]*k3[y] for y in range(len(varList))]))
            print('k4',k4)
            for i in range(len(fnList)):
                yList.append([varList[i]+hList[j]/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])])
            if j == 1:
                varList = []
                varList.extend(yList[1]) #Computes with y Intermediate for the 2nd half step
            #print(varList,yList,'\n')
        t += h
        deltaList = [yList[2][y]-yList[0][y] for y in range(len(fnList))]
        #print('deltaList',deltaList)
        varList = [yList[2][x]+deltaList[x]/15 for x in range(len(fnList))]
        #print('varList',varList)
        scaleList = [varList[y]+fnList[y](t,[varList[y]])*h for y in range(len(fnList))]
        #print('scaleList',scaleList)
        errorList = [ertol*scaleList[y] for y in range(len(fnList))]
        #print('errorList',errorList)
        n = np.array(deltaList).argmax()
        #print('n',n)
        if np.abs(deltaList[n]) < np.abs(errorList[n]):
            alpha = 0.2
        else:
            alpha = 0.25
        #print('alpha',alpha)
        h = np.abs(errorList[n]/deltaList[n])**alpha*h
        print('h',h)
    return (varList,t,count)
















