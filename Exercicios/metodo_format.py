a = int(input("Informe o primeiro valor: "))
b = int(input("Informe o segundo valor: "))

soma = a + b
subtracao = a - b
divisao = a / b
resto_divisao = a % b
multiplicacao = a * b

# Alias (apelidos) são usados entre chaves para indicar onde cada variável irá entrar.
# A barra invertida \ indica que há código na próxima linha.
resultado = "\nSoma: {som}\nSubtração: {sub}\nDivisão: {div}\nResto: {res}\nMultiplicação: {mul}\n" \
    .format(som=soma, sub=subtracao, div=divisao, res=resto_divisao, mul=multiplicacao)

print(resultado)
