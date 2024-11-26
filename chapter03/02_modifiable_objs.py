def print_id(variable_name, variable):
    print(f"id({variable_name}) = {id(variable)}")


def main():
    original_list = [1, 2]
    new_list = original_list

    print_id("original_list", original_list)
    print_id("new_list", new_list)

    print("------")
    new_list[0] = 100
    print_id("original_list", original_list)
    print_id("new_list", new_list)

    print("original_list", original_list)
    print("new_list", new_list)
    print("------")

    temp_list = [1, 2]
    print_id("temp_list", temp_list)

    print("Original List")
    # bonues (spoiler)
    print(original_list)
    print(*original_list)

if __name__ == "__main__":
    main()