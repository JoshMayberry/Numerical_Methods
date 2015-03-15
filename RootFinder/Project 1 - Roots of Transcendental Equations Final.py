import math
import numpy as np
import equations as eq

#Run This Program
def gaia(fn,nroots,edes=1):
    """This runs evrything to find the as many roots as you want.
    This program has been sucessfully tested for up to 5000 roots for both Sin() and Tan() functions that have roots after zero.

    'fn' is the name of your function in 'equations.py'.
    'nroots' is how many roots you want.
    'edes' is your desired error. When showing 4 decimal places, the default desired error is enough.
    Example Input: project1(eq.eq1,5000,0.01)
    """
    global count
    print("Welcome, mortal. I require a few constants to divine thine function.")
    ask_for_constants()
    while last_check()==1:
        ask_for_constants()
    count = 0 #Resets the counter to zero.
    (xlist,errorlist) = find_first_root(fn,edes)
    slopelist = find_where_slope_is_zero(fn,xlist)
    periodlist = find_period_of_function(fn,slopelist,nroots)
    (xlist,errorlist) = use_period_to_find_all_others(fn,periodlist,xlist,errorlist,edes)
    report_results(xlist,nroots,count,errorlist)

def f(fn,x):
    """This calls the desired equation from equations.py
    Example Input: f(eq1,0.2)
    """
    global count
    count = count + 1
    fx = fn(x)
    return fx

def ri(eq,xlist,edes):
    """This is Ridder's Methood.
    Example Input: ri(eq1,[0.2,1.6])
    """
    x1,x2 = xlist[0],xlist[1]
    n = math.ceil(math.log(abs(x1-x2)/(edes/100))/math.log(2))
    for i in range(int(n)):
        f1,f2,x3 = f(eq,x1),f(eq,x2),(x1+x2)/2
        f3 = f(eq,x3)
        if f3**2-f1*f2 > 0:   #This makes the program not crash if an error happens for a root.
            x4 = x3+(x3-x1)*np.sign(f1-f2)*f3/math.sqrt(f3**2-f1*f2)
            f4 = f(eq,x4)
            if f3*f4<0:
                x1 = x3
                x2 = x4
            elif f1*f4<0:
                x1 = x1
                x2 = x4
            elif f2*f4<0:
                x1 = x4
                x2 = x2
        else:
            x4 = '???' #Defaults a zero for an error
    error = abs((x1-x2)/x2)*100
    return [x4,error]

def ask_for_constants():
    """This function asks the user for three constants. These constants are made to be global.
    Example Input: ask_for_constants()
    """
    print("I will ask for three constants: k, C, and Bi.\nIf thine function does not require one or two of these constants, type 'no'.\n")
    eq.k = input("What is thine 'k'? ")
    verify = 0
    while(verify==0):
        verify,eq.k = verify_constant(eq.k,0)
        if verify == 0:
            eq.k = input("What is thine 'k'? ")
    eq.C = input("What is thine 'C'? ")
    verify = 0
    while(verify==0):
        verify,eq.C = verify_constant(eq.C,1)
        if verify == 0:
            eq.C = input("What is thine 'C'? ")
    eq.Bi = input("What is thine 'Bi'? ")
    verify = 0
    while(verify==0):
        verify,eq.Bi = verify_constant(eq.Bi,2)
        if verify == 0:
            eq.C = input("What is thine 'Bi'? ")

def verify_constant(const,which):
    """This function verifies that the provided constants has roots after zero and is periodic.
    Example Input: verify_constants(eq.k,0)
    """
    verify = 1
    try:
        const = eval(const)
        if which == 0 and const == 0:
            print('This is a straight line. Repent.')
            verify = 0
        elif which == 1 and const == 0:
            print('Thou madest a covenant that such a value would not be given. Repent.')
            verify = 0
        elif which == 1 and const > 0:
            print('There are no roots for this sin() function. Repent.')
            verify = 0
        else:
            verify = 1
    except(SyntaxError,NameError,TypeError): #This is for if they leave it blank, put letters without '', change it from a number to a string, or put in a key word.
        if const == 'llama':
            verify = 1
        else:
            const = 'no'
            verify = 1
    return (verify,const)

