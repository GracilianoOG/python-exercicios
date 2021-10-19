def calculadora(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        return "Operadora inválido"


num1 = int(input("Informe o primeiro número: "))
op = input("Informe o operador: ")
num2 = int(input("Informe o segundo número: "))

print(calculadora(num1, num2, op))
