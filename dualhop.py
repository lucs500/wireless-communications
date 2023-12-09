import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
r = 5 # Eficiência espectral (bps/Hz)
n = 2 # Número de retransmissões
d1_d2_ratio = 0.6 # Razão entre distância emissor-relê e distância emissor-transmissor
m = 4 # Parâmetro m da distribuição Nakagami-m

# Range de SNR em dB
snr_db_range = np.linspace(-10, 30, 41)

# Cálculo da outage probability para canal Nakagami-m
def outage_probability(snr_db, m, n, r, d1_d2_ratio):
snr_linear = 10**(snr_db / 10)
outage_prob = 1 - (1 + snr_linear * (d1_d2_ratio**(-n)) / (m * r))**(-n)
return outage_prob

# Gere o gráfico de outage probability
plt.figure(figsize=(10, 6))
plt.semilogy(snr_db_range, outage_probability(snr_db_range, m, n, r, d1_d2_ratio), label=f'Dual Hop (n={n})')
plt.xlabel('SNR (dB)')
plt.ylabel('Outage Probability')
plt.grid(True)
plt.legend()
plt.title('Outage Probability for Dual Hop System')
plt.show()
