def print_id(variable_name, variable):
    print(f"id({variable_name}) = {id(variable)}")


def main():
    a = 10
    b = 10

    str1 = "CF6"
    str2 = 'CF6'

    print_id("a", a)
    print_id("b", b)

    print_id("str1", str1)
    print_id("str2", str2)

    b = 20
    print_id("a", a)
    print_id("b", b)


if __name__ == "__main__":
    main()