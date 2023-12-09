import numpy as np
import matplotlib.pyplot as plt

def f(x):
return -35.547-32.3*np.log(x) #equação F(n)

x = np.linspace(0, 1000)

plt.plot(x, f(x), color='red')
plt.legend()
plt.xlabel('d (m)')
plt.ylabel('Pr (dBm)')

plt.show()
