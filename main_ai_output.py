Here is the updated code:

```
def generate_random_numbers(n: int, min_value: int = 0, max_value: int = 100) -> list:
    """
    Generates a list of 'n' random numbers between 'min_value' and 'max_value'.

    Args:
        n (int): The number of random numbers to generate.
        min_value (int): The minimum value for the random range. Default is 0.
        max_value (int): The maximum value for the random range. Default is 100.

    Returns:
        list: A list of 'n' random numbers between 'min_value' and 'max_value'.

    Raises:
        ValueError: If 'n' is not a positive integer.
    """
    import random
    if n < 1:
        raise ValueError("Number of random numbers must be a positive integer.")
    return [random.randint(min_value, max_value) for _ in range(n)]

numbers = generate_random_numbers(10)
print(numbers)

if __name__ == '__main__':
    print('Auto-created main.py')
```