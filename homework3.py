import math
import matplotlib.pyplot as plt
import numpy as np


############################## Problem 2 ####################################

def plotFunction():
    x = np.linspace(-5,10,100)
    y = x-4*np.sin(2*x) - 3

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.grid(True, which='both')

    ax.spines['left'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    ax.spines['bottom'].set_position('zero')

    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    plt.show()


def f(x):
    return (-1*math.sin(2*x) + 5*x/4 - 3/4)

def fixed_point_iteration(function, val, error_bound, iter, max_iter):
    if(abs(val - function(val)) < error_bound):
        print("Value to at least error " + str(error_bound) + "places is:" + str(val))
        return val
    if(iter >= max_iter):
        print("Did not converge within error bound. Value is " +  str(val) + ", error is " + str(abs(val - function(val))))
        return val
    else:
        #print("New value is: " + str(function(val)))
        return fixed_point_iteration(function, function(val), error_bound, iter+1, max_iter)


def main_problem_2():
    start_val_arr = np.linspace(-5,10,100)
    for s in start_val_arr:
        print(str(s) + " -->")
        fixed_point_iteration(f, s, 10**(-10), 0, 100)

#plotFunction()

####################################### Problem 3 ########################################

def plot_soil_function():
    x = np.linspace(0, 5, 100)
    y = []
    alpha, t, T_i, T_s = 0.138*10**(-6), 60*24*3600, 20, -15
    for num in x:
        y.append(math.erf(num/(2*math.sqrt(alpha*t)))*(T_i - T_s) + T_s)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.grid(True, which='both')

    ax.spines['left'].set_position('zero')

    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    ax.spines['bottom'].set_position('zero')

    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    plt.show()

def soil_function(x):
    alpha, t, T_i, T_s = 0.138*10**(-6), 60*24*3600, 20, -15
    return (math.erf(x/(2*math.sqrt(alpha*t)))*(T_i - T_s) + T_s)


#uses bisection method to find root within a specified tolerance
def bisect(f,a,b,tol):
    num_iterations = 0

    #max iteration is terminating point
    max_iterations = 100

    mid = (a+b)/2

    while ((b-a)/2 > tol and num_iterations < max_iterations):
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

def use_bisection():
    result, iterations = bisect(soil_function, 0, 5, 10**(-13))
    print("Result: " + str(result))
    print("Iterations: " + str(iterations)) 


def soil_deriv(x):
    alpha, t, T_i, T_s = 0.138*10**(-6), 60*24*3600, 20, -15
    return (((T_i-T_s)/math.sqrt(math.pi*alpha*t))*math.exp(-1*(x/(2*math.sqrt(alpha*t))**2)))



## Newton's method code from https://personal.math.ubc.ca/~pwalls/math-python/roots-optimization/newton/
def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

#use_bisection()

#pun intended
soilution = newton(soil_function, soil_deriv, 0.01, 10**(-13), 100)

print(soilution)
