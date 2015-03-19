#Curve Fit Program
#This program creates trendlines from data points
#By: Joshua Mayberry
#
#########################################
#                                       #
#           Table of Contents           #
#                                       #
#   Main Program............26 - 70     #
#   Check Program...........73 - 102    #
#   Line Generator Logic...104 - 120    #
#   Trendline Optimiser....122 - 134    #
#   Trendline Generator....136 - 201    #
#   Equation Generator.....203 - 217    #
#   Plot Generator.........219 - 282    #
#                                       #
#########################################

#Psudocode: Import Values, Check that thsoe values are valid, Generate the trendlines, plot them.
    #The trendline generator must be smart and be able to create different types of trendlines, and their equations. 

import math
import numpy as np
import matplotlib.pyplot as plt

def cfit(x,y,filename,flag,fitType):
    """
    'x' is the x-points
    'y' is the y-points
    'filename' is an external file loaction that can be loaded.
    'flag' determines wether to use the points given (1) or load from an external file (2).
    'fitType' is a string for the curve fit. It can be one of the following:
        'line' - straight line curve fit
        'log' - logrithmic curve fit
        'power' - power law curve fit
        'exp' - exponential curve fit
        'second' - second order polynomial curve fit
        'third' - third order polynomial curve fit
        'fourth' - fourth order polynomial curve fit
        'all' - all the curve fits listed above
        'best' - first and second options for best curve fits
    'temp' is a temporary variable that does various things throught the program, being constantly overwritten.
    
    Example Input: cfit(x,y,'data.txt',2,'all')
    Example Input: cfit(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),'dummy',1,'line')
    """

    temp = check(x,y,filename,flag,fitType)
    x,y,fitType = temp[0],temp[1],temp[2]
    if temp[3] == 1:
        if (fitType == 'all') or (fitType =='best'):
            temp = [(lineGenerator(x,y,'line'))]
            temp.append(lineGenerator(x,y,'log'))
            temp.append(lineGenerator(x,y,'power'))
            temp.append(lineGenerator(x,y,'exp'))
            temp.append(lineGenerator(x,y,'second'))
            temp.append(lineGenerator(x,y,'third'))
            temp.append(lineGenerator(x,y,'fourth'))
            if fitType == 'best':
                temp = optimizer(np.transpose(np.array(temp)).tolist())
            else:
                temp = np.transpose(np.array(temp)).tolist()
                temp[1] = (np.array(temp[1]).flatten().tolist())
        else:
            temp = lineGenerator(x,y,fitType)
        showplots(x,y,temp,fitType)
        eqn = temp[1]
        r2 = temp[0][1]
        return eqn,r2
    else: print('failed the check') #program ends
       
#The Black Box
def check(x,y,filename,flag,fitType):
    """This checks that the inputs will work.
    'x' is the flagged x list to use.
    'y' is the flagged y list to use.
    'n' is wether the other checks failed or not.
    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """
    n = 1

    if flag == 2:
        data = np.loadtxt(filename)
        x = data[:,0]
        y = data[:,1]
    if len(x) > len(y):
        print('Your x-list is larger than your y-list.')
        n = 0
    elif len(y) > len(x):
        print('Your y-list is larger than your x-list.')
        n = 0
    if type(x) != np.ndarray:
        print("Your x-list is not an np.array. I'll fix that for you")
        x = np.array(x)
    if type(y) != np.ndarray:
        print("Your y-list is not an np.array. I'll fix that for you")
        y = np.array(x)
    fitType = fitType.lower() #Gets rid of any accidental caps for you
    if fitType not in ('line','log','power','exp','second','third','fourth','all','best'):
        print('I do not understand the fitType you gave me. Please make sure you spelled it correctly.')
        n = 0
    return [x,y,fitType,n]

