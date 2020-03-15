#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt


def bisection(lower, upper, func):
    if func(lower) * func(upper) >= 0:
        raise ValueError

    orig_lower = lower
    orig_upper = upper
    root = lower
    apre = 100
    prev = 0
    n = 0
    error = 0.01

    file = open('output_bisection.txt', 'w')
    while apre > error:
        # Find middle point
        n = n + 1
        root = (lower + upper) / 2

        apre = abs((root - prev) / root) * 100

        # Check if middle point is root
        if func(root) == 0.0:
            break

        # Decide the side to repeat the steps
        if func(root) * func(upper) < 0:
            lower = root
        else:
            upper = root

        prev = root

        file.write('{0} {1} {2} {3} {4}\n'.format(n, orig_lower, orig_upper, root, apre))
    file.close()
    return root


if __name__ == '__main__':
    # read the function
    str_fun = 'lambda x: ' + input('Ingresa la función f(x) = ')
    fun = eval(str_fun)

    # 100 linearly spaced numbers
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

    # show the plot
    print("--- Mostrando gráfica ---")

    lower = int(input('Ingresa el límite inferior: '))
    upper = int(input('Ingresa el límite superior: '))
    plt.plot(lower, 0, 'bo')
    plt.plot(upper, 0, 'bo')

    try:
        root = bisection(lower, upper, fun)
        plt.plot(root, 0, 'r*')
        plt.show(block=True)
    except ValueError:
        print("Por favor, intenta con otros límites.")
