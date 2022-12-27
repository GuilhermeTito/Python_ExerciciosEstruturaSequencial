# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o comprimento do lado do quadrado em centímetros: "))
dobroArea = 2 * (lado * lado)
print("O dobro da área do quadrado é %.2f centímetros quadrados."%(dobroArea))