def lineGenerator(x,y,fitType):
    """This determines which type of trendline(s) should be computed."""
    
    if (fitType == 'line') or (fitType == 'log') or (fitType == 'power') or (fitType == 'exp'):
        solved = trendline(x,y,fitType)
        eqn = equation(solved,fitType)
    elif fitType == 'second':
        solved = trendline(x,y,2)
        eqn = equation(solved,fitType)
    elif fitType == 'third':
        solved = trendline(x,y,3)
        eqn = equation(solved,fitType)
    elif fitType == 'fourth':
        solved = trendline(x,y,4)
        eqn = equation(solved,fitType)

    return [solved,[eqn]]

def optimizer(myList):
    """Finds the best two fits for the trendlines"""
    eqns = np.transpose(np.array(myList[1])).tolist()
    myList = np.transpose(np.array(myList[0])).tolist()
    solvedMax,r2Max,eqnMax = [],[],[]
    for i in range(2):
        n = np.array(myList[1]).flatten().argmax()
        solvedMax.append(myList[0][i])
        r2Max.append(myList[1][i])
        eqnMax.append(eqns[0][i])
        myList[1][n] = [0]
        myList[0][n] = [0]
    return [[solvedMax,r2Max],eqnMax]

def trendline(x,y,fitType):
    """This creates various types of trendlines from lists of data in the form of numpy arrays.
    It returns the a & b values as a list, as well as the r2 value.

    Example Input: trendline(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),'line')
    """
    if type(fitType)==str:
        n = len(x)
        if fitType == 'line':
            sumx = np.sum(x)
            sumy = np.sum(y)
            sumxy = np.sum(x*y)
            sumx2 = np.sum(x**2)
            sumy2 = np.sum(y**2)
            
        elif fitType == 'power':
            sumx = np.sum(np.log(x))
            sumy = np.sum(np.log(y))
            sumxy = np.sum(np.log(x)*np.log(y))
            sumx2 = np.sum(np.log(x)**2)
            sumy2 = np.sum(np.log(y)**2)

        elif fitType == 'exp':
            sumx = np.sum(x)
            sumy = np.sum(np.log(y))
            sumxy = np.sum(x*np.log(y))
            sumx2 = np.sum(x**2)
            sumy2 = np.sum(np.log(y)**2)

        elif fitType == 'log':
            sumx = np.sum(np.log(x))
            sumy = np.sum(y)
            sumxy = np.sum(np.log(x)*y)
            sumx2 = np.sum(np.log(x)**2)
            sumy2 = np.sum(y**2)

        A = np.array([[n,sumx],[sumx,sumx2]])
        b = np.array([[sumy],[sumxy]])
        solved = np.linalg.solve(A,b)      
        r2 = (solved[0,0]*sumy+solved[1,0]*sumxy-1/n*sumy**2)/(sumy2-1/n*sumy**2)

        if fitType == 'power': solved[0,0] = np.exp(solved[0,0])
        elif fitType == 'exp': solved[0,0] = np.exp(solved[0,0])

            
    else:
        #The fitType is the order that the polynomial is.
        sumxList,sumyList,b,r2 = [],[],[],0
        n = len(x)
        A = [[n]]
        for i in range(fitType*2): #Create a list that ranges from x^1 to x^n
            sumxList.append(np.sum(x**(i+1)))
            sumyList.append(np.sum(x**(i)*y))      
        for i in range(fitType): #Initialize the A
            A.append([sumxList[i]])        
        for j in range(fitType+1):#Set up the A and b
            for i in range(fitType):
                A[j].append(sumxList[i+j])
            b.append(sumyList[j])        
        A = np.array(A)
        b = np.array(b).transpose()
        solved = np.linalg.solve(A,b)
        for i in range(fitType+1):
            r2 += solved[i]*sumyList[i]
        r2 = (r2-sumyList[0]**2/n)/(np.sum(y**2)-1/n*sumyList[0]**2)
    return [solved.tolist(),[r2]]

