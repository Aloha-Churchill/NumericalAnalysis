import math

sum = 0
x = 9.999999995*(10**(-10))

for i in range(1,11):
    sum += (x**i)*(1/(math.factorial(i)))

print(sum)
