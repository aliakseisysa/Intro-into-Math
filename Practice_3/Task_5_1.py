#Нарисуйте трехмерный график двух параллельных плоскостей

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-500, 500, 1)
Y = np.arange(-500, 500, 1)
X, Y = np.meshgrid(X, Y)
Z2 = 1 - 2*X - 3*Y
Z1 = -8 - 10*X - 15*Y
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
show()