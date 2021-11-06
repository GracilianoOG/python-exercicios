# Sets (conjuntos)
conjunto1 = {1, 2, 3, 4}
conjunto2 = {5, 6, 7, 8, 9}

# Manipulação de conjuntos
conjunto1.add(5)
conjunto2.discard(9)

# Print dos conjuntos
print("Conjunto 1: {}".format(conjunto1))
print("Conjunto 2: {}\n".format(conjunto2))

# União de conjuntos (junta os sets, descarta itens repetidos)
conjunto_uniao = conjunto1.union(conjunto2)
print("União: {}\n".format(conjunto_uniao))

# Intersecção de conjuntos (itens iguais)
conjunto_interseccao = conjunto1.intersection(conjunto2)
print("Intersecção: {}\n".format(conjunto_interseccao))

# Diferença de conjuntos (itens diferentes de um pro outro)
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print("Diferença entre C1 e C2: {}".format(conjunto_diferenca1))
print("Diferença entre C2 e C1: {}\n".format(conjunto_diferenca2))

# Diferença simétrica de conjuntos (todos os itens diferentes)
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print("Diferença simétrica: {}\n".format(conjunto_diff_simetrica))

# Conjuntos (superset e subset)
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset1 = conjunto_a.issubset(conjunto_b)
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
conjunto_superset1 = conjunto_a.issuperset(conjunto_b)
conjunto_superset2 = conjunto_b.issuperset(conjunto_a)

# Prints dos supersets e subsets
print("Conjunto A: {}".format(conjunto_a))
print("Conjunto B: {}".format(conjunto_b))
print("A é superconjunto de B?: {}".format(conjunto_superset1))
print("B é superconjunto de A?: {}".format(conjunto_superset2))
print("A é subconjunto de B?..: {}".format(conjunto_subset1))
print("B é subconjunto de A?..: {}\n".format(conjunto_subset2))

# Converter lista em set
lista_animais = ["gato", "gato", "peixe", "peixe", "elefante"]
conju_animais = set(lista_animais)
print("Lista de animais...........: {}".format(lista_animais))
print("Conjunto de animais........: {}".format(conju_animais))
print("Lista de animais convertida: {}\n".format(list(conju_animais)))
