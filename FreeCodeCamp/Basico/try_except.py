try:
    num1 = float(input("Informe um número: "))
    num2 = float(input("Informe outro número: "))
    result = num1 / num2
    print(result)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
