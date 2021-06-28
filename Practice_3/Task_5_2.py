#Нарисуйте трехмерный график двух любых поверхностей второго порядка.

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-50, 50, 1)
Y = np.arange(-50, 50, 1)
X, Y = np.meshgrid(X, Y)
Z1 = (X**2/2**2) - (Y**2/3**2)
Z2 = (X**2/2**2) + (Y**2/3**2)
ax.plot_surface(X, Y, Z1)
ax.plot_surface(X, Y, Z2)
show()