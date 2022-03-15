# Author: Kornel Kielczewski -- <kornel.k@plusnet.pl>
# code modified by Section 1 APPM Group


import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import make_regression
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

clf = Ridge()


X, y, w = make_regression(
    n_samples=10, n_features=1, coef=True, random_state=1, bias=3.5, noise=30
)

X1, y1, w1 = make_regression(
    n_samples=10, n_features=1, coef=True, random_state=1, bias=3.5, noise=30
)

plt.figure(figsize=(20, 6))

plt.subplot(121)
ax = plt.gca()
ax.scatter(X, y)
plt.scatter(X,y)
plt.xlabel("Sample X Data")
plt.ylabel("Sample Y Data")
plt.title("Sample Linear Data Without Noise")

plt.subplot(122)
ax = plt.gca()
ax.scatter(X1, y1)
plt.scatter(X1,y1)
plt.xlabel("Sample X Data")
plt.ylabel("Sample Y Data")
plt.title("Sample Linear Data With Noise=10")
plt.show() 



coefs = []
errors = []

# alpha is equivalent to lambda in our paper
alphas = np.logspace(-6, 6, 200)

# Train the model with different regularisation strengths
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, [w]))

# Display results
plt.figure(figsize=(20, 6))

plt.subplot(121)
ax = plt.gca()
ax.plot(alphas, coefs)

print(coefs[0])


ax.set_xscale("log")
plt.xlabel("lambda")
plt.ylabel("weights")
plt.title("Ridge coefficients as a function of the regularization")
plt.axis("tight")


plt.subplot(122)
ax = plt.gca()
ax.plot(alphas, errors)
ax.set_xscale("log")
plt.xlabel("lambda")
plt.ylabel("error")
plt.title("Coefficient error as a function of the regularization")
plt.axis("tight")



plt.show()