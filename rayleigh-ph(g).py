import numpy as np
import matplotlib.pyplot as plt

Ph = 1.0 # variância da amplitude

h = np.linspace(0, 5, 1000) # intervalo dos valores para h^2

pdf_h = 1 / (Ph) * np.exp(-h / (Ph)) # cálculo da pdf com equação deduzido

plt.plot(h, pdf_h)
plt.xlabel('h^2')
plt.ylabel('pdf')
plt.title('pdf da potência instantânea recebida (Rayleigh)')
plt.legend()
plt.grid(True)
plt.show() # plot do gráfico
