list_orgn = ["banana", "apple", "grape"]

# Copy but share the same memory space
list_cpy1 = list_orgn

# Copy only the elements inside, do not share the same memory space
list_cpy2 = list(list_orgn)
list_cpy3 = list_orgn.copy()
list_cpy4 = list_orgn[:]
list_orgn.append("lemon")

# Prints
print("Appending 'lemon' in the original list...")
print("Original.........:", list_orgn)
print("Same memory space:", list_cpy1)
print("List method......:", list_cpy2)
print("Copy method......:", list_cpy3)
print("Slicing method...:", list_cpy4)