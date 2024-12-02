def name_spacing(num: int):
    if not isinstance(num, int):
        print("The number of given spaces must be int.")
        return
    
    if num < 0:
        print("The number of given spaces must be positive")
        return
    
    name = input("Please give me a name: ").strip()

    if not name:
        print("No name provided!")
        return
    
    spaced_name = (" " * num).join(name)
    print(spaced_name)


def main():
    num = int(input("Give an int: "))

    name_spacing(num)

if __name__ == "__main__":
    main()