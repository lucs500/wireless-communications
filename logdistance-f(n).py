import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return 215.9*x**2-2885.76*x+9867.47 #equação F(n)

x = np.linspace(4.5, 9)

plt.plot(x, f(x), color='red')
plt.legend()
plt.xlabel('n')
plt.ylabel('F(n)')
plt.yscale('log')

plt.show()
