# Pega todos os itens diferentes que estejam no PRIMEIRO set

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff1 = setA.difference(setB)
print(diff1)

diff2 = setB.difference(setA)
print(diff2)