def equation(solved,fitType):
    """This creates an equation for the trendline
    Example Input: equation([[[7.7307334109429595], [1.7776484284051208]], 0.99394696088416035],'line')"""
    
    if fitType == 'line': eqn = ('y='+str(solved[0][0][0])+'+'+str(solved[0][1][0])+'*x')
    elif fitType == 'power': eqn = ('y='+str(solved[0][0][0])+'*x**('+str(solved[0][1][0])+')')
    elif fitType == 'exp': eqn = ('y='+str(solved[0][0][0])+'*np.exp('+str(solved[0][1][0])+'*x)')
    elif fitType == 'log': eqn = ('y='+str(solved[0][0][0])+'+'+str(solved[0][1][0])+'*np.log(x)')
    else: 
        if fitType == 'second': n = 2
        elif fitType == 'third': n = 3
        elif fitType == 'fourth': n = 4
        eqn = 'y='+str(solved[0][0])+'+'+str(solved[0][1])+'*x'
        for i in range(n-1): eqn += '+'+str(solved[0][i+2])+'*x**'+str(i+2)
    return eqn

def showplots(xlist,ylist,answer,fitType):
    """This creates a dynamic plot(s) for the trendlines.

    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """
    myLegends = ['given']
    h = 50 #step scalar
    x = np.arange(xlist.min(),xlist.max(),(xlist.max()-xlist.min())/h)
    plt.figure(1,figsize=(8,4))
    plt.plot(xlist,ylist,'ko')
    for j in range(len(answer[1])):
        if j<7:
            if j%2 == 0:
                if j == 0: lnStl = 'Purple'
                elif j == 2: lnStl = 'OrangeRed'
                elif j == 4: lnStl = 'y-'
                elif j == 6: lnStl = 'b-'
            else:
                if j == 1: lnStl = 'r-'
                elif j == 3: lnStl = 'Orange'
                elif j == 5: lnStl = 'g-'
        else: lnStl = 'w--'
        if fitType == 'best':
            plt.figure(2,figsize=(16,8))
            plt.subplot(2,1,j+1)
            if 'e**' in answer[1][j]: myLegends.append('exp')
            elif 'log' in answer[1][j]: myLegends.append('log')
            elif '**4' in answer[1][j]: myLegends.append('fourth')
            elif '**3' in answer[1][j]: myLegends.append('third')
            elif '**2' in answer[1][j]: myLegends.append('second')
            elif '**' in answer[1][j]: myLegends.append('power')
            else: myLegends.append('line')
        elif fitType == 'all':
            plt.figure(2,figsize=(16,8))
            plt.subplot(3,3,j+1)
            if j == 0: myLegends.append('line')
            elif j == 1: myLegends.append('log')
            elif j == 2: myLegends.append('power')
            elif j == 3: myLegends.append('exp')
            elif j == 4: myLegends.append('second')
            elif j == 5: myLegends.append('third')
            elif j == 6: myLegends.append('fourth')
        else: myLegends.append(fitType)
        plt.plot(xlist,ylist,'ko')        
        plt.plot(x,eval(answer[1][j].strip('y=')),lnStl)
        plt.figure(1)
        plt.plot(x,eval(answer[1][j].strip('y=')),lnStl)       
    plt.figure(1)
    plt.legend(myLegends)
    if fitType == 'best':
        plt.figure(2)
        for j in range(len(answer[1])):
            plt.subplot(2,1,j+1)
            plt.legend(['given',myLegends[j+1]])
    elif fitType == 'all':
        plt.figure(2)
        for j in range(len(answer[1])):
            plt.subplot(3,3,j+1)
            plt.legend(['given',myLegends[j+1]])
    if fitType in ('all','best'):
        plt.figure(1).canvas.set_window_title('All Lines')
        plt.figure(2).canvas.set_window_title('Individual Lines')
    else: plt.figure(1).canvas.set_window_title('Curve Fit')
    plt.show()














