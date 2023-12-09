import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return x**4/(2.51*10**13) # equação de probabilidade (Rayleigh)

def g(y):
   return y**8/(5**26*8.45*10**8) # equação de probabilidade (Nakagami-m)

x = np.linspace(0, 2240)
y = np.linspace(0, 2441) # valores até atingir 1 de probabilidade

plt.plot(x, f(x), color='blue', label='Rayleigh')
plt.plot(y, g(y), color='red', label='Nakagami-m')
plt.legend()
plt.xlabel('d (m)')
plt.ylabel('Pout')
plt.ylim(0, 1)

plt.show()
