# Python String Handling Demonstration

Welcome to the Python String Handling Demonstration! This script illustrates how to manipulate and navigate strings in Python using indexing, loops, and string properties like immutability. It's an ideal resource for anyone new to Python or those teaching fundamental programming concepts related to string operations.

## Script Overview 📘

The script demonstrates the basic yet essential string operations such as accessing characters via indexing, using loops to iterate over strings, and understanding Python's string immutability. These operations are crucial for mastering string manipulation in Python.

### :computer: Script Code

```python
# Define a string variable
message = "Coding Factory"

# Print individual characters using indexing (zero-indexed)
print(message[0])  # 'C'
print(message[1])  # 'o'
print(message[2])  # 'd'
print(message[3])  # 'i'
print(message[4])  # 'n'
print(message[5])  # 'g'

# Strings in Python are immutable, which means you cannot change an existing string directly
# The following line, if uncommented, would result in a TypeError because strings cannot be modified
# message[0] = 'c'

# Use len() to get the number of characters in the string
print(f"Number of letters inside the {message}: {len(message)}")  # Outputs the length of the message

# Iterate over each character in the string using a simple for-loop
# This is often called an "enhanced for" loop, similar to foreach in other languages
for char in message:
    print(char)  # Prints each character on a new line

# The range function generates a sequence of numbers, which by default starts from 0 and goes up to n-1
for i in range(10):
    print(i)  # Prints numbers 0 to 9

# Iterate over the string by index using a for-loop with range based on the length of the message
# Print each character without newline, separated by a space
for i in range(len(message)):
    print(message[i], end=" ")  # end=" " keeps the output on the same line
print()  # Print a newline at the end


# @ANTONIOY IOANNIS
number = 12345678
number_str = str(number)

# Print individual characters using indexing (zero-indexed)
#μπορουμε ενα string πχ  ονομα, επιθετο , ιδιοτητα κτλ να το χειριστουμε σαν μονοδιαστατο πινακα μιας γραμμης
#και να εκτυπωσουμε ενα ενα τα γραμματα του.
# Μπορουμε να το κανουμε και στους αριθμους αρκει να τους εχουμε "φερει" σαν string!!!!

print("\nprint the variable number_str per char\n")
print(int(number_str[0]))  # '1'
print(int(number_str[1]))  # '2'
print(number_str[2])  # '3'
print(number_str[3])  # '4'
print(number_str[4])  # '5'
print(number_str[5])  # '6'
print(number_str[6])  # '7'
print(int(number_str[7]))  # '8'
print("... end of variable number_str\n")

# αν θελουμε μπορουμε να ξανακανουμε int τον καθε αριθμο -οπως πχ ανωθεν τους [0],[1],[7]- και να τους χειριστουμε ξανα σας αριθμους
print("\n-----\nΤο σύνολο του πρώτου [0] και του δεύτερου αριθμου [1] ειναι: ", int((number_str[0])) + int((number_str[1])), ".")
print("Το σύνολο του πρώτου [0] και του όγδοου αριθμού [7] είναι: ", int((number_str[0])) + int((number_str[7])), ".  \n-----\n")


# Strings in Python are immutable, which means you cannot change an existing string directly
# The following line, if uncommented, would result in a TypeError because strings cannot be modified
# message[0] = 'c'

# Use len() to get the number of characters in the string
print(f"Number of letters inside the {message}: {len(message)}")  # Outputs the length of the message

# Iterate over each character in the string using a simple for-loop
# This is often called an "enhanced for" loop, similar to foreach in other languages
for char in message:
    print(char)  # Prints each character on a new line

# The range function generates a sequence of numbers, which by default starts from 0 and goes up to n-1
for i in range(10):
    print(i)  # Prints numbers 0 to 9

# Iterate over the string by index using a for-loop with range based on the length of the message
# Print each character without newline, separated by a space
for i in range(len(message)):
    print(message[i], end=" ")  # end=" " keeps the output on the same line
print()  # Print a newline at the end
```

## Key Features 🌟

- **String Indexing**: Understand how to access individual characters in a string using indexing.
- **Immutability of Strings**: Learn why strings in Python are immutable and how this affects string manipulation.
- **Looping Over Strings**: Explore different methods to iterate over strings, enhancing your ability to handle string data.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Download `18_string_indexing_traverse.py` from this repository.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `18_string_indexing_traverse.py`.
5. Run the script with: `python 18_string_indexing_traverse.py`.

## Usage Example 📋

Execute the script to see how string indexing, immutability, and iteration are performed in the console. This demonstration will deepen your understanding of string manipulation techniques in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align="center">Happy Coding 👨‍💻</h1>

<p align="center">
  Made with ❤️ by <a href="https://www.linkedin.com/in/panagiotis-moschos">Panagiotis Moschos</a> (<a href="https://github.com/pmoschos">GitHub</a>)
</p>