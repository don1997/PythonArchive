import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from mpl_toolkits import mplot3d


"""
#assigns values to x and y var
x = [1,2,3]
y = [1,2,3]
z = [10,11,12]
#assigns vars to graph
plt.plot(x,y,z)
#print graph
plt.show()
"""
def f(x, y):
    return np.sin(np.sqrt(x ** 3 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface');

plt.show()