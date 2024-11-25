students = "Alice", "Bob", "Charlie"

print(type(students))

# iterate
for index, student in enumerate(students):
    print(f"{index} : {student}")

# enhanced for
for student in students:
    print(student)

# first_st = students[0]
# second_st = students[1]
# third_st = students[2]

first_st, second_st, third_st = students

print(f"first_st: {first_st}")
print(f"second_st: {second_st}")
print(f"third_st: {third_st}")

# students = "Alice", "Bob", "Charlie"

students = list(students)
students[0] = "Panagiotis"
students = tuple(students)

print(students)
print(type(students))