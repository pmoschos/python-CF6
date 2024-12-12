# Geometric Shapes Area Calculation Using 'match'

Welcome to the Geometric Shapes Area Calculation Script! This Python script demonstrates how to use the `match` statement to calculate areas of various geometric shapes. The program supports `Circle`, `Rectangle`, and `Triangle` classes, and uses pattern matching to identify and handle each shape appropriately.

## Script Overview 📘

The script includes:
- A `Shape` base class and its subclasses `Circle`, `Rectangle`, and `Triangle` to represent different geometric shapes.
- A `calculate_area` function that uses the `match` keyword to calculate the area based on the shape type.
- A main block that tests the functionality with various shape instances.

### :computer: Script Code

```python
# A program that uses the 'match' keyword to work with different geometric shapes.

from math import pi

class Shape:
    """Base class for all geometric shapes."""
    def area(self):
        """Calculates the area of the shape."""
        raise NotImplementedError("Subclasses must implement the area method.")

class Circle(Shape):
    """Class representing a Circle."""
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius ** 2)

class Rectangle(Shape):
    """Class representing a Rectangle."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    """Class representing a Triangle."""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height


def calculate_area(shape):
    """
    Calculates the area of the given shape using the 'match' keyword.

    Args:
        shape: An instance of a Shape or its subclasses.
    """
    match shape:
        # Case for matching a Circle instance
        case Circle(radius=radius):
            area = shape.area()
            print(f"The area of the circle with radius {radius} is {area:.2f}.")
        
        # Case for matching a Rectangle instance
        case Rectangle(width=width, height=height):
            area = shape.area()
            print(f"The area of the rectangle with width {width} and height {height} is {area}.")
        
        # Case for matching a Triangle instance
        case Triangle(base=base, height=height):
            area = shape.area()
            print(f"The area of the triangle with base {base} and height {height} is {area}.")
        
        # Default case for unknown shapes
        case _:
            print("Unknown shape.")


# Test cases to help students understand pattern matching with geometric shapes
if __name__ == "__main__":
    # Creating instances of different shapes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 7)
    unknown_shape = Shape()

    # Calculating and printing the area of each shape
    calculate_area(circle)          # Should calculate and print the area of the circle
    calculate_area(rectangle)       # Should calculate and print the area of the rectangle
    calculate_area(triangle)        # Should calculate and print the area of the triangle
    calculate_area(unknown_shape)   # Should indicate that the shape is unknown

```

## Key Features 🌟

- **Pattern Matching**: Demonstrates Python's `match` statement to identify and process specific shape types.
- **Area Calculation**: Computes the area of `Circle`, `Rectangle`, and `Triangle` shapes using appropriate formulas.
- **Dynamic Dispatch**: Provides a clean and extensible approach to handling various shapes dynamically.

## Technical Requirements 🔧

- **Python Version**: Python 3.10 or later (required for the `match` statement).
- **External Libraries**: None (uses built-in Python functionalities).

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.10 or later is installed on your machine.
2. Save the script as `12_area_shapes_cals.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `12_area_shapes_cals.py`.
5. Run the script with: `python 12_area_shapes_cals.py`.

## Usage Example 📋

Execute the script to calculate areas of various shapes:

1. **Circle Example:**
    ```python
    circle = Circle(5)
    calculate_area(circle)
    # Output: The area of the circle with radius 5 is 78.54.
    ```

2. **Rectangle Example:**
    ```python
    rectangle = Rectangle(4, 6)
    calculate_area(rectangle)
    # Output: The area of the rectangle with width 4 and height 6 is 24.
    ```

3. **Triangle Example:**
    ```python
    triangle = Triangle(3, 7)
    calculate_area(triangle)
    # Output: The area of the triangle with base 3 and height 7 is 10.5.
    ```

4. **Unknown Shape Example:**
    ```python
    unknown_shape = Shape()
    calculate_area(unknown_shape)
    # Output: Unknown shape.
    ```

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

