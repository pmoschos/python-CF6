def compare_integers(a, b):
    if a == b:
        print("Equals")
    elif a > b:
        print("First num is greater than second num")
    else:
        print("First num is less than second num")

def main():
    try:
        a = int(input("Give me the first integer: "))
        b = int(input("Give me the second integer: "))
    except ValueError:
        print("Invalid input. Please give integers")
        return

    compare_integers(a, b)

    # 1. Ternary Operator (Simple Example)
    result = "Positive" if a > 0 else "Non-positive"
    print(result)


    # if a == b:
    #     print("Equals")
    # elif a > b:
    #     print("First num is greater than second num")
    # else:
    #     print("First num is less than second num")

    # 2. Ternary Operator (Extended Example)
    res = (
        "Equals" if a == b else
        "First num is greater than second num" if a > b else
        "First num is less than second num"
    )
    print(res)

if __name__ == "__main__":
    main()