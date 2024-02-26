import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 1.0, 500)
y = numpy.random.normal(5.0, 4.0, 500)

plt.scatter(x, y, c=y, cmap='gnuplot_r')  # Color points based on y values with a red colormap
plt.show()
