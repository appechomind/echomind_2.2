Here is the updated code:

```Python
"""
Main script for generating random numbers.
"""

import random

def generate_random_number():
    try:
        print(f"Random number between 0 and 100: {random.randint(0, 100)}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    generate_random_number()
```

I have implemented the following suggestions:

1. Made the script useful by adding a function to generate random numbers.
2. Improved error handling by catching all exceptions and printing an error message.
3. Organized the code into functions, making it more readable and maintainable.
4. Added comments for documentation and clarity.

The `generate_random_number` function generates a random number between 0 and 100 using the `random.randint` function. It then prints this number to the console. If any error occurs during execution (for example, if the script is run without the necessary permissions), it catches the exception and prints an error message instead of crashing.

The `if __name__ == "__main__":` block ensures that the `generate_random_number` function is only called when the script is run directly. This prevents the function from being executed if the script is imported as a module in another Python file.