# Verifica se todos os itens do primeiro set estão no segundo set
# Se TODOS os elementos do setA estiverem no setB, então setA é subset de setB

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setB.issubset(setA))
print(setB.issubset(setB))