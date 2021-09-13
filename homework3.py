import math
import matplotlib.pyplot as plt
import numpy as np

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


def main():
    start_val_arr = np.linspace(-5,10,100)
    for s in start_val_arr:
        print(str(s) + " -->")
        fixed_point_iteration(f, s, 10**(-10), 0, 100)


#plotFunction()
main()
