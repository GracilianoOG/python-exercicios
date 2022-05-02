# Verifica se o primeiro set é PAI do segundo set. Se tem todos os elementos do filho
# Se o pai (superset) tiver os elementos do seu filho (subset), então é o pai legítimo

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issuperset(setB))
print(setB.issuperset(setA))
print(setB.issuperset(setB))