# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A) o produto do dobro do primeiro com metade do segundo .
# B) a soma do triplo do primeiro com o terceiro.
# C) o terceiro elevado ao cubo.
import math
int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
real = float(input("Digite um número real: "))
A = (2 * int1) * (int2 / 2)
B = (3 * int1) + real
C = pow(real, 3)
print("Resultado da operação A: %.2f"%(A))
print("Resultado da operação B: %.2f"%(B))
print("Resultado da operação C: %.2f"%(C))