#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


def trapezoidal(a, b, f, x1, y1, file, n):
    # get base points
    x = np.linspace(a, b, 4)
    y = [f(el) for el in x]

    x = np.array(x)

    base = b - a
    height = (y[np.where(x == a)[0][0]] + y[np.where(x == b)[0][0]]) / 2
    area = base * height

    # plot the left wall
    plt.plot([a, a], [0, y[np.where(x == a)[0][0]]], 'b')

    # plot the right wall
    plt.plot([b, b], [0, y[np.where(x == b)[0][0]]], 'b')

    # plot the roof of the trapezoid
    plt.plot([a, b], [y[np.where(x == a)[0][0]], y[np.where(x == b)[0][0]]], 'b')

    file.write('{0} {1} {2}\n'.format(n, height, area))
    return area


if __name__ == '__main__':
    # read the function
    str_fun = 'lambda x: ' + input('Ingresa la función f(x) = ')
    fun = eval(str_fun)

    lower = int(input('Ingresa el valor inferior: '))
    upper = int(input('Ingresa el valor superior: '))
    n = int(input('Ingresa el número de trapezoides: '))

    # 100 linearly spaced numbers
    lin = np.linspace(lower, upper, 100)
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

    # show the plot
    print("--- Mostrando gráfica ---")

    # plot the function
    plt.plot(lin, y, 'g')

    xs = np.linspace(lower, upper, n + 1)
    area = 0

    file = open('output_trapezoidal.txt', 'w')
    k = 0
    for i in range(0, n):
        k = k + 1
        area = area + trapezoidal(xs[i], xs[i+1], fun, lin, y, file, k)
    file.close()
    print(area)
    plt.show(block=True)
