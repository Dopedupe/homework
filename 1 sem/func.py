import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
from math import sqrt
import warnings

warnings.filterwarnings('ignore')

x = np.arange(0, 5.0, 0.01)

x0 = 3                                                        # точка х0  <- менять здесь
f = pow((2 * x - 3), 2) * np.sin(pow(x, 2) + 2)


def func(x):
    return (2 * x - 3) ** 2 * np.sin(x ** 2 + 2)

def find_max(x, max):
    for i in x:
        if max == pow((2 * i - 3), 2) * np.sin(pow(i, 2) + 2):
            return i


def find_min(x, min):
    for i in x:
        if min == pow((2 * i - 3), 2) * np.sin(pow(i, 2) + 2):
            return i


def first_d(x):
    return (8 * x - 12) * np.sin(pow(x, 2) + 2) + pow((2 * x - 3), 2) * 2 * x * np.cos(pow(x, 2) + 2)

def second_d(x):
    return 2 * (20 * x ** 2 - 36 * x + 9) * np.cos(x ** 2 + 2) + 4 * (-4 * x ** 4 + 12 * x ** 3 - 9 * x ** 2 + 2) * np.sin(
    x ** 2 + 2)

def normal(x, x0):
    return func(x0) - (x - x0) / first_d(x0)

def kas(x, x0):
    return func(x0) + (x - x0) * first_d(x0)

def dlina_krivo(x):
    return sqrt(1+(first_d(x)**2))


result, blank = integrate.quad(dlina_krivo, 0, 5)
length = np.arange(x0-0.25, x0+0.25, 0.01)


ax1 = plt.subplot(221)
plt.plot(x, f, 'b')
plt.plot(find_max(x, max(f)), max(f), 'or')
plt.plot(find_min(x, min(f)), min(f), 'or')

plt.plot(length, normal(length, x0), '--r')
plt.plot(length, kas(length, x0), '--g')
plt.title("Function")
plt.grid()

ax2 = plt.subplot(222)
plt.plot(x, first_d(x), 'b')
plt.title("1DFunction")
plt.grid()

ax3 = plt.subplot(223)
plt.plot(x, second_d(x), 'b')
plt.title("2DFunction")
plt.grid()

ax4 = plt.subplot(224)
for t in x:
    temp = np.arange(t-0.25, t+0.25, 0.01)
    plt.plot(temp, kas(temp, t), '--g')
plt.xlabel(f'Длина кривой: {result:.5e}')
plt.grid()


plt.show()