mydict = {"name": "John", "lastname": "Carmack", "age": 30, "city": "New York"}
print(mydict)

key = "name"

# if in
if key in mydict:
    print(mydict[key])

# Try / Except
try:
    print(mydict[key])
except:
    print("error")