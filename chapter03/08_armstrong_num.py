def is_armostrong_number(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power
    
    return n == total

def main():
    try:
        num = int(input("Please insert an int: "))
    except ValueError:
        print("Invalid number")
        return
    
    if is_armostrong_number(num):
        print(f"{num} is an Armstron number")
    else:
        print(f"{num} isn't an Armstron number")

if __name__ == "__main__":
    main()