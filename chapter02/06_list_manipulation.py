# Populate
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add
fruits.append("Berry")
print("After adding Berry", fruits)

# Add 2 or more items at the end of the list
fruits.extend(["Grapes", "Fig"])
print("After adding Berry and grapes and fig", fruits)

# insert 1 item in a specific position
fruits.insert(1, "Coconut")
print("After insert Coconut at pos 1 (2nd element)", fruits)

# update 
fruits[0] = "Melon"
print("After update element at pos 0:", fruits)

# update 2 elements
# print(fruits[1:3])
fruits[1:3] = ["A"]
print("List after update 2 elements:", fruits)

# fruits[0] = [1, 2, 3, 4]
# print(fruits)

# delete
removed_item = fruits.pop(1)
print(f"removed_item: {removed_item}")
print(fruits)

new_removed_item = fruits.remove("Cherry")
print(f"new_removed_item: {new_removed_item}")
print(fruits)

# remove a fantastic item
# fruits.remove("exotic_fruit")
# print(fruits)

if new_removed_item in fruits:
    
    print(f"{new_removed_item} removed")
else:
    print(f"Cherry doesn't exist")


# search
pos = fruits.index("Berry")
print(f"in position: {pos} exists {fruits[pos]}")