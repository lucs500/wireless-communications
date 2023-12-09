import numpy as np
import matplotlib.pyplot as plt

def alamouti_2x1_tx(s):
   s1, s2 = s / np.sqrt(2)  # Símbolos BPSK / Normalização 3dB
   return np.array([[s1, s2], [-s2, s1]])

def alamouti_2x1_rx(y, h):
   h1, h2 = h  # Coeficientes das 2 antenas
   norm = np.abs(h1)**2 + np.abs(h2)**2  # Normalização
   s1_til = (np.conj(h1) * y[0] + h2 * np.conj(y[1])) / norm
   s2_til = (np.conj(h2) * y[0] - h1 * np.conj(y[1])) / norm  # Equações deduzidas
   return [np.sign(s1_til.real), np.sign(s2_til.real)]

def mrc_1x2_rx(y, h):
   y_mrc = np.conj(h[0]) * y[0] + np.conj(h[1]) * y[1]
   return np.sign(y_mrc.real)

# Parâmetros
num_bits = 10**6
SNR_dB = np.arange(0, 25, 2)
BER_Ala = []
BER_MRC = []

for snr in SNR_dB:
   # Símbolos BSPK aleatórios
   bits = np.random.randint(0, 2, num_bits) * 2 - 1
   simbolos = bits.reshape(-1, 2)


   # Canal e ruído
   ruido_var = 1 / (10**(snr / 10))
   ruido_desv = np.sqrt(ruido_var / 2)  # Normalização 3dB

   # 2x1 Alamouti
   erro_alamouti = 0
   for s in simbolos:
       h = (np.random.randn(2) + 1j * np.random.randn(2)) / np.sqrt(2)  # Rayleigh
       x = alamouti_2x1_tx(s)
       n = ruido_desv * (np.random.randn(2) + 1j * np.random.randn(2))
       y = np.array([h.dot(x[0]) + n[0], h.dot(x[1]) + n[1]])
       s_til = alamouti_2x1_rx(y, h)

       erro_alamouti += np.sum(s != s_til)
   BER_Ala.append(erro_alamouti / num_bits)

   # 1x2 MRC
   erro_mrc = 0
   for s in bits:
       h = (np.random.randn(2) + 1j * np.random.randn(2)) / np.sqrt(2)
       n = ruido_desv * (np.random.randn(2) + 1j * np.random.randn(2))
       y = np.array([h[0] * s + n[0], h[1] * s + n[1]])
       s_til = mrc_1x2_rx(y, h)

       erro_mrc += (s != s_til)
   BER_MRC.append(erro_mrc / num_bits)


# Plotando
plt.semilogy(SNR_dB, BER_Ala, '-o', label='2x1 Alamouti')
plt.semilogy(SNR_dB, BER_MRC, '-s', label='1x2 MRC')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.legend()
plt.grid(True)
plt.show()
