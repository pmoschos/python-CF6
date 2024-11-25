def print_cities(*cities):
    if not cities:
        print("No cities provided")
    else:
        print("Cities:", ", ".join(cities))

def main():
    # Cities: Athens, London, Paris
    print_cities("Athens", "London", "Paris")
    print_cities("Athens")
    print_cities()

if __name__ == "__main__":
    main()