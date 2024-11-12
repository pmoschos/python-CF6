message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

print(f"Number of letters in {message}: {len(message)}")

for char in message:
    print(char, end=" ")
print()

print(type(range(100_000_000)))

for i in range(10):
    print(i, end=" ")
print()

for i in range(len(message)):
    print(message[i], end=" ")
print()

# range(start, stop, step)
# start: inclusive
# stop: exclusive
for i in range(0, 10, 2):
    print(i, end=" ")