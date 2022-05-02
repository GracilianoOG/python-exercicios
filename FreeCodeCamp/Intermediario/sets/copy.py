myset_ogr = {1, 2, 3, 4, 5}
myset_cpy1 = myset_ogr
myset_cpy2 = myset_ogr.copy()
myset_cpy3 = set(myset_ogr)

myset_ogr.add(6)

print("Original:", myset_ogr)
print("Memória.:", myset_cpy1)
print("copy()..:", myset_cpy2)
print("set()...:", myset_cpy3)