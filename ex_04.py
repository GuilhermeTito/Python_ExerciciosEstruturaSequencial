# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
notas = [0,0,0,0]
soma = 0
i = 0
while i < 4:
    j = i + 1
    notas[i] = float(input("Digite a %dª nota bimestral: "%(j)))
    if notas[i] > 10:
        print("A nota não pode ser maior que 10.")
    else:
        soma = soma + notas[i]
        i = i + 1
media = soma / 4
print("A média foi %.2f"%(media))