# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = float(input("Digite o tamanho do arquivo em MB: "))
velocidade = float(input("Digite a volocidade da internet em MBps: "))
tempo = tamanho / velocidade
print("O download demorará %.2f segundos para ser concluído."%(tempo))