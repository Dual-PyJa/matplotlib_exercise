import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y=x*2
#x = np.arange(0,5,0.1)
#y = np.square(x)

plt.plot(x,y,"k*")

plt.title("Y=X*2",loc="right")

#plt.plot(x,x,"b_-",x,x**2,"y4",x,x**3,"k*")

plt.show()