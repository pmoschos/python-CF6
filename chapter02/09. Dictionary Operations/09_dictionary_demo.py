# populate dictionary (dict)
products = {
    1:"apples", 
    2:"bananas", 
    3:"honey", 
    4:"melons"
}

print("Initial products: ", products)

# insert a new product
products[15] = "oranges"
print("Products after insertion:", products)

# get the product with id: 3
print(products[3])

# update
products[2] = "milk"
print("Products after update:", products)

# delete
# del products[100]
# print("Products after deletion:", products)

removed_product = products.pop(100, "Not found")
print(f"removed_product: {removed_product}")
print("Products after deletion:", products)

# popitem() remove 'last' item
# product = products.popitem()
# print(type(product))

key, value = products.popitem()
print(f"{key} : {value}")
print(products)

# {1: 'apples', 2: 'milk', 3: 'honey', 4: 'melons'}

key_to_check = 20

if key_to_check in products:
    print(f"{key_to_check} exists")
else:
    print(f"{key_to_check} doesn't exist")

# get keys from a dictionary
for key in products.keys():
    print(key)

# get values from a dictionary
for value in products.values():
    print(value)

# iterate a dictionary
for key in products.keys():
    print(f"{key} : {products[key]}")

print("--------------------------")
for key, value in products.items():
    print(f"{key} : {value}")