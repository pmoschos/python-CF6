items = [1, 2, 3.14, True, "Hello CF6 friends"]

for item in items:
    print(item, end=" ")
print()

nest_list = [
    [1, 2], 
    [3, 4], 
    [5, 6]
]

print(f"nested list: {nest_list}") # [[1, 2], [3, 4], [5, 6]]
print(f"first nested list: {nest_list[0]}") # [1, 2]
print(f"first element of second nested list: {nest_list[1][0]}") # 3

# [3, 4], [1, 2]
print(f"first nested list: {nest_list[1]}, {nest_list[0]}")
print(f"first nested list: {nest_list[:2][::-1]}")

for outer_item in nest_list:
    for inner_item in outer_item:
        if inner_item % 2 == 0:
            result = inner_item


print("Final even num:", result)