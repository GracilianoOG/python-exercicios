num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
maior = num1

if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

print("O maior número é:", maior)
