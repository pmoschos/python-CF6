def process_characters():
    ch = input("Please insert a char: ")

    while ch != "#":
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
    
    print("Goodbye")

def process_characters2():
    while True:
        ch = input("Please insert a char: ")
        if ch == "#":
            break
        print(ch, ":", ord(ch))

def main():
    process_characters()

if __name__ == "__main__":
    main()