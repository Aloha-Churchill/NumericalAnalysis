
from scipy import integrate
import math
import numpy as np




# Trapezoidal Method

# Define function to integrate
def f(x):
    return math.sin(1/x)

# Implementing trapezoidal method
def trapezoidal(x0,xn,n):
    # calculating step size
    n = n*5
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    

def simpson():
    pass

def gauss_quad():
    f = lambda x: x**8
    integrate.quadrature(f, 0.0, 1.0)


def computer_trapezoidal():
    x = np.linspace(-2, 2, num=20)
    y = x
    y_int = integrate.cumulative_trapezoid(y, x, initial=0)


# TRAPEZOIDAL
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )