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
    x,y = temp[0],temp[1]
    if temp[2] == 1:
        #print('check worked')
        if (fitType == 'all') or (fitType =='best'):
            temp = [(lineGenerator(x,y,'line'))]
            temp.append(lineGenerator(x,y,'log'))
            temp.append(lineGenerator(x,y,'power'))
            temp.append(lineGenerator(x,y,'exp'))
            temp.append(lineGenerator(x,y,'second'))
            temp.append(lineGenerator(x,y,'third'))
            temp.append(lineGenerator(x,y,'fourth'))
            if fitType == 'best':
                #print ('best')
                temp = optimizer(np.transpose(np.array(temp)).tolist())
                print('from optimizer: ',temp)
            else:
                temp = np.transpose(np.array(temp)).tolist()
                temp[1] = (np.array(temp[1]).flatten().tolist())
        else:
            temp = lineGenerator(x,y,fitType)
        showplots(x,y,temp)
        eqn = temp[1]
        r2 = temp[0][1]
        #return eqn,r2
    else:
        print('failed the check')
       
#The Black Box
def check(x,y,filename,flag,fitType):
    """This checks that the inputs will work.
    'x' is the flagged x list to use.
    'y' is the flagged y list to use.
    'n' is wether the other checks failed or not.
    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """

    if flag == 1:   
        if len(x) > len(y):
            print('Your x-list is larger than your y-list.')
        elif len(y) > len(x):
            print('Your y-list is larger than your x-list.')
        if type(x) != np.ndarray:
            print('Your x-list is not an np.array')
        if type(y) != np.ndarray:
            print('Your y-list is not an np.array')
    else:
        data = np.loadtxt(filename)
        x = data[:,0]
        y = data[:,1]
    #Check for multi-dimensionsal
    #Check that there are not too many choices

    #Have it return wether or not it is good. If not, the whole thing stops.       
    n = 1
    return [x,y,n]

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
    #print(myList,'\n')
    #print(myList[0],'\n')
    #print(myList[1],'\n')
    solvedMax,r2Max,eqnMax = [],[],[]
    for i in range(2):
        n = np.array(myList[1]).flatten().argmax()
        solvedMax.append(myList[0][i])
        r2Max.append(myList[1][i])
        eqnMax.append(eqns[0][i])
        myList[1][n] = [0]
        myList[0][n] = [0]
    #print('optimized: ', solvedMax,r2Max,eqn)
    return [[solvedMax,r2Max],eqnMax]

def trendline(x,y,eqnType):
    """This creates various types of trendlines from lists of data in the form of numpy arrays.
    It returns the a & b values as a list, as well as the r2 value.

    Example Input: trendline(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),'line')
    """
    #print(x,y)
    #print(eqnType)
    if type(eqnType)==str:
        n = len(x)
        if eqnType == 'line':
            sumx = np.sum(x)
            sumy = np.sum(y)
            sumxy = np.sum(x*y)
            sumx2 = np.sum(x**2)
            sumy2 = np.sum(y**2)
            
        elif eqnType == 'power':
            sumx = np.sum(np.log(x))
            sumy = np.sum(np.log(y))
            sumxy = np.sum(np.log(x)*np.log(y))
            sumx2 = np.sum(np.log(x)**2)
            sumy2 = np.sum(np.log(y)**2)

        elif eqnType == 'exp':
            sumx = np.sum(x)
            sumy = np.sum(np.log(y))
            sumxy = np.sum(x*np.log(y))
            sumx2 = np.sum(x**2)
            sumy2 = np.sum(np.log(y)**2)

        elif eqnType == 'log': #This one doesn't work
            sumx = np.sum(np.log(x))
            sumy = np.sum(y)
            sumxy = np.sum(np.log(x)*y)
            sumx2 = np.sum(np.log(x)**2)
            sumy2 = np.sum(y**2)

        A = np.array([[n,sumx],[sumx,sumx2]])
        b = np.array([[sumy],[sumxy]])
        solved = np.linalg.solve(A,b)      
        r2 = (solved[0,0]*sumy+solved[1,0]*sumxy-1/n*sumy**2)/(sumy2-1/n*sumy**2)

        if eqnType == 'power':
            solved[0,0] = np.exp(solved[0,0])
        elif eqnType == 'exp':
            solved[0,0] = np.exp(solved[0,0])
            #y = e(y)
            
    else:
        #The eqnType is the order that the polynomial is.
        sumxList,sumyList,b,r2 = [],[],[],0
        n = len(x)
        A = [[n]]
        for i in range(eqnType*2): #Create a list that ranges from x^1 to x^n
            sumxList.append(np.sum(x**(i+1)))
            sumyList.append(np.sum(x**(i)*y))
        
        for i in range(eqnType): #Initialize the A
            A.append([sumxList[i]])
        
        for j in range(eqnType+1):#Set up the A and b
            for i in range(eqnType):
                A[j].append(sumxList[i+j])
            b.append(sumyList[j])
        
        A = np.array(A)
        b = np.array(b).transpose()

        #Solve it
        solved = np.linalg.solve(A,b)

        for i in range(eqnType+1):
            r2 += solved[i]*sumyList[i]
        r2 = (r2-sumyList[0]**2/n)/(np.sum(y**2)-1/n*sumyList[0]**2)
    return [solved.tolist(),[r2]]

def equation(solved,fitType):
    """This creates an equation for the trendline
    Example Input: equation([[[7.7307334109429595], [1.7776484284051208]], 0.99394696088416035],'line')"""
    #print(solved)
    
    if fitType == 'line':
        eqn = ('y='+str(solved[0][0][0])+'+'+str(solved[0][1][0])+'*x')
    elif fitType == 'power':
        eqn = ('y='+str(solved[0][0][0])+'*x**('+str(solved[0][1][0])+')')
    elif fitType == 'exp':
        eqn = ('y='+str(solved[0][0][0])+'*np.exp('+str(solved[0][1][0])+'*x)')
    elif fitType == 'log':
        eqn = ('y='+str(solved[0][0][0])+'+'+str(solved[0][1][0])+'*np.log(x)')
    else: 
        if fitType == 'second': n = 2
        elif fitType == 'third': n = 3
        elif fitType == 'fourth': n = 4
        eqn = 'y='+str(solved[0][0])+'+'+str(solved[0][1])+'*x'
        for i in range(n-1):
            eqn += '+'+str(solved[0][i+2])+'*x**'+str(i+2)
    #print(eqn,'\n')
    return eqn

def showplots(xlist,ylist,answer):
    """This creates a dynamic plot(s) for the trendlines.

    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """
    print('\nshowplots: ', answer,'\n')
    h = 50 #step scalar
    x = np.arange(xlist.min(),xlist.max(),(xlist.max()-xlist.min())/h)
    plt.figure(1)
    plt.plot(xlist,ylist,'k-')
    for j in range(len(answer[1])):
        if j<6:
            if j%2 == 0:
                if j == 0: lnStl = 'Purple'
                elif j == 2: lnStl = 'Orange'
                elif j == 4: lnStl = 'g-'
            else:
                if j == 1: lnStl = 'r-'
                elif j == 3: lnStl = 'y-'
                elif j == 5: lnStl = 'b-'
        else:
            lnStl = 'w--'
        #print(answer[1][j])
        #print(np.transpose(answer[j]).tolist())
        #print(eval(answer[1][j].strip('y=')))
        print(answer[1][j])
        plt.plot(x,eval(answer[1][j].strip('y=')),lnStl)
    plt.show()














