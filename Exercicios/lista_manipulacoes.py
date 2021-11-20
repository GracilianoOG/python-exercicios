# Criação de listas
print("\n--- Criação das listas ---")
lista = [0, 1, 2, 3, 4, 5, 6]
lista_copia = lista[:]
lista_copia2 = lista.copy()
lista_mesma_ref = lista
print("Tipo da lista...........: ", type(lista))
print("Lista original..........:", lista)
print("Lista copiada com [:]...:", lista_copia)
print("Lista copiada com copy():", lista_copia2)
print("Lista referenciada......:", lista_mesma_ref)
print("\n--- Alteração da lista original ---")
lista.append("mudei")
print("Lista original..........:", lista)
print("Lista copiada com [:]...:", lista_copia)
print("Lista copiada com copy():", lista_copia2)
print("Lista referenciada......:", lista_mesma_ref)
print("\n--- Pop da lista original ---")
lista.pop()
print("Lista original..........:", lista)
print("Lista copiada com [:]...:", lista_copia)
print("Lista copiada com copy():", lista_copia2)
print("Lista referenciada......:", lista_mesma_ref)
print("\n--- Limpeza de algumas listas ---")
del lista_copia[:]
lista_copia2.clear()
print("Lista com [:] vazia...:", lista_copia)
print("Lista com copy() vazia:", lista_copia2)
del lista_copia
del lista_copia2
del lista_mesma_ref

# Printando todos os elementos, um a um
print("\n--- Printando todos com loop for ---")
for item in lista:
    print(item, end=" ")
print()

for indice in range(len(lista)):
    print(lista[indice], end=" ")
print()

# Printando elementos da lista
print("\n--- Printando individual ---")
print("[-1]", lista[-1])  # Último item da lista
print("[6]", lista[6])
print("[0]", lista[0])
print("[1]", lista[1])
print("[0:1]", lista[0:1])
print("[0:2]", lista[0:2])
print("[1:3]", lista[1:3])
print("[1:6:2]", lista[1:6:2])  # Pos. 1 até 5 de 2 em 2

# Métodos diversos
print("\n--- Diversos ---")
print("Somar com sum(): {}".format(sum(lista)))
print("Menor com min(): {}".format(min(lista)))
print("Maior com max(): {}".format(max(lista)))

# Manipulação da lista
print("\n--- Manipulação ---")
print(lista)
lista.append(7)  # Adiciona o 7 ao final da lista
print(lista, "<- append(7)")
lista.insert(-1, 7)  # Colocar o 7 na última posição
print(lista, "<- insert(-1, 7)")
lista.pop()  # Remove o último item
print(lista, "<- pop()")
lista.pop(7)
print(lista, "<- pop(7)")
lista.reverse()  # Inverte a lista
print(lista, "<- reverse()")
lista.sort()  # Ordena a lista
print(lista, "<- sort()")
print()
