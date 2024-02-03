import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

def f(x):
    return 3 * x ** 2 - 3

a = 0
b = 2

num_points = 100000

def monte_carlo_integrate(func, a, b, num_points):
    x_vals = np.random.uniform(a, b, num_points)
    y_vals = np.random.uniform(0, max(func(x_vals)), num_points)
    under_curve = np.sum(y_vals < func(x_vals))
    area_mc = (b - a) * max(func(x_vals)) * (under_curve / num_points)
    return area_mc


result, error = spi.quad(f, a, b)

area_mc = monte_carlo_integrate(f, a, b, num_points)


print(f"Quad: {result}")
print(f"Метод Монте-Карло: {area_mc}")



x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(x, y, color='gray', alpha=0.3)
ax.set_xlim([a, b])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегралу f(x) = 3x^2 - 3 від {a} до {b}')
plt.grid()
plt.show()
