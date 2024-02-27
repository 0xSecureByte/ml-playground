import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = [2, 4, 5, 4, 3, 12, 2, 7, 8, 15, 10, 12, 11]

x_transformed = np.log(x)
y_transformed = np.log(y)

slope, intercept, r, p, std_err = stats.linregress(x_transformed, y_transformed)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x_transformed))

plt.scatter(x_transformed, y_transformed, label='Original Data')
plt.plot(x_transformed, mymodel, color='red', label='Linear Regression')
plt.xlabel('log(x)')
plt.ylabel('log(y)')
plt.legend()
plt.show()

print("R-value:", r) # 0.7127489233437811

# BEST FIT FOR LINEAR REGRESSION