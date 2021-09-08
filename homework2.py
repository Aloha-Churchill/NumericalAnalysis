import numpy as np
import math
import time

#evaluates f(x) = 2x-1-sin(x)
def f0(x):
    return (2*x-1-math.sin(x))

#evaluates compact form of function (x-5)^9
def f1(x):
    return ((x-5)**9)

#evaluates expanded form of function (x-5)^9
def f2(x):
    coeff_arr = np.poly(np.repeat(5, 9))
    res = 0
    n = len(coeff_arr)
    for coeff in coeff_arr:
        res += coeff*(x**n)
        n -= 1 
    return res

def f3(x):
    return (x**3 + x - 4)

#uses bisection method to find root within a specified tolerance
def bisect(f,a,b,tol):
    num_iterations = 0

    #max iteration is terminating point
    max_iterations = 100
    
    mid = (a+b)/2

    #this is the correct root for (x-5)^9
    correct_root = 5

    while ((b-a)/2 > tol and num_iterations < max_iterations): # or could use abs(mid-correct_root) > tol
        num_iterations += 1
        if(f(mid) < 0):
            #guess greater number
            b = b
            a = mid
            mid = (a+b)/2
        else:
            #guess smaller number
            a = a
            b = mid
            mid = (a+b)/2
    

    return mid, num_iterations

def problem3c():
    result, iterations = bisect(f0, 0, math.pi/2, 10**(-8))
    print("Result: " + str(result))
    print("Iterations: " + str(iterations)) 

def main():
    result, iterations = bisect(f3, 1, 4, 10**(-3))
    print("Result: " + str(result))
    print("Iterations: " + str(iterations))

    #result, iterations = bisect(f2, 4.82, 5.2, 10**(-3))
    #print("Result with Expanded Evaluation: " + str(result))
    #print("Iterations: " + str(iterations))

#problem3c()
main()
