import math
import matplotlib.pyplot as plt
import numpy as np

def eval_f(x,y,z):
    return (x**2 - 4*y**2 + 4*z**2 - 16)

def eval_dfx(x,y,z):
    return (2*x)

def eval_dfy(x,y,z):
    return (-8*y)

def eval_dfz(x,y,z):
    return (8*z)

def eval_d(x,y,z):
    return(eval_f(x,y,z)/(math.pow(eval_dfx(x,y,z), 2) + math.pow(eval_dfy(x,y,z), 2) + math.pow(eval_dfz(x,y,z), 2)))

def iterate(x0, y0, z0):
    err_x = []
    err_y = []
    err_z = []

    x_curr = x0
    y_curr = y0
    z_curr = z0

    x_root = 1.1879646925144265
    y_root = 0.15204294946012115
    z_root = 1.915803233846135

    for i in range(20):
        print("xn = " + str(x_curr))
        print("yn = " + str(y_curr))
        print("zn = " + str(z_curr))
        
        err_x.append(abs(x_curr - x_root))
        err_y.append(abs(y_curr - y_root))
        err_z.append(abs(z_curr - z_root))

        x_curr = x_curr - eval_d(x_curr, y_curr, z_curr)*eval_dfx(x_curr,y_curr, z_curr)
        y_curr = y_curr - eval_d(x_curr, y_curr, z_curr)*eval_dfy(x_curr,y_curr, z_curr)
        z_curr = z_curr - eval_d(x_curr, y_curr, z_curr)*eval_dfz(x_curr,y_curr, z_curr)
        

    plt.plot(np.arange(20), err_x)
    plt.plot(np.arange(20), err_y)
    plt.plot(np.arange(20), err_z)
    plt.show()

    print("X ERROR")
    print(err_x)
    print("Y ERROR")
    print(err_y)
    print("Z ERROR")
    print(err_z)


iterate(1,1,1)