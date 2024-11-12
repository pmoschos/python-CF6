import math

name = "Alice"
age = 20

print("PI=", math.pi)

# string concat
# print(name + " is " + age + " years old.")
print(name + " is " + str(age) + " years old.")

# Python 2 style
print("PI = %6.2f" %math.pi)
print("%s is %d years old" %(name, age))

# Python 3 style (using format)
print("Age is {0:2d}".format(age))
print("PI = {0:.3f}".format(math.pi))

print("{0} is {1} years old".format(name, age))

# string formating
print("{0:*^10} : {1:<20}".format(name, age), end=".\n")

# Demonstrate modern Python 3 style string interpolation using f-strings
print(f"{name} is {age} years old.")
