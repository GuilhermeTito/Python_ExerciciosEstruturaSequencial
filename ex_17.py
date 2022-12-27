# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
# valores para cima, isto é, considere latas cheias.
import math
area = float(input("Digite a área em metros quadrados a ser pintada: "))
litros = (area / 6) * 1.1

latas = math.ceil(litros / 18)
precoLatas = latas * 80

galoes = math.ceil((litros * 10) / 36)
precoGaloes = galoes * 25

mixLatas = math.floor(litros / 18)
if litros % 18 != 0:
    mixGaloes = math.ceil(((litros - (mixLatas * 18)) * 10) / 36)
else:
    mixGaloes = 0
precoMix = (mixLatas * 80) + (mixGaloes * 25)

print("Comprando apenas latas, você vai precisar de %d latas de tinta, que vão custar R$%d.00 no total."%(latas, precoLatas))
print("Comprando apenas galões, você vai precisar de %d galões de tinta, que vão custar R$%d.00 no total."%(galoes, precoGaloes))
print("Comprando uma mistura de latas e galões, você vai precisar de %d latas e %d galões de tinta, que vão custar R$%d.00 no total."%(mixLatas, mixGaloes, precoMix))