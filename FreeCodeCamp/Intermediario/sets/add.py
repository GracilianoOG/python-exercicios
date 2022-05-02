myset = set()
print(type(myset))
print(myset)

myset.add(1)
myset.add(1)  # Não adiciona duplicados
myset.add(2)
myset.add(3)

print(myset)