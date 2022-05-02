mydict = {"name": "John", "lastname": "Carmack", "age": 30, "city": "New York"}
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()  # Deleta o último item
print(mydict)