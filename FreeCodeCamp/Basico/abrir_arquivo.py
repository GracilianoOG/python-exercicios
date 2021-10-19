arquivo_empregado = open("FreeCodeCamp\empregados.txt", "r")

for empregado in arquivo_empregado.readlines():
    print(empregado)

arquivo_empregado.close()
