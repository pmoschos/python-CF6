name = input("Please enter your name: ")

is_stundent = input("Are you a student? (yes/no): ").lower() == "yes"

print(f"name: {name}")
print(f"is_student: {is_stundent}")

if is_stundent:
    print("You are a student")
else:
    print("You are not a student")

