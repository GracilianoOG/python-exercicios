def fibonacci(seq):
    atual = 0
    proxima = 1

    for i in range(seq):
        print(atual, end=" ")
        atual, proxima = proxima, proxima + atual


fibonacci(20)