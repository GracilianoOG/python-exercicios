# Remove elementos iguais ao outro set, atualização

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

setA.difference_update(setB)
print(setA)