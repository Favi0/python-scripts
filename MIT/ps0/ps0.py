import numpy as np
"""
    Write a program that does the following in order:
        1.Asks the user to enter a number “x”
        2.Asks the user to enter a number “y”
        3.Prints out number “x”, raised to the power “y”.
        4.Prints out the log (base 2) of “x”.
"""

x = int(input("Please, enter a number x: "))
y = int(input("Please, enter a number y: "))
print("X =",x,"raised to the power of Y =",y,"is",x**y)
print("The log(base2) of X = {0} is {1}".format(x,np.log2(x)))
