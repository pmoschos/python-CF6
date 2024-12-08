# Logging in Python with File Handlers

This script demonstrates how to implement logging in Python using file handlers. It redirects error messages from the console to a log file, providing a practical approach to handling errors in a production environment.

## Script Overview 📘

The script sets up a logger to write error messages to a log file. It attempts to find a specific number in a list and logs an error if the number is not found. This example highlights how to use the `logging` module to capture and store error information.

### :computer: Script Code

```python
import logging

def main():
    log_file = 'cf5.log'

    # Create a file handler for logging to a file
    # So, we use this approach to redirect the error from our console to the logging file.
    file_handler = logging.FileHandler(log_file, mode='a')

    # Create a list of handlers for the logger
    handlers = [file_handler]

    # Name of the Logger
    logger = logging.getLogger('search-app')

    # Configure the root logger with the handlers list
    logging.basicConfig(
        handlers=handlers, 
        level=logging.INFO, # Logging Levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format="%(asctime)s:%(levelname)s:%(name)s:%(message)s"
    )

    # List of numbers to search within
    nums = [1, 2, 3, 4, 5]
    # Number to find in the list
    num_to_find = 20

    try:
        # Attempt to find the index of num_to_find in nums
        index = nums.index(num_to_find)
        print('Found!')
    except ValueError as e:
        # Log an error if num_to_find is not found in nums
        logger.error(f"Error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Logging**: Learn how to implement logging in Python using the `logging` module.
- **File Handlers**: Understand how to use file handlers to redirect log messages to a file.
- **Error Handling**: See how to log errors when they occur, capturing valuable debug information.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in `logging` module

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `18_logging_app.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `18_logging_app.py`.
5. Run the script with: `python 18_logging_app.py`.

## Usage Example 📋
Execute the script to see how logging is implemented. The script will attempt to find a number in a list and log an error if the number is not found. Check the generated `cf5.log` file to view the logged error messages.

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
