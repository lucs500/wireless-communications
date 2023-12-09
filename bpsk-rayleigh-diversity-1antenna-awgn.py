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
taxa_erro_bit_dif_antenas = np.zeros(len(Eb_N0_dB))
taxa_erro_bit_1_antena = np.zeros(len(Eb_N0_dB))
taxa_erro_bit_awgn = np.zeros(len(Eb_N0_dB))

for i in range(len(Eb_N0_dB)):
# Simule o canal Rayleigh com diversidade na recepção
canal_rayleigh = (np.random.randn(antenas, N) + 1j * np.random.randn(antenas, N)) / np.sqrt(2)

# Transmita os símbolos pelo canal Rayleigh com diversidade
sinal_recebido = np.zeros((antenas, N), dtype=complex)
for j in range(antenas):
sinal_recebido[j, :] = np.convolve(simbolos, canal_rayleigh[j, :])[:N]

# Transmita os símbolos pelo canal Rayleigh com 1 antena
canal_rayleigh_1_antena = (np.random.randn(1, N) + 1j * np.random.randn(1, N)) / np.sqrt(2)
sinal_recebido_1_antena = np.convolve(simbolos, canal_rayleigh_1_antena[0, :])[:N]

# Calcule a potência média do sinal recebido
potencia_media_dif_antenas = np.mean(np.abs(sinal_recebido[0])**2)
potencia_media_1_antena = np.mean(np.abs(sinal_recebido_1_antena)**2)

# Calcule a relação sinal-ruído (Eb/N0)
Eb_N0_lin = 10 ** (Eb_N0_dB[i] / 10)

# Calcule a potência do ruído para corresponder a Eb/N0 desejado
variancia_ruido_dif_antenas = potencia_media_dif_antenas / (2 * antenas * Eb_N0_lin)
variancia_ruido_1_antena = potencia_media_1_antena / (2 * Eb_N0_lin)

# Gere o ruído AWGN complexo
ruido_real = np.random.randn(N)
ruido_imaginario = np.random.randn(N)
ruido_complexo_dif_antenas = (ruido_real + 1j * ruido_imaginario) * np.sqrt(variancia_ruido_dif_antenas)
ruido_complexo_1_antena = (ruido_real + 1j * ruido_imaginario) * np.sqrt(variancia_ruido_1_antena)

# Adicione o ruído aos sinais recebidos com diversidade
sinal_recebido += ruido_complexo_dif_antenas

# Adicione o ruído ao sinal recebido com 1 antena
sinal_recebido_1_antena += ruido_complexo_1_antena

# Na recepção, faça a detecção e decodificação dos símbolos com diversidade
sinal_decodificado_dif_antenas = np.sum(sinal_recebido, axis=0)
bits_decodificados_dif_antenas = np.where(sinal_decodificado_dif_antenas >= 0, 1, 0)

# Na recepção, faça a detecção e decodificação dos símbolos com 1 antena
bits_decodificados_1_antena = np.where(sinal_recebido_1_antena >= 0, 1, 0)

# Calcule a taxa de erro de bit (BER) com diversidade
erro_bit_dif_antenas = np.sum(bits != bits_decodificados_dif_antenas)
taxa_erro_bit_dif_antenas[i] = erro_bit_dif_antenas / N

# Calcule a taxa de erro de bit (BER) com 1 antena
erro_bit_1_antena = np.sum(bits != bits_decodificados_1_antena)
taxa_erro_bit_1_antena[i] = erro_bit_1_antena / N

# Calcule a BER para o canal AWGN
variancia_ruido_awgn = potencia_media_dif_antenas / (2 * Eb_N0_lin)
ruido_awgn = (ruido_real + 1j * ruido_imaginario) * np.sqrt(variancia_ruido_awgn)
sinal_decodificado_awgn = simbolos + ruido_awgn
bits_decodificados_awgn = np.where(sinal_decodificado_awgn >= 0, 1, 0)
erro_bit_awgn = np.sum(bits != bits_decodificados_awgn)
taxa_erro_bit_awgn[i] = erro_bit_awgn / N

# Plote a BER em função da relação sinal-ruído (Eb/N0)
plt.semilogy(Eb_N0_dB, taxa_erro_bit_dif_antenas, marker='o', linestyle='-', label='Diversidade de Antenas')
plt.semilogy(Eb_N0_dB, taxa_erro_bit_1_antena, marker='s', linestyle='-', label='1 Antena')
plt.semilogy(Eb_N0_dB, taxa_erro_bit_awgn, marker='^', linestyle='-', label='AWGN')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('BER')
plt.grid(True)
plt.legend()
plt.title('Desempenho do BPSK em Canal Rayleigh com Diversidade vs. 1 Antena vs. AWGN')
plt.show()
