import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
M = 2 # Número de símbolos na constelação (BPSK)
Eb_N0_dB = np.arange(-10, 21, 2) # Faixa de relação sinal-ruído em dB
N = 100000 # Número de bits para transmitir
n_amostras = 10 # Número de amostras do canal Rayleigh
antenas = 2 # Número de antenas para diversidade

# Gere os bits aleatórios para a transmissão
bits = np.random.randint(0, M, N)

# Mapeie os bits para símbolos BPSK
simbolos = 2 * bits - 1

# Inicialize arrays para armazenar as taxas de erro de bit
taxa_erro_bit = np.zeros(len(Eb_N0_dB))

for i in range(len(Eb_N0_dB)):
# Simule o canal Rayleigh com diversidade na recepção
canal_rayleigh = (np.random.randn(antenas, N) + 1j * np.random.randn(antenas, N)) / np.sqrt(2)

# Transmita os símbolos pelo canal Rayleigh
sinal_recebido = np.zeros((antenas, N), dtype=complex)
for j in range(antenas):
sinal_recebido[j, :] = np.convolve(simbolos, canal_rayleigh[j, :])[:N]

# Calcule a potência média do sinal recebido
potencia_media = np.mean(np.abs(sinal_recebido[j])**2)

# Calcule a relação sinal-ruído (Eb/N0)
Eb_N0_lin = 10 ** (Eb_N0_dB[i] / 10)

# Calcule a potência do ruído para corresponder a Eb/N0 desejado
variancia_ruido = potencia_media / (2 * antenas * Eb_N0_lin)

# Gere o ruído AWGN complexo
ruido_real = np.random.randn(N)
ruido_imaginario = np.random.randn(N)
ruido_complexo = (ruido_real + 1j * ruido_imaginario) * np.sqrt(variancia_ruido)

# Adicione o ruído aos sinais recebidos
sinal_recebido += ruido_complexo

# Na recepção, faça a detecção e decodificação dos símbolos
sinal_decodificado = np.sum(sinal_recebido, axis=0)
bits_decodificados = np.where(sinal_decodificado >= 0, 1, 0)

# Calcule a taxa de erro de bit (BER)
erro_bit = np.sum(bits != bits_decodificados)
taxa_erro_bit[i] = erro_bit / N

# Plote a BER em função da relação sinal-ruído (Eb/N0)
plt.semilogy(Eb_N0_dB, taxa_erro_bit, marker='o', linestyle='-')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.grid(True)
plt.title('Desempenho do BPSK em Canal Rayleigh com Diversidade')
plt.show()
