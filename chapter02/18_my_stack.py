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

