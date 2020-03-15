#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


def get_root(f, d, x0, error):
    root = x0
    n = 0
    h = f(root) / d(root)
    file = open('output_nr.txt', 'w')
    while abs(h) >= error:
        n = n + 1
        h = f(root) / d(root)
        root = root - h

        file.write('{0} {1} {2}\n'.format(n, root, h))
    file.close()
    return root


if __name__ == '__main__':
    # read the function
    str_fun = 'lambda x: ' + input('Ingresa la función f(x) = ')
    str_der = 'lambda x: ' + input('Ingresa la derivada de la función f\'(x) = ')
    f = eval(str_fun)
    d = eval(str_der)

    # 100 linearly spaced numbers
    lin = np.linspace(-5, 5, 100)
    y = [f(x) for x in lin]

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

    # show the plot
    print("--- Mostrando gráfica ---")

    x0 = int(input('Ingresa el valor inicial: '))

    root = get_root(f, d, x0, 0.0001)

    plt.plot(root, 0, 'r*')
    plt.show(block=True)
