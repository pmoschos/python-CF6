# Falsy - Truthy Values
# 0, 0.0, 0j, "", [], {}, (), set(), False, None

empty_dict = {} # <class 'dict'>
print(type(empty_dict))

# 0 < a < 10
a = 5

if a > 0 and a < 10:
    print("Valid num")

if 0 < a < 10:
    print("Valid num")

# challenge
students = ("Alice", "Bob", "Charlie")

students = tuple(["Panagiotis"] + list(students)[1:])
print(students)

# enumerate()
students = ["Alice", "Bob", "Charlie", "David"]

for index, value in enumerate(students, start=100):
    print(f"{index} : {value}")

