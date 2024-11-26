def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

def main():
    try:
        num = int(input("Please insert a posivite int: "))
        if num <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number")
        return

    facto = calculate_factorial(num)

    print(f"{num}! = {facto}")

if __name__ == "__main__":
    main()