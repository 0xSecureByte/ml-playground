import matplotlib.pyplot as plt
from scipy import stats

x = [6,7,8,7,2,23,2,9,4,9,12,9,6]
y = [93,6,8,88,11,86,10,87,94,78,77,85,86]
slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r) # 0.3729186928452404

# BAD FIT FOR LINEAR REGRESSION