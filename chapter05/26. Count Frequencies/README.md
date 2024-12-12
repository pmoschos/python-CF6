# Counting Frequencies in a List Script

Welcome to the Counting Frequencies in a List Script! This Python script demonstrates four distinct methods to count the frequency of items in a list, showcasing various approaches to achieve the same goal with different techniques and built-in functionalities.

---

## Script Overview 📘

The script explores the following methods:

1. **Dictionary Comprehension**: Uses dictionary comprehension to create a frequency dictionary.
2. **Manual Loop with Conditional Checks**: Iteratively builds the frequency dictionary by checking if the key exists.
3. **Manual Loop with `get()` Method**: Utilizes the `get()` method to handle missing keys during frequency calculation.
4. **`Counter` from `collections` Module**: Leverages Python’s `collections.Counter` for a concise and powerful solution.

### :computer: Script Code

```python
from collections import Counter

def count_with_dict_comprehension(my_list):
    """
    Count frequencies using dictionary comprehension.
    """
    frequency_dict = {item: my_list.count(item) for item in set(my_list)}
    print("\nDictionary Comprehension:", frequency_dict)

def count_with_manual_loop(my_list):
    """
    Count frequencies using a manual loop and conditional check.
    """
    frequency_dict = {}
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    print("\nManual Loop:", frequency_dict)

def count_with_get_method(my_list):
    """
    Count frequencies using a manual loop with `get()` method for default values.
    """
    frequency_dict = {}
    for item in my_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    print("\nManual Loop with get():", frequency_dict)

def count_with_counter(my_list):
    """
    Count frequencies using `Counter` from the `collections` module.
    """
    frequency_dict = Counter(my_list)
    print("\nUsing Counter:", frequency_dict)
    # Get elements sorted by frequency
    sorted_by_freq = frequency_dict.most_common()
    print("\nSorted by Frequency:", sorted_by_freq)

def main():
    # Original list of strings
    my_list = ["apple", "banana", "kiwi", "apple", "orange", "banana", "apple", "kiwi", "melon", "kiwi", "kiwi"]

    # Demonstrate different ways to count frequencies
    count_with_dict_comprehension(my_list)
    count_with_manual_loop(my_list)
    count_with_get_method(my_list)
    count_with_counter(my_list)

if __name__ == "__main__":
    main()
```

---

## Key Features 🌟

- **Diverse Approaches**: Illustrates four distinct ways to solve the same problem.
- **Use of `collections.Counter`**: Demonstrates the power of Python’s standard library.
- **Sorted Output**: Shows how to sort elements by frequency with `Counter.most_common()`.

---

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended.
- **External Libraries**: None (uses the built-in `collections` module).

---

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `count_frequencies.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `count_frequencies.py`.
5. Run the script with:

   ```bash
   python count_frequencies.py
   ```

---

## Usage Example 📋

Execute the script to see the output for the sample list:

```plaintext
Dictionary Comprehension: {'banana': 2, 'apple': 3, 'kiwi': 4, 'orange': 1, 'melon': 1}

Manual Loop: {'apple': 3, 'banana': 2, 'kiwi': 4, 'orange': 1, 'melon': 1}

Manual Loop with get(): {'apple': 3, 'banana': 2, 'kiwi': 4, 'orange': 1, 'melon': 1}

Using Counter: Counter({'kiwi': 4, 'apple': 3, 'banana': 2, 'orange': 1, 'melon': 1})

Sorted by Frequency: [('kiwi', 4), ('apple', 3), ('banana', 2), ('orange', 1), ('melon', 1)]
```

---

## 📲 Contact and Contribution

### Contact 📧
- **Author**: Panagiotis Moschos
- **Email**: pan.moschos86@gmail.com
- **GitHub**: [pmoschos](https://github.com/pmoschos)

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).


## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by 
  <a href="https://www.linkedin.com/in/panagiotis-moschos" target="_blank">
  Panagiotis Moschos</a> (https://github.com/pmoschos)
</p>

