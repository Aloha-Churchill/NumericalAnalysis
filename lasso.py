# code adapted from Kornel Kielczewski

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.metrics import mean_squared_error

clf = Lasso() #or set this to Lasso()

X, y, w = make_regression(
    n_samples=10, n_features=5, n_informative=5, coef=True, random_state=1, noise=50
)


coefs = []
errors = []

print(w)
lambdas = np.logspace(-6, 6, 200)

# Train the model with different regularisation strengths
for a in lambdas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
    #print(int(mean_squared_error(clf.coef_, w)))

print(coefs[0])
# Display results
plt.figure(figsize=(20, 6))

plt.subplot(121)
ax = plt.gca()
ax.plot(lambdas, coefs)


ax.set_xscale("log")
plt.xlabel("lambda")
plt.ylabel("weights")
plt.title("LASSO coefficients as a function of the regularization")
plt.axis("tight")

plt.subplot(122)
ax = plt.gca()
ax.plot(lambdas, errors)
ax.set_xscale("log")
plt.xlabel("lambda")
plt.ylabel("error")
plt.title("Coefficient error as a function of the regularization")
plt.axis("tight")


# Print lowest error and lowest error index (i.e. which value of lambda in the array)
print("Minimum Mean Squared Error Term: " + str(min(errors)))
print("Corresponding lambda value: " + str(lambdas[errors.index(min(errors))]))

plt.show()