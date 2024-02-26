import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(4.0, 0.5, 1000)

plt.hist(x, 50)
plt.show()