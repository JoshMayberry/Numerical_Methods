def ridders_methood():
    Gaurntees the root stays bracketed (unlike secant)
    Has similar efficency to secant methood.

    Limitation: requires endpoints to have opposite signs for the functional values (ex: x1 is + and x2 is -).

    Loop:
        x3 = (x1+x2)/2
        x4 = (x3+(x3-x1)*Sign(f(x1)-f(x2))*f(x3))/math.sqrt(f(x3)**2-f(x1)*f(x2))
            #if x<0 then np.sign(x) = -1         or math.copysign(x)
            #if x>0 then np.sign(x) = 1
            #if x=0 then np.sign(x) = 0

        Now, select new endpoints: x4 and
            x3 if f(x3)*fx(4)<0
            x1 or x2, whichever has the opposite sign (f(x1) or f(x2) from f(x4).
        Make those endpoints x1 and x2
