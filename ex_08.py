# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
sHora = float(input("Digite o quanto você ganha por hora em reais: "))
horasMes = float(input("Digite o número de horas que você trabalha por mês: "))
sMes = sHora * horasMes
print("Você ganha %.2f reais por mês."%(sMes))