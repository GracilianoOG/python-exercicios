num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))
maior = num1
menor = num1

# Verifica o maior número
if num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

# Verifica o menor número
if num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3

if maior != menor:
    print("O maior número é:", maior)
    print("O menor número é:", menor)
else:
    print("Ambos são iguais!")
