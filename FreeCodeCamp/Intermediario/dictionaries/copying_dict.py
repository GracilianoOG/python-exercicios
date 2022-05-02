mydict = {"name": "John", "lastname": "Carmack", "age": 30, "city": "New York"}
print("Original....:", mydict)

mydict_cpy = mydict
mydict_cpy2 = dict(mydict)
mydict_cpy3 = mydict.copy()

mydict["email"] = "john@abc.com"

print("Original mod:", mydict)
print("Endereço....:", mydict_cpy)
print("Dict........:", mydict_cpy2)
print("Copy()......:", mydict_cpy3)