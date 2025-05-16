Here is the updated code:
```python
"""
Main Python Script: A Simple Calculator
=====================================

This script provides a basic calculator functionality, allowing users to perform simple arithmetic operations.
"""

def calculate(expression):
    """
    Evaluate a mathematical expression and return the result.

    Args:
        expression (str): The mathematical expression to evaluate.

    Returns:
        float or int: The result of the evaluation.
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    while True:
        user_input = input("Enter a mathematical expression (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            result = calculate(user_input)
            if result is not None:
                print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
I've added:

* A simple calculator functionality using the `eval()` function to evaluate mathematical expressions.
* Error handling to catch potential errors and provide informative error messages.
* A basic command-line interface for users to input mathematical expressions or quit the program.

The code is now structured into a main `main()` function, which contains a loop that repeatedly prompts the user for input until they choose to quit. The `calculate()` function takes an expression as input and attempts to evaluate it using `eval()`. If an error occurs during evaluation, the error message is printed and the program continues running.