# 🪢 Python Multiple Inheritance Demonstration 🔀

Welcome to the Python Multiple Inheritance Demonstration! This script showcases how multiple inheritance can be implemented in Python through a `WorkingStudent` class that inherits from `Person`, `Worker`, and `Student`. It’s an excellent resource for understanding class inheritance and combining functionalities.

## Script Overview 📘

The script demonstrates:
- Basic inheritance using Python classes.
- Combining attributes and methods from multiple parent classes.
- Defining a derived class that inherits and initializes multiple base classes.

### 💻 Script Code

```python
class Person:
    """
    Base class representing a person.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def display_info(self) -> None:
        print(f"Name: {self.name}, Age: {self.age}")


class Worker:
    """
    Class representing a worker.
    """
    def __init__(self, job_title: str, company: str):
        self.job_title = job_title
        self.company = company

    def work(self) -> None:
        print(f"{self.job_title} working at {self.company}.")


class Student:
    """
    Class representing a student.
    """
    def __init__(self, major: str, university: str):
        self.major = major
        self.university = university

    def study(self) -> None:
        print(f"Studying {self.major} at {self.university}.")


class WorkingStudent(Person, Worker, Student):
    """
    Derived class representing a person who is both a worker and a student.
    """
    def __init__(self, name: str, age: int, job_title: str, company: str, major: str, university: str):
        # Initialize all parent classes
        Person.__init__(self, name, age)
        Worker.__init__(self, job_title, company)
        Student.__init__(self, major, university)


# Demonstrating the WorkingStudent class
def main() -> None:
    # Create a WorkingStudent object
    ws = WorkingStudent(
        name="Alice",
        age=25,
        job_title="Software Engineer",
        company="TechCorp",
        major="Computer Science",
        university="MIT"
    )

    # Display person information
    ws.display_info()
    # Show work-related details
    ws.work()
    # Show study-related details
    ws.study()


if __name__ == "__main__":
    main()
```

## Key Features 🌟

- **Basic Inheritance**: Demonstrates the use of inheritance with separate classes for `Person`, `Worker`, and `Student`.
- **Multiple Inheritance**: Combines the functionalities of three base classes into the derived `WorkingStudent` class.
- **Overriding Initialization**: Illustrates how to initialize all parent classes explicitly in a derived class.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

This script can be run directly in any Python environment. Follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Save the script as `24_multiple_inheritance_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `24_multiple_inheritance_demo.py`.
5. Run the script with the command: `python 24_multiple_inheritance_demo.py`.

## Usage Example 📋

Executing the script demonstrates how a `WorkingStudent` object combines the functionalities of a `Person`, `Worker`, and `Student`. The object can display personal information, perform work-related actions, and show study details, showcasing the power of multiple inheritance in Python.

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

