##MS&E 211X
##Yunru Huang
##yrhuang
##HW5 Question 5

"""
Part (a)

When alpha = 0.1
The optimal point is [0.0, 3.3591924730804372, 3.3591924730804372]
Optimal objective value is 0.362374378107
Achieved at the 1130th iteration.

When alpha = 1
The optimal point is [0.0, 3.3591970972001617, 3.3591970972001617]
Optimal objective value is 0.362374378044
Achieved at the 109th iteration.
"""

# (b)

"""
The first attached graph at the end of the pdf file corresponds to alpha = 0.1
The second attached graph is for alpha = 1.
"""

# (c)

import math
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

EPS = 1e-5
ALPHA = 0.1
ALPHA2 = 1


def f(x):
    x0, x1, x2 = x
    t1 = math.exp(-x1 - x0)
    t2 = math.exp(-x2 - x0)
    t3 = math.exp(-x1 + x0)
    t4 = math.exp(-x2 + x0)
    return math.log(1 + t1) + math.log(1 + t3) + math.log(1 + t3) + math.log(1 + t4) + 0.01 * (x1 * x1 + x2 * x2)


def grad(x):
    x0, x1, x2 = x
    t1 = math.exp(-x1 - x0)
    t2 = math.exp(-x2 - x0)
    t3 = math.exp(-x1 + x0)
    t4 = math.exp(-x2 + x0)
    dx0 = -t1 / (1 + t1) - t2 / (1 + t2) + t3 / (1 + t3) + t4 / (1 + t4)
    dx1 = -t1 / (1 + t1) - t3 / (1 + t3) + 0.02 * x1
    dx2 = -t2 / (1 + t2) - t4 / (1 + t4) + 0.02 * x2
    return dx0, dx1, dx2


def norm(x):
    x0, x1, x2 = x
    return math.sqrt(x0 * x0 + x1 * x1 + x2 * x2)


def optimize(alpha):
    x = [0, 0, 0]
    i = 0
    f_values = []
    # g_values = []
    while True:
        i += 1
        f_values.append(f(x))
        g = grad(x)
        # g_values.append(norm(g))
        if norm(g) <= EPS:
            break
        else:
            x[0] -= alpha * g[0]
            x[1] -= alpha * g[1]
            x[2] -= alpha * g[2]

    plt.plot(range(1, i + 1), f_values)
    plt.ylabel('objective function values')
    plt.xlabel('iteration number')
    plt.title('alpha = 0.1')
    plt.show()

    print(i)
    print(x)
    print(f_values[i - 1])


def main():
    optimize(0.1)
    optimize(1)


main()


