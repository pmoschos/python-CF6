a = 10
b = 20

result = a + b

print(f"{a} + {b} = {result}")

print(f"Type(a): {type(a)}")

magic_result = a.__add__(b)

print(f"Magic: {a} + {b} = {magic_result}")