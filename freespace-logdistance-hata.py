import numpy as np
import matplotlib.pyplot as plt

plt.rcParams ["figure.autolayout"] = True

def a(x):
  return 1000 * 0.1666**2 / ((4*np.pi)**2 * x**2) #modelo ar livre

def b(x):
  return 1000 * 0.1666**2 / ((4*np.pi) **2 * 1000**2) * (x / 1000) **-3 #modelo log-distância (Pr(d0) espaço-livre) com n=3

def c(x):
  return 1000 * 0.1666**2 / ((4*np.pi)**2 * 1000**2) * (x / 1000)**-4 #modelo log-distância (Pr(do) espaço-livre) com n=4

x = np.linspace (1000, 20000)

plt.plot(x, a(x), color='red', label='Ar livre')
plt.plot(x, b(x), color='blue', label='n=3')
plt.plot(x, c(x), color='green', label='n=4')
plt.legend()
plt.xlabel('d (m)')
plt.xscale('log')
plt.ylabel('Pr (W)')
plt.yscale ('log')

plt.show()
