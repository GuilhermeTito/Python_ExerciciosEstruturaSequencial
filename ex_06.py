# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
raio = float(input("Digite o raio do círculo em centímetros: "))
area = math.pi * (raio * raio)
print("A área do círculo é de %.2f centímetros quadrados."%(area))