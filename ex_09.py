# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
def fahCel():
    tempF = float(input("Digite a temperatura em graus Fahrenheit: "))
    tempC = 5 * ((tempF - 32) / 9)
    print("A temperatura em graus Celsius é %.2f."%(tempC))