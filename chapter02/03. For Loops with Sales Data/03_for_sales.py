# List of fruits:
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# fruit we want to check
fruit_to_check = "Banana"

for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in list")
        break
else:
    print(f"{fruit_to_check} is not in list")

print("Why do Python devs never get lost?")
print("Because the always know where 'in' is!")

if fruit_to_check in fruits:
    print(f"{fruit_to_check} is in list")
else:
    print(f"{fruit_to_check} is not in list")

print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list!")