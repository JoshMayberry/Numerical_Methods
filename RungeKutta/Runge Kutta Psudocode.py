Write function as dy/dt = (   )
Get initial values for t & y
Loop:
    Put those values into the function dt/dt and let that be k1.
    Calculate new values for t & y
        tnew = t+1/2*h
        ynew = 1/2*k1*h
    Put those values into dy/dt and let it be k2.
    Calculate new values for t and y
    Calculate k3
    Calculate new values for t and y
    Calculate k4
    ynew = yold + 1/6*(k1+2*k2+2*k3+k4)*h
    tnew = told + h
