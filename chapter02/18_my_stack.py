import re

stack = []
num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list: # if list isn't empty! ([] - > empty list)
        list.pop()
    else:
        print("Stack is empty")

def print_stack(list):
    if list:
        print("Current stack:", list)
    else:
        print("Stack is empty")

def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. Print Stack")
    print("4. q/Q for Quit")

def get_choice():
    return input("Please provide a choice\n")


def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        if choice == 'q' or choice == "Q":
            break




if __name__ == "__main__":
    main()