Here's an example of how you could refactor this code:

```python
def print_greeting(name):
    """Print a custom greeting"""
    try:
        if name:
            print(f"Welcome, {name}!")
        else:
            print("Welcome to my Python script!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    name = input("Enter your name (optional): ")
    print_greeting(name)
```

In this updated code, I've added a `print_greeting` function that takes an optional name parameter. The function prints a custom greeting message based on the provided name, and also includes basic error handling using a try-except block. In the main part of the script, I've used the `input` function to get user input for their name, which is then passed to the `print_greeting` function.