import numpy as np
import matplotlib.pyplot as plt

def f(x):
return 1591.47*x**2-10305.1*x+17116.93 #equação F(n)

x = np.linspace(1.5, 5)

plt.plot(x, f(x), color='red')
plt.legend()
plt.xlabel('n')
plt.ylabel('F(n)')
plt.yscale('log')

plt.show()
