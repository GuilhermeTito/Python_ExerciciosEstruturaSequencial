# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
tempC = float(input("Digite a temperatura em graus Celsius: "))
tempF = (tempC * 9 / 5) + 32
print("A temperatura em graus Fahrenheit é %.2f."%(tempF))