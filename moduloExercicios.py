import math

def ex01():
    print("Exercício 1.\n")
    print("Alo, Mundo!")
    input("Pressione enter para continuar...")

def ex02():
    print("Exercício 2.\n")
    x = input("Digite um número: ")
    print(x)
    input("Pressione enter para continuar...")

def ex03():
    print("Exercício 3.\n")
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    soma = x + y
    print("A soma dos dois é: %s"%(soma))
    input("Pressione enter para continuar...")

def ex04():
    print("Exercício 4.\n")
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
    input("Pressione enter para continuar...")

def ex05():
    print("Exercício 5.\n")
    metros = float(input("Digite uma distância em metros: "))
    centimetros = metros * 100
    print("%.2f metros é igual a %.2f centímetros."%(metros, centimetros))
    input("Pressione enter para continuar...")

def ex06():
    print("Exercício 6.\n")
    raio = float(input("Digite o raio do círculo em centímetros: "))
    area = math.pi * (raio * raio)
    print("A área do círculo é de %.2f centímetros quadrados."%(area))
    input("Pressione enter para continuar...")

def ex07():
    print("Exercício 7.\n")
    lado = float(input("Digite o comprimento do lado do quadrado em centímetros: "))
    dobroArea = 2 * (lado * lado)
    print("O dobro da área do quadrado é %.2f centímetros quadrados."%(dobroArea))
    input("Pressione enter para continuar...")

def ex08():
    print("Exercício 8.\n")
    sHora = float(input("Digite o quanto você ganha por hora em reais: "))
    horasMes = float(input("Digite o número de horas que você trabalha por mês: "))
    sMes = sHora * horasMes
    print("Você ganha %.2f reais por mês."%(sMes))
    input("Pressione enter para continuar...")

def ex09():
    print("Exercício 9.\n")
    tempF = float(input("Digite a temperatura em graus Fahrenheit: "))
    tempC = 5 * ((tempF - 32) / 9)
    print("A temperatura em graus Celsius é %.2f."%(tempC))
    input("Pressione enter para continuar...")

def ex10():
    print("Exercício 10.\n")
    tempC = float(input("Digite a temperatura em graus Celsius: "))
    tempF = (tempC * 9 / 5) + 32
    print("A temperatura em graus Fahrenheit é %.2f."%(tempF))
    input("Pressione enter para continuar...")

def ex11():
    print("Exercício 11.\n")
    int1 = int(input("Digite um número inteiro: "))
    int2 = int(input("Digite outro número inteiro: "))
    real = float(input("Digite um número real: "))
    a = (2 * int1) * (int2 / 2)
    b = (3 * int1) + real
    c = pow(real, 3)
    print("Resultado da operação A: %.2f"%(a))
    print("Resultado da operação B: %.2f"%(b))
    print("Resultado da operação C: %.2f"%(c))
    input("Pressione enter para continuar...")

def ex12():
    print("Exercício 12.\n")
    altura = float(input("Digite sua altura em metros: "))
    pesoIdeal = (72.7 * altura) - 58
    print("Seu peso ideal é %.2f quilos."%(pesoIdeal))
    input("Pressione enter para continuar...")

def ex13():
    print("Exercício 13.\n")
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
    input("Pressione enter para continuar...")

def ex14():
    print("Exercício 14.\n")
    peso = float(input("Digite o peso dos peixes em quilos: "))
    if peso <= 50:
        print("Não há excesso, portanto não haverá multa.")
    else:
        excesso = peso - 50
        multa = excesso * 4
        print("Há um excesso de %.2f quilos, portanto a multa será de %.2f reais."%(excesso, multa))
    input("Pressione enter para continuar...")

def ex15():
    print("Exercício 15.\n")
    salHora = float(input("Digite o quanto você ganha por hora em reais: "))
    horasTrabMes = float(input("Digite o número de horas que você trabalha por mês: "))
    salMesBruto = salHora * horasTrabMes
    ir = salMesBruto * 11 / 100
    inss = salMesBruto * 8 / 100
    sindicato = salMesBruto * 5 / 100
    salMesLiq = salMesBruto - (ir + inss + sindicato)
    print("+ Salário Bruto: R$%.2f"%salMesBruto)
    print("- IR: R$%.2f"%(ir))
    print("- INSS: R$%.2f"%(inss))
    print("= Salário Líquido: R$%.2f"%salMesLiq)
    input("Pressione enter para continuar...")

def ex16():
    print("Exercício 16.\n")
    area = float(input("Digite a área em metros quadrados a ser pintada: "))
    litros = area / 3
    if litros % 18 != 0:
        latas = int(litros / 18) + 1
    else:
        latas = litros / 18
    preco = latas * 80
    print("Você vai precisar de %d latas de tinta, que vão custar R$%d.00 no total."%(latas, preco))
    input("Pressione enter para continuar...")

def ex17():
    print("Exercício 17.\n")
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
    input("Pressione enter para continuar...")

def ex18():
    print("Exercício 18.\n")
    tamanho = float(input("Digite o tamanho do arquivo em MB: "))
    velocidade = float(input("Digite a volocidade da internet em MBps: "))
    tempo = tamanho / velocidade
    print("O download demorará %.2f segundos para ser concluído."%(tempo))
    input("Pressione enter para continuar...")

if __name__ == "__main__":
    print("Execute estruturaSequencial.py")
    input("Pressione enter para continuar...")