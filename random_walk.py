#!/usr/bin/env python
import numpy
from matplotlib import pylab
import random

# reading the number of steps
n = int(input("Ingresa el número de pasos: "))
l = int(input("Ingresa la longitud de los pasos(mayor a 2 para obtener un mejor resultado): "))

# creating two array for containing x and y coordinate
# of size equals to the number of size and filled up with 0's
x = numpy.zeros(n)
y = numpy.zeros(n)

# filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(0, l)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

# plotting stuff:
pylab.title("Random Walk ($n = " + str(n) + "$ pasos)")
pylab.plot(x, y)
pylab.show()
