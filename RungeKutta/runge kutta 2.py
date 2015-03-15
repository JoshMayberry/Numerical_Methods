import math

def slope(t,y):
    """dy/dt=y*sin^3(t)"""
    global count
    count +=1
    return y*math.sin(t)**3

def rk(fn,t,y,tfinal,h=1):
    global count
    count = 0
    for i in range(tfinal):
        #print('t',t,'y',y)
        k1 = fn(t,y)     
        k2 = fn(t+h/2,y+h/2*k1)
        k3 = fn(t+h/2,y+h/2*k2)
        k4 = fn(t+h,y+h*k3)        
        t += h
        y += h/6*(k1+2*k2+2*k3+k4)
        #print('k',k1,k2,k3,k4,'\n')
    return (y,t,count)
