import numpy as np
import matplotlib.pyplot as plt

def f(x):
   return -35.930-66.8*np.log10(x) #equação F(n)

x = np.linspace(1, 10)

y = [1, 2, 3, 4, 5, 10]
z = [-35.93, -69.99, -70.43, -73.39, -86.2, -95.82] #pontos medidos

plt.scatter(y, z, label='Pontos medidos')

plt.plot(x, f(x), color='red', label='Função encontrada')
plt.legend()
plt.xlabel('d (m)')
plt.ylabel('Pr (dBm)')

plt.show()
