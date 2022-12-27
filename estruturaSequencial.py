import sys
import moduloExercicios
while 1:
    print("\nExercícios de Estrutura Sequencial\n")
    print("Digite um número de 1 a 18 para ir para o respectivo exercício. Digite 0 para sair.")
    op = int(input())
    if op == 0:
        sys.exit()
    elif op == 1:
        moduloExercicios.ex01()
    elif op == 2:
        moduloExercicios.ex02()
    elif op == 3:
        moduloExercicios.ex03()
    elif op == 4:
        moduloExercicios.ex04()
    elif op == 5:
        moduloExercicios.ex05()
    elif op == 6:
        moduloExercicios.ex06()
    elif op == 7:
        moduloExercicios.ex07()
    elif op == 8:
        moduloExercicios.ex08()
    elif op == 9:
        moduloExercicios.ex09()
    elif op == 10:
        moduloExercicios.ex10()
    elif op == 11:
        moduloExercicios.ex11()
    elif op == 12:
        moduloExercicios.ex12()
    elif op == 13:
        moduloExercicios.ex13()
    elif op == 14:
        moduloExercicios.ex14()
    elif op == 15:
        moduloExercicios.ex15()
    elif op == 16:
        moduloExercicios.ex16()
    elif op == 17:
        moduloExercicios.ex17()
    elif op == 18:
        moduloExercicios.ex18()
    else:
        print("Digite um valor válido.")
        input("Pressione enter para continuar...")