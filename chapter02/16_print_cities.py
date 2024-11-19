def print_cities(*cities, separator = ", ", end = "\t"):
    """
    ....
    *cities (str): .... 
    """
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities), sep=separator, end=end)

def main():
    # Cities: Athens, London, Paris
    print_cities("Athens", "London", "Paris", separator=" | ", end=".")
    # print_cities("Athens")
    # print_cities()

if __name__ == "__main__":
    main()