import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rayleigh, rice, nakagami

# Parâmetros das distribuições
scale_rayleigh = 1.0 # Parâmetro de escala da distribuição Rayleigh
scale_rice = 1.0 # Parâmetro de escala da distribuição Rice
shape_nakagami = 2.0 # Parâmetro de forma da distribuição Nakagami

# Valores de x para o gráfico
x = np.linspace(0, 5, 1000)

# Calcula as PDFs para cada distribuição
pdf_rayleigh = rayleigh.pdf (x, scale-scale_rayleigh)
pdf_rice = rice.pdf (x, b=scale_rice)
pdf_nakagami = nakagami.pdf (x, shape_nakagami)

# Cria o gráfico
plt.figure (figsize=(10, 6))
plt.plot(x, pdf_rayleigh, label='Rayleigh')
plt.plot(x, pdf_rice, label='Rice')
plt.plot(x, pdf_nakagami, label='Nakagami')
plt.xlabel('x')
plt.ylabel('PDF (x)')
plt.title('Curvas PDF das Distribuições Rayleigh, Rice e Nakagami')
plt.legend()
plt.grid (True)

#Exibe o gráfico
plt.show()
