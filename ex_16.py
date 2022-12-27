# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = float(input("Digite a área em metros quadrados a ser pintada: "))
litros = area / 3
if litros % 18 != 0:
    latas = int(litros / 18) + 1
else:
    latas = litros / 18
preco = latas * 80
print("Você vai precisar de %d latas de tinta, que vão custar R$%d.00 no total."%(latas, preco))