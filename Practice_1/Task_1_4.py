#Постройте на одном графике две кривые y(x)
# для функции двух переменных y(k,x)=cos(k∙x),
# взяв для одной кривой значение k=1, а для другой – любое другое k, не равное 1

import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-20,20,0.1)
k1=1
k2=0.5
plt.plot(x, np.cos(k1*x))
plt.plot(x, np.cos(k2*x))
plt.show()