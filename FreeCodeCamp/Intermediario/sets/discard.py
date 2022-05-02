myset = {1, 2, 3, 4, 5, 6, 7, 8}
print(myset)

myset.discard(3)
myset.discard(1)
myset.discard(1)  # Não retorna erro ao deletar algo que não existe no set
print(myset)