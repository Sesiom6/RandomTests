print("Operações disponíveis:")
print("Soma (+)")
print("Subtração (-)")
print("Multiplicação (*)")
print("Divisão (/)\n")

num1 = float(input("Informe o primeiro número: "))
operador = input("Informe a operação a ser realizada (+, -, *, /): ")
num2 = float(input("Informe o segundo número: "))

if operador == "+":
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado)
elif operador == "-":
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)
elif operador == "*":
    resultado = num1 * num2
    print(num1, "*", num2, "=", resultado)
elif operador == "/":
    resultado = num1 / num2
    print(num1, "/", num2, "=", resultado)
else:
    print("Operação inválida")
