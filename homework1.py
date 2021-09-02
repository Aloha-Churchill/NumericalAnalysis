#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


coeff_array = np.poly(np.full(9,2))
eval_array = np.linspace(1.92,2.08,100)

### Question 1
## a
# i - Personal Algorithm: iterates through expanded formula and calculates result
def myEvaluate(p):
    exp = 9
    ans = 0
    num_coeffs = len(coeff_array)
    for i in range(num_coeffs):
        ans += coeff_array[i]*p**exp
        exp = exp-1
    return ans

# ii - Compact form p(x) = (x-2)^9
def compactEvaluate(p):
    ans = (p-2)**9
    return ans

# iii - Horner's rule: recursive implementation
def hornerEvaluate(p, coeff_index):
    if coeff_index == 0:
        return coeff_array[0]
    return coeff_array[coeff_index] + p*hornerEvaluate(p, coeff_index - 1)

# iv - Software Library
def libraryEvaluate():
    return np.polyval(coeff_array, eval_array)

# method to aggregate arrays into one return statement
def create_arrays():
    my_eval_result = []
    compact_eval_result = []
    horner_eval_result = []
    num_iterations = len(eval_array)
    for i in range(num_iterations):
        my_eval_result.append(myEvaluate(eval_array[i]))
        compact_eval_result.append(compactEvaluate(eval_array[i]))
        horner_eval_result.append(hornerEvaluate(eval_array[i], 9))
    
    return my_eval_result, compact_eval_result, horner_eval_result

# plots different results
def plot():
    a, b, c = create_arrays()
    plt.plot(eval_array, libraryEvaluate(), 'yellow')
    plt.plot(eval_array, a, 'red')
    plt.plot(eval_array, b, 'blue')
    plt.plot(eval_array, c, 'green')
    plt.legend()
    plt.xlabel('input')
    plt.ylabel('result')
    plt.show()

plot()