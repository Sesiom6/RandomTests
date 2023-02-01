import math

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potência")
print("6 - Raiz Quadrada")

escolha = int(input("Digite sua escolha (1/2/3/4/5/6): "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == 1:
    print("Resultado:", num1 + num2)
elif escolha == 2:
    print("Resultado:", num1 - num2)
elif escolha == 3:
    print("Resultado:", num1 * num2)
elif escolha == 4:
    print("Resultado:", num1 / num2)
elif escolha == 5:
    print("Resultado:", num1 ** num2)
elif escolha == 6:
    print("Resultado:", math.sqrt(num1))
else:
    print("Opção inválida, por favor escolha novamente")
