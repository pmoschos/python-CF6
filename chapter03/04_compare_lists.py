def compare_lists(list1, list2):
    print(f"{list1} is {list2}: {list1 is list2}")
    print(f"{list1} == {list2}: {list1 == list2}")


def main():
    my_list = [1, 2, 3]
    your_list = [1, 2, 3]

    print(id(my_list), id(your_list))

    compare_lists(my_list, your_list)

if __name__ == "__main__":
    main()