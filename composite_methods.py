import numpy as np
from scipy import integrate



def eval_function(x):
    return (1/(1+(x)**2))

def trapezoidal_composite(a,b,n):
    h = (b-a)/n

    sum1 = 0
    for j in range(1, n+1):
        sum1 += eval_function(a + j*h)

    result = (h/2)*(eval_function(a) + 2*sum1 + eval_function(b))
    return result

def simpson_composite(a,b,n):
    if(n%2 != 0):
        print("Need n to be even")
        return

    h = (b-a)/n
    point_arr = np.linspace(a,b,n)

    #first sum f(x_{2j})
    sum1 = 0
    for j in range(1, int(n/2)):
        sum1 += eval_function(point_arr[2*j])

    sum2 = 0
    for j in range(1, int(n/2) + 1):
        sum2 += eval_function(point_arr[2*j-1])

    
    result = (h/3)*(eval_function(a) + 2*sum1 + 4*sum2 + eval_function(b))
    return result


def gaussian_quadrature():
    pass



def main():
    r_trap = trapezoidal_composite(-5,5,5*100)
    r_simp = simpson_composite(-5,5,5*100)

    f = lambda x: 1/(1+(x)**2)
    res_calc = integrate.quadrature(f, -5.0, 5.0, tol=10**(-4))

    i = 1000
    while(True):
        if(abs(res_calc[0] - trapezoidal_composite(-5,5,i)) < 10**(-4)):
            print("n-value for trapezoidal:" + str(i))
            break
        else:
            print(i)
            i += 2
    

    #print(res_calc[0])
    #print("Trapezoidal Error :" + str(abs(res_calc[0] - r_trap)))
    #print("Simpson's Error   :" + str(abs(res_calc[0] - r_simp)))


main()