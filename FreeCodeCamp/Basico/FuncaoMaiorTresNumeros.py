def maior_de_tres(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    elif num3 > num1 and num3 > num2:
        return num3
    else:
        return "Todos são iguais"

num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print("Maior número: " + str(maior_de_tres(num1, num2, num3)))
