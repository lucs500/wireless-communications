import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import nakagami

df = pd.read_csv(r'C:\Users\lucas\Downloads\5m.csv') # dados com valores em dBm, linear e média

data = np.sqrt(df['Linear']/df['Mean']) # cálculo de h

shape, loc, scale = nakagami.fit(data, floc=0)
best_m = shape # ajuste da distribuição Nakagami e encontrando melhor valor de m

plt.hist(data, bins=20, density=True, alpha=0.5, label='Data') #histograma
x = np.linspace(min(data), max(data), 100)
pdf = nakagami.pdf(x, best_m, loc=loc, scale=scale)
plt.plot(x, pdf, 'r-', label='Best fit (m={:.2f})'.format(best_m))
plt.xlabel('h')
plt.ylabel('pdf(h)')
plt.grid(True)
plt.legend()
plt.show() #plot do gráfico
