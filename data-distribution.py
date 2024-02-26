# /usr/local/bin python3
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.1, 4.0, 1000)

plt.hist(x, 30)
plt.show()