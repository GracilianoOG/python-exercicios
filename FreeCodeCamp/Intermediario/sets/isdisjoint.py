# Se ambos os sets não tiverem NENHUM elemento semelhante, retorna true

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}

print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))