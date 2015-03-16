import math
import numpy as np
import matplotlib.pyplot as plt

def ramuh(x,y,choices,plotTypes):
    """This is the user interface
    'x' is your list of x-axis variables
    'y' is your list of y-axis variables
    'choices' is an integer of how many top choices you want to view.
    'plotType' controls how the trendlines are shown in the end.
        0: all on the same plot
        1: all on different plots in the same window
        2: all on different windows that pop up all at once
        3: all on different windows that pop up one by one.

    Example Input: ramuh(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """

#[lineList,r2Max,nList,recomendation]
    print('Welcome to ramuh. I will be your guide for our journey in curve fitting.')
    print('I see you have given me some inputs. Let me check that they are indeed numpy arrays.')
    result = check(x,y,choices,plotTypes)
    print('Looks good. You asked for the best {0:2d} trendlines for this data. I would be happy to oblige.\n'.format(choices))
    answer = optimizer(x,y,choices)
    #i = 0
    #print('\nlineList',answer[0][i])
    #print('\nr2Max',answer[1][i])
    #print('\nnList',answer[2][i])
    #print('\nrecomendation',answer[3][i])
    #print('')
    for i in range(choices):
        print('Choice number {0:2d} comes from a '.format(i+1)+answer[2][i]+' trendline')
        print('The r2 value for it is, {0:1.5f}, which is '.format(answer[1][i])+answer[3][i])
        print('This trendline is: '+answer[0][i],'\n')
    print("Before I go, I'll let you check over the trendlines I choose. Here is a plot that contains them all.")
    showplots(x,y,answer,choices,plotTypes)
          
#The Black Box
def check(x,y,choices,plotTypes):
    """This checks that the inputs will work.

    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """

    if len(x) > len(y):
        print('Your x-list is larger than your y-list.')
    elif len(y) > len(x):
        print('Your y-list is larger than your x-list.')

    if type(x) != np.ndarray:
        print('Your x-list is not an np.array')
    if type(y) != np.ndarray:
        print('Your y-list is not an np.array')
    #Check for multi-dimensionsal
    #Check that there are not too many choices

    #Have it return wether or not it is good. If not, the whole thing stops.

def showplots(xlist,ylist,answer,choices,plotType):
    """This creates a dynamic plot(s) for the trendlines.

    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2,0)
    """
    
    h = 50 #step scalar
    x = np.arange(xlist.min(),xlist.max(),(xlist.max()-xlist.min())/h)
    if plotType == 0:
        plt.figure(1)
        plt.plot(xlist,ylist,'k-')
        for j in range(choices):
            if j<6:
                if j%2 == 0:
                    if j == 0:
                        lnStl = 'Purple'
                    elif j == 2:
                        lnStl = 'Orange'
                    elif j == 4:
                        lnStl = 'g-'
                else:
                    if j == 1:
                        lnStl = 'r-'
                    elif j == 3:
                        lnStl = 'y-'
                    elif j == 5:
                        lnStl = 'b-'
            else:
                lnStl = 'w--'
            plt.plot(x,eval(answer[0][j].strip('y=')),lnStl)
        plt.show()
    
          
