Gauss Psudocode

Have the function import two equations from equations.py
Have the user input an initial guess for one of them.
x = Do f2(user_input_guess)
Loop till % error is small:
    y = f1(x)
    x = f2(y)
If the error keeps getting larger, then switch the functions.
Display the intercection point to the user.


Class Psudocode

input functions
input # of functions
input initial guess
While error>desired error:
    for i in range(#of functions)
        solve each function
        calculate error
            (x2-x1)/(y2-y1) = % error
        check for divergence
