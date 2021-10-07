from scipy.interpolate import barycentric_interpolate
import matplotlib.pyplot as plt
import numpy as np
import math



def main(N):
    x_observed = []
    x_chebyshev = []
    y_observed = []
    y_chebyshev = []

    for i in range(1, N):
        h=2/(N-1)
        x_observed.append(-1+(i-1)*h)
        y_observed.append(1/(1+(10*x_observed[i-1])**2))

        x_chebyshev.append((math.cos(2*i-1)*math.pi)/(2*N))
        y_chebyshev.append(1/(1+(10*x_chebyshev[i-1])**2))

    
    x = np.linspace(min(x_chebyshev), max(x_chebyshev), num =100)
    y = barycentric_interpolate(x_chebyshev,y_chebyshev, x)

    print(y)

    plt.plot(x_chebyshev, y_chebyshev, "o", label = "observation")
    plt.plot(x,y, label = "barycentric interpolation")

    plt.legend()
    plt.show()

main(1000000)
