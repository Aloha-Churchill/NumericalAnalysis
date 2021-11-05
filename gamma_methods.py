import math
from scipy import integrate
import numpy as np
import timeit

def actual_gamma(x):
    return math.gamma(x)

#truncating interval of integration with composite trapezoidal
def truncate_integrate(truncation, n, x):
    t = np.linspace(0.0, truncation, n)
    y = np.power(t,x-1)*np.exp(-t)

    start = timeit.timeit()
    y_int = integrate.trapezoid(y, t)
    end = timeit.timeit()

    print("Total time taken: " + str(abs(end-start)))
    return y_int


def main():
    x_vals = np.linspace(2,10,5)
    print(x_vals)

    for x in x_vals:
        
        ci = actual_gamma(x)
        print("------------x: " + str(x))
        ti = truncate_integrate(100,1000,x)
        print("Error:" + str(abs(ti-ci)))
    
    """
        for x in x_vals:
        truncation_bound = 10
        n = 5
        while(abs(truncate_integrate(truncation_bound,n,x) - actual_gamma(x)) > 10**(-3)):
            truncation_bound += 10

            truncation_bound = 10
    


    n = 5
    truncation_bound = 10

    while(abs(truncate_integrate(truncation_bound,n,2) - actual_gamma(2)) > 10**(-3)):
        print("Error is: " + str(abs(truncate_integrate(truncation_bound,n,2) - actual_gamma(2))))
        truncation_bound += 10
    """

    #print(truncate_integrate(10,10000,2))
    #print(actual_gamma(2))

main()
