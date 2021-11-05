from scipy import integrate
import math
import numpy as np


#actual_result = integrate.quad(lambda x: math.sin(1/x), 0.1,2.0)

actual_result = 1.145580834099501

def trapezoidal(n):
    x = np.linspace(0.1, 2.0, n*5)
    y = np.sin(1/x)
    y_int = integrate.trapezoid(y, x)
    return y_int

def simpson(n):
    x = np.linspace(0.0, 1.0, 5)
    #y = np.sin(1/x)
    y = x*np.cos(1/x)
    y_int = integrate.simpson(y, x)
    return y_int

def gauss_quad(n):
    f = lambda x: np.sin(1/x)
    #tol=10**(-3)
    res = integrate.quadrature(f, 0.1, 2.0,maxiter=n*5)
    return res



def main():
    
    desired_error = 10**(-3)
    n = 1

    while (gauss_quad(n)[1] > desired_error):
        n = n+1
    

    

    print(gauss_quad(n))
    #print("Error is:" + str(actual_result - gauss_quad()))
    print("Iterations: " + str(n))


simpson(5)