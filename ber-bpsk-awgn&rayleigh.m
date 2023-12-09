close all;
clear all;

rand('state',0); %Reinicializa sementes de geradores de números aleatórios
randn('state',0);

bits=1e6; %Número de bits transmitidos

M=2; %BPSK, dois símbolos possíveis na modulação.

b=rand(1,bits)>0.5; %Gera 0s e 1s
x=2*b-1; %Gera símbolos com energia unitária (note que os símbolos pertencem aos Reais)
N0=1; %Neste exemplo N0 é fixada em 1
n=randn(1,bits)*sqrt(N0/2); %Ruído base com variancia N0/2. Geramos só a parte real, 
%pois BPSK tem símbolos reais (no modulador QAM usamos só o ramo que modula o coseno da portadora), 
%se fosse uma modulação com símbolos complexos, teríamos que gerar também uma parte imaginária do ruído, com variância N0/2

EbN0dB=0:1:10; %Intervalo da SNR que será considerado
ber_simulada=zeros(1,length(EbN0dB));
ber_teorica=zeros(1,length(EbN0dB));

for i=1:length(EbN0dB)

    EbN0=10^(EbN0dB(i)/10); %Valor de Eb/N0 em linear para o loop
    Eb=EbN0*N0; %Cálculo de Eb
    Es=Eb*log2(M); %Cálculo de Es, a Energia de Símbolo

    y_awgn=sqrt(Es)*x+n; %Saída amostrada do filtro casado no receptor, onde o sinal sqrt(Es)*x tem a energia média Es já que a energia inicial de x era 1, canal AWGN.
    
    h=1/sqrt(2)*randn(1, bits)+1j/sqrt(2)*randn(1, bits); %Variação instantânea de de amplitude Rayleigh
    y_rayleigh=h.*(sqrt(Es)*x)+n; %Canal Rayleigh
    
    b_est_awgn=y_awgn>0;
    b_est_rayleigh=real(y_rayleigh./h)>0; %Decisor no receptor, modulação BPSK. Se a saída do filtro casado for >1 decide por bit 1, caso contrário, decide por bit 0.
    
    erros_awgn=sum(b~=b_est_awgn);
    erros_rayleigh=sum(b~=b_est_rayleigh); %Contagem de erros de bit

    ber_simulada_awgn(i)=erros_awgn/bits;
    ber_simulada_rayleigh(i)=erros_rayleigh/bits; %Cálculo da BER simulada
    
    ber_teorica_awgn(i)=0.5*erfc(sqrt(EbN0));
    ber_teorica_rayleigh(i)=0.5*(1-sqrt(EbN0/(1+EbN0))); %Cálculo da BER teórica
end

%Gráfico
figure;
semilogy(EbN0dB, ber_simulada_awgn, 'b-o', EbN0dB, ber_simulada_rayleigh, 'r-s', EbN0dB, ber_teorica_awgn, 'b--', EbN0dB, ber_teorica_rayleigh, 'r--');
legend('AWGN Simulado', 'Rayleigh Simulado', 'Teórico AWGN', 'Teórico Rayleigh');
xlabel('Eb/N0 [dB]');
ylabel('BER');
grid on;
