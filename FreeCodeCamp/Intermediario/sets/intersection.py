# Interseção pega o item que aparece em ambos os sets, oposto do symmetric_difference

pares = {0, 2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}
primos = {2, 3, 5, 7}

Intersecao1 = pares.intersection(impares)
print(Intersecao1)

Intersecao2 = pares.intersection(primos)
print(Intersecao2)

Intersecao3 = impares.intersection(primos)
print(Intersecao3)