# Set Operations in Python

This script demonstrates various set operations in Python, including intersection, union, difference, and symmetric difference. These operations are useful for comparing and manipulating sets of data.

## Script Overview 📘

The script defines two sets and performs several operations to find common elements, all elements, elements in one set but not the other, and elements in either set but not both.

### :computer: Script Code

```python
def main():
    """
    Main function to demonstrate set operations in Python.
    """
    # Define two sets
    bag1 = {"A1", "A2", "A3", "A4", "BA1"}
    bag2 = {"A1", "A2", "B3", "B4", "BB2"}

    # Find common elements (intersection) of bag1 and bag2
    common_elements = bag1 & bag2
    # Alternatively, using the intersection method
    common_elements = bag1.intersection(bag2)
    print("Common elements of bag1 and bag2:", common_elements)

    # Find all elements (union) of bag1 and bag2
    all_the_elements = bag1 | bag2
    # Alternatively, using the union method
    all_the_elements = bag1.union(bag2)
    print("All elements of bag1 and bag2:", all_the_elements)

    # Find elements in bag1 but not in bag2 (difference)
    diff1 = bag1 - bag2
    # Alternatively, using the difference method
    diff1 = bag1.difference(bag2)
    print("Elements in bag1 but not in bag2:", diff1)

    # Find elements that are in either bag1 or bag2 but not both (symmetric difference)
    diff2 = bag1 ^ bag2
    # Alternatively, using the symmetric_difference method
    diff2 = bag1.symmetric_difference(bag2)
    print("Elements in either bag1 or bag2 but not both:", diff2)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Set Operations**: Learn how to perform various set operations such as intersection, union, difference, and symmetric difference.
- **Methods**: Understand the use of set methods like `intersection`, `union`, `difference`, and `symmetric_difference`.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in set operations

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `20_set_operations.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `20_set_operations.py`.
5. Run the script with: `python 20_set_operations.py`.

## Usage Example 📋
Execute the script to see how set operations are performed. The script will output the common elements, all elements, elements in one set but not the other, and elements in either set but not both.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
