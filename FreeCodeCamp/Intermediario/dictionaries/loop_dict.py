mydict = {"name": "John", "lastname": "Carmack", "age": 30, "city": "New York"}
print(mydict)

print("==========================")  # Mostra todas as chaves
for key in mydict:
    print(key)

print("==========================")  # Mostra todas as chaves
for key in mydict.keys():
    print(key)

print("==========================")  # Mostra todos os valores
for value in mydict.values():
    print(value)

print("==========================")  # Mostra a chave e o valor
for key, value in mydict.items():
    print(key, ":", value)

print("==========================")