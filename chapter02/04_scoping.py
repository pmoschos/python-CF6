import random

random_numbers = []

# use for loop to generate 10 random integers
for _ in range(10):
    num = random.randint(1, 100)
    random_numbers.append(num)

print(random_numbers)

# last even number of the list (even)
for num in random_numbers:
    if num % 2 == 0:
        even = num

print(f"The last item of the list: {num}")
print(f"The last 'even' itam of the list: {even}")