def optimizer(x,y,choices):
    """This runs through the various trendlines and evaluates them.
    myList = [linear,power_law,logrtithmic,poly2,poly3,poly4]

    Example Input: optimizer(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),2)
    """
    
    myList,solvedMax,r2Max,nList,recomendation,lineList = [],[],[],[],[],[]
    myList.append(trendline(x,y,'linear'))
    myList.append(trendline(x,y,'power_law'))
    myList.append(trendline(x,y,'exponential'))
    myList.append(trendline(x,y,'logrithmic'))
    myList.append(trendline(x,y,3))
    myList.append(trendline(x,y,4))
    myList.append(trendline(x,y,5))
    myList = np.transpose(myList)[:]
    for i in range(choices):
        print(myList)
        n = myList[1].argmax()
        print(n)
        solvedMax.append(myList[0][i].tolist())
        r2Max.append(myList[1][i])
        if n == 0:
            nList.append('linear')
            lineList.append('y='+str(solvedMax[0][0][0])+'+'+str(solvedMax[0][1][0])+'*x')
        elif n == 1:
            nList.append('power law')
            lineList.append('y='+str(solvedMax[0][0][0])+'*x**('+str(solvedMax[0][1][0]))
        elif n == 2:
            nList.append('exponential')
            lineList.append('y='+str(solvedMax[0][0][0])+'*np.exp('+str(solvedMax[0][1][0])+'*x)')
        elif n == 3:
            nList.append('logrithmic')
            lineList.append('y='+str(solvedMax[0][0][0])+'+'+str(solvedMax[0][1][0])+'*np.log(x)')
        else:
            if n == 4:
                nList.append('2nd order polynomial')
                lineList.append('y='+str(solvedMax[0][0][0])+'+'+str(solvedMax[0][1][0])+'*x'+str(solvedMax[0][2][0])+'*x**2')
            elif n == 5:
                nList.append('3rd order polynomial')
                lineList.append('y='+str(solvedMax[0][0][0])+'+'+str(solvedMax[0][1][0])+'*x'+str(solvedMax[0][2][0])+'*x**2'+str(solvedMax[0][3][0])+'*x**3')
            else:
                nList.append(str(n-1)+'th order polynomial')
                temp = 'y='+str(solvedMax[0][0][0]+'+'+str(solvedMax[0][1][0])+'*x')
                for i in range(n-1):
                    temp += '+'+str(solvedMax[0][i+2][0])+'*x**'+str(i+2)
                lineList.append(tempStr)

        if r2Max[i] >= 0.999:
            recomendation.append('extremely good. I recommend using it.')
        elif r2Max[i] >= 0.99:
            recomendation.append('very good. I recommend using it.')
        elif r2Max[i] >= 0.98:
            recomendation.append('great. I recommend using it.')
        elif r2Max[i] >= 0.95:
            recomendation.append('good. You could use it.')
        elif r2Max[i] >= 0.90:
            recomendation.append('alright. You could still use it.')
        elif r2Max[i] >= 0.80:
            recomendation.append('not that good. You should re-take your data so I can provide you with a better trendline.')
        elif r2Max[i] >= 0.50:
            recomendation.append('bad. You should re-take your data so I can provide you with a useable trendline.')
        else:
            recomendation.append("horrible. I'm sorry it did not work out.")

        myList[1][n] = 0
        
    return [lineList,r2Max,nList,recomendation]

def trendline(x,y,eqnType):
    """This creates various types of trendlines from lists of data in the form of numpy arrays.

    Example Input: trendline(np.array([0.5,0.9,1.7,2.4]),np.array([8.7,9.3,10.6,12.1]),'linear')
    """
    if type(eqnType)==str:
        n = len(x)
        if eqnType == 'linear':
            sumx = np.sum(x)
            sumy = np.sum(y)
            sumxy = np.sum(x*y)
            sumx2 = np.sum(x**2)
            sumy2 = np.sum(y**2)
            
        elif eqnType == 'power_law':
            sumx = np.sum(np.log(x))
            sumy = np.sum(np.log(y))
            sumxy = np.sum(np.log(x)*np.log(y))
            sumx2 = np.sum(np.log(x)**2)
            sumy2 = np.sum(np.log(y)**2)

        elif eqnType == 'exponential':
            sumx = np.sum(x)
            sumy = np.sum(np.log(y))
            sumxy = np.sum(x*np.log(y))
            sumx2 = np.sum(x**2)
            sumy2 = np.sum(np.log(y)**2)

        elif eqnType == 'logrithmic': #This one doesn't work
            sumx = np.sum(np.exp(x))
            sumy = np.sum(y)
            sumxy = np.sum(np.exp(x)*y)
            sumx2 = np.sum(np.exp(x)**2)
            sumy2 = np.sum(y**2)

        A = np.array([[n,sumx],[sumx,sumx2]])
        b = np.array([[sumy],[sumxy]])
        solved = np.linalg.solve(A,b)      
        r2 = (solved[0,0]*sumy+solved[1,0]*sumxy-1/n*sumy**2)/(sumy2-1/n*sumy**2)

        if eqnType == 'power_law':
            solved[0,0] = np.exp(solved[0,0])
        elif eqnType == 'exponential':
            solved[0,0] = np.exp(solved[0,0])
            #y = e(y)
        elif eqnType == 'logrithmic':
            solved[0,0] = np.exp(solved[0,0])
            bAns = solved[1,0]
            #x = e(x)
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
    return [solved,r2]

