def last_check():
    """This checks that the user did not enter all strings for the constants.
    It also looks for key words that produce easter eggs.
    The key word is 'llama'.
    Example Input: check_for_stupid()
    """
    if eq.k=='llama' or eq.C=='llama' or eq.Bi=='llama':
        print('Very well. Thou art easily entertained.\n           \\\\  // \n           \\\_/// \n         ?????//// \n        @@@@@@@@}}} \n     //|||||||||}}}} \n  \\\\\\\\\@@@//////}}}}} \n /////////////////}}}}} \n{{{{{{{{{{{{{{{{{{}}}}}} \n\\\\//_____//\\\\\\\\\\\\\\\\\\\}}}} \n           \\\\\\\\\\\\\\\\\\\\\}} \n           ////////////\\\\\\ \n          /////////////\\ \n         ///||||||||}}}}}} \n        }}}}}}}}}}}}}}}}\\ \n        /////////}}}}}}}}}}}}}} \n       //////////////////////]))))\\\\\________________////&& \n        \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\)))))))))))))))|||||||||||$$$$&&& \n        //////////////////////////////////???????????????&&&& \n       (((((((((((((((||||||||||||||||||||||||||)))))))))))))) \n        ||//llama/llama/llama/llama/llama/llama/llama/llama\\\\\\\\ \n       //////////////////////////////////////////////////////// \n        //llama/llama/llama/llama/llama/llama/llama/llama///// \n        ////////////////////////////////////////////////////// \n        llama/llama/llama/llama/llama/llama/llama/llama}}}}}}} \n         (((|||||||||||||||||||||||||//___))))))))))))))))}}} \n             (((\\\\\\\\\\\\\\\\||||//////          \\\\//////////))) \n                |||||||||||||||||            [[[{{{{{{{{{{ \n                  }}}}}} }}}}}}}              \\\\\\\\\\\|||))) \n                    }}}} }}}}}                 {{{{{ {{{}} \n                    ||||  ||||                 /////  \\\\\\ \n                    [[]]   [[]]                ////     \\\\ \n                    ///    ///                ///        \\\ \n                   ///   ////               ////          \\\ \n                 ///     //                 //           /// \n')
        failed = 1
    elif type(eq.k)==str and type(eq.C)==str and type(eq.Bi)==str:
        print('\nWhat ist thine malfunction? Thine offering contained no numbers. Repent.')
        failed = 1
    else:
        print('Thank you, mortal. I shall now divine thine function.\n')
        failed = 0
    return failed

def find_first_root(fn,edes):
    """This function finds the first root with brute force.
    Example Input: find_first_function(ex1)
    """
    x1 = 0
    x2 = 0.1
    xlist = find_two_opposite_signs(fn,x1,x2)
    ridders = ri(fn,xlist,edes)
    xroot1 = [ridders[0]]
    error1 = [ridders[1]]
    return [xroot1,error1]

def find_two_opposite_signs(fn,x1,x2):
    """This function finds two opposing signs.
    Example Input: find_two_opposite_signs(ex1,0,0.1)
    """
    f1 = f(fn,x1)
    f2 = f(fn,x2)
    while np.sign(f1) == np.sign(f2):
        x2 += 0.1
        f2 = f(fn,x2)
    return [x1,x2]

def find_where_slope_is_zero(eq,xlist):
    """This function finds the where the slope is equal to zero.
    Example Input: find_where_slope_is_zero(eq1,[0.2,0.6])
    """
    global tan
    x1 = xlist[0]+0.1
    y1 = f(eq,x1)
    tan = 0
    while round(y1/x1)!=0:
        x1+=0.1
        y1 = f(eq,x1)
    x2 = x1+0.2
    y2 = f(eq,x2)
    while np.sign(y2)==np.sign(y1):     #Corrects for tan()
        x2 += 1
        y2 = f(eq,x2)
        tan = 1
    while round(y2/x2)!=0:
        x2+=0.1
        y2 = f(eq,x1)
    return [x1,x2] 
    
def find_period_of_function(eq,slopelist,nroots):
    """This function finds the Period of the function.
    It then makes a list of x values that are that period apart.
    Example Input: find_period_of_function(eq1,[0.947969,1.278602])
    """
    global tan
    s1 = slopelist[0]
    s2 = slopelist[1]
    if tan == 1:
        T = 3.14159265359
    else:
        T = s2-s1
    periodlist = []
    for i in range(nroots):
        periodlist.append(s1+T*i)
    return periodlist

def use_period_to_find_all_others(eq,periodlist,xlist,errorlist,edes):
    """This function finds the roots using the period list as the xbounds.
    Example Input: use_period_to_find_all_others(eq1,[0.947,1.278,1.543,1.935,2.145],[0])
    """
    for i in range(len(periodlist)-1):
        ridders = ri(eq,[periodlist[i],periodlist[i+1]],edes)
        xlist.append(ridders[0])
        errorlist.append(ridders[1])
    return (xlist,errorlist)

def report_results(xlist,nroots,count,errorlist):
    """This function reports teh results to the user.
    Example Input: report_results([0.947,1.278,1.543],3,100,[1.4,1.5,1.6])
    """
    print('I have returned, and it only took me {0:3d} cycles- for I am all powerful. Thine {1:2d} roots are as follows:'.format(count,nroots))
    for i in range(nroots):
        if type(xlist[i])!= str: #No error was found in calculating
            if errorlist[i]== 100:
                print('The PDF thou sent thine students said the first root is zero. But thou said to them not report a root that is zero. So I will not.')
            else: 
                print('Root',i+1,'is {0:2.4f}. The error of this is {1:2.5}%.'.format(xlist[i],errorlist[i]))
        elif i != nroots-1: #Checks that there is a number after this one to average with the last.
            if xlist[i-1] != '???' and xlist[i+1] != '???': 
                print('Root',i+1,'is about {0:2.4f}. This was found using a linear average.'.format((xlist[i-1]+xlist[i+1])/2,))
            elif i != nroots-2:
                if xlist[i-2] != '???' and xlist[i+2] != '???': 
                    print('Root',i+1,'is about {0:2.4f}. This was found using a large linear average.'.format((xlist[i-2]+xlist[i+2])/2,))
                else: 
                    print('Thou art not worthy of root',i+1,'for it is above thine understanding.')
            else: 
                print('Thou art not worthy of root',i+1,'for it is above thine understanding.')
        else: 
            print('Thou art not worthy of root',i+1,'for it is above thine understanding.')
    print('Good luck on thine travels, mortal')







    
