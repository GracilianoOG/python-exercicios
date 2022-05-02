# Pega todos os itens diferentes que estejam em ambos os sets, oposto da intersection

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff1 = setA.symmetric_difference(setB)
print(diff1)

diff2 = setB.symmetric_difference(setA)
print(diff2)