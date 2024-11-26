def is_square(length, width):
    return length == width

def main():
    try:
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
    except ValueError:
        print("Invalid input. Please give an integer.")
        return

    if is_square(length, width):
        print("Rectangle is a square")
    else:
        print("Rectangle is not square")

if __name__ == "__main__":
    main()