# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite H se for homem ou M se for mulher: ")
if sexo == "H" or sexo == "h":
    pesIde = (72.7 * altura) - 58
    print("Seu peso ideal é %.2f quilos."%pesIde)
elif sexo == "M" or sexo == "m":
    pesIde = (62.1 * altura) - 44.7
    print("Seu peso ideal é %.2f quilos."%pesIde)
else:
    print("Inválido.")