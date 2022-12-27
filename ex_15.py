# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o 
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
sHora = float(input("Digite o quanto você ganha por hora em reais: "))
horasTrabMes = float(input("Digite o número de horas que você trabalha por mês: "))
sMesBruto = sHora * horasTrabMes
ir = sMesBruto * 11 / 100
inss = sMesBruto * 8 / 100
sindicato = sMesBruto * 5 / 100
sMesLiq = sMesBruto - (ir + inss + sindicato)
print("+ Salário Bruto: R$%.2f"%(sMesBruto))
print("- IR: R$%.2f"%(ir))
print("- INSS: R$%.2f"%(inss))
print("= Salário Líquido: R$%.2f"%(sMesLiq))