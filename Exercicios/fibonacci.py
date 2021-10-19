# Sequência Fibonacci

fib1 = 0
fib2 = 1
sequencias = -1

while sequencias < 1 or sequencias > 20:
    sequencias = int(input("Digite o números de sequências Fibonacci (1 - 20): "))

for sequencia in range(sequencias):
    print(fib2, end=" ")
    fib1, fib2 = fib2, fib1 + fib2
