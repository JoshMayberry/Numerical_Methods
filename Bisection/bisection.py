def equation (x):
    import math
    k = 10
    c = -1
    fx = x*math.sin(k*x)-x-c #This was x*math.sin(x)-x=c, but the c got moved so the equation =ed 0.
    return fx

def fn(x):
    fx = equation (x)
    return fx

def bi(mylist):
    """mylist is [x1,x2,edes]"""
    import math
    x1 = mylist[0]          #left bound
    x2 = mylist[1]          #right bound
    edes = mylist[2]/100    #desired %error
    n = math.log(abs(x1-x2)/edes)/math.log(2)
    print('edes: ',edes,'\nn: ',n)
    i = 0
    print('Just one moment...')
    for i in range(int(n)):
        xnew = (x1+x2)/2
        error = abs((x1-xnew)/xnew)*100
        check = fn(x1)*fn(xnew)
        if check > 0:
            x1 = xnew
        elif check < 0:
            x2 = xnew
        else:
            print('You broke something.')
            break
        #print('x1: ',x1,'\nx2: ',x2,'\nxnew: ',xnew,'\nerror: ',error,'\ncheck: ',check)
    print('approx. root: ',xnew,'\n%error: ',error)
