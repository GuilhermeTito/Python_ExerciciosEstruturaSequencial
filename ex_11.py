# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo .
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.
import math
int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
real = float(input("Digite um número real: "))
a = (2 * int1) * (int2 / 2)
b = (3 * int1) + real
c = pow(real, 3)
print("Resultado da operação A: %.2f"%(a))
print("Resultado da operação B: %.2f"%(b))
print("Resultado da operação C: %.2f"%(c))