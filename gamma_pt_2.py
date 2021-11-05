import math
from scipy import integrate
import numpy as np
import timeit


def actual_gamma(x):
    return math.gamma(x)

def gauss_quad(n,x):

    f = lambda t: np.power(t,x-1)*np.exp(-t)
    #tol=10**(-3)
    res = integrate.quadrature(f, 0, 100 ,maxiter=n)
    return res



def main():
    
    x_vals = np.linspace(2,10,5)

    desired_error = 10**(-3)
    n = 1

    while (gauss_quad(n,2)[1] > desired_error):
        n = n+1
    

    

    print(gauss_quad(n,2))
    #print("Error is:" + str(actual_result - gauss_quad()))
    print("Iterations: " + str(n))

main()