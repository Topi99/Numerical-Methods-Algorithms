#!/usr/bin/env python
import cmath
from matplotlib import pyplot as plt
import numpy as np


def ctr(z):
    return round(z.real, 7) + round(z.imag, 7) * 1j


def bairstow(a, r, s, g, roots, it, file):
    if g < 1:
        file.write('{0} {1} {2}'.format(it, r, s))
        return None
    if g == 1:
        roots.append(float(-a[0]) / float(a[1]))
        file.write('{0} {1} {2}'.format(it, r, s))
        return None
    if g == 2:
        D = (a[1] ** 2.0) - 4.0 * a[2] * a[0]
        X1 = (-a[1] - cmath.sqrt(D)) / (2.0 * a[2])
        X2 = (-a[1] + cmath.sqrt(D)) / (2.0 * a[2])
        roots.append(X1)
        roots.append(X2)
        file.write('{0} {1} {2}'.format(it, r, s))
        return None

    n = len(a)
    b = [0] * len(a)
    c = [0] * len(a)
    b[n - 1] = a[n - 1]
    b[n - 2] = a[n - 2] + r * b[n - 1]
    i = n - 3

    while i >= 0:
        b[i] = a[i] + r * b[i + 1] + s * b[i + 2]
        i = i - 1

    c[n - 1] = b[n - 1]
    c[n - 2] = b[n - 2] + r * c[n - 1]
    i = n - 3

    while i >= 0:
        c[i] = b[i] + r * c[i + 1] + s * c[i + 2]
        i = i - 1
    din = ((c[2] * c[2]) - (c[3] * c[1])) ** (-1.0)
    r = r + din * ((c[2]) * (-b[1]) + (-c[3]) * (-b[0]))
    s = s + din * ((-c[1]) * (-b[1]) + (c[2]) * (-b[0]))

    if abs(b[0]) > 1E-8 or abs(b[1]) > 1E-8:
        return bairstow(a, r, s, g, roots, i+1, file)
    if g >= 3:
        Dis = ((-r) ** 2.0) - (4.0 * 1.0 * (-s))
        X1 = (r - (cmath.sqrt(Dis))) / 2.0
        X2 = (r + (cmath.sqrt(Dis))) / 2.0
        roots.append(X1)
        roots.append(X2)
        return bairstow(b[2:], r, s, g - 2, roots, i+1, file)

roots = []
a = []
g = int(input("degree ? : "))

str_fun = 'lambda x:'
for k in range(0, g + 1):
    A = float(input("Coef. X^" + str(g - k) + " ? : "))
    str_fun = str_fun + ' + ' + str(A) + ' * x**' + str(g - k)
    a.append(A)

fun = eval(str_fun)
a.reverse()

lin = np.linspace(-5, 5, 100)
y = [fun(x) for x in lin]
# set interactive mode on
plt.ion()

# setting the axes at the centre
fig = plt.figure()

# set the limits so they don't change while plotting
plt.xlim(min(lin), max(lin))
plt.ylim(min(y), max(y))

ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(lin, y, 'g')

k = 1
r = int(input("Ingrese r0: "))
s = int(input("Ingrese s0: "))

file = open('output_bairstow.txt', 'w')

bairstow(a, r, s, g, roots, 0, file)

file.close()

print("\nRaices encontradas => \n")
for r in roots:
    print("R" + str(k) + " = " + str(ctr(r)))
    k = k + 1
    plt.plot(r.real, 0, 'r*')
# show the plot
print("--- Mostrando gráfica ---")
plt.show(block=True)
