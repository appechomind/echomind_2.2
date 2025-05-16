Here is the updated code:

```
import random

def generate_random_numbers(n: int, min_value: int = 1, max_value: int = 100) -> list[int]:
    """
    Generate a list of n random integers between min_value and max_value (inclusive).

    Args:
        n (int): The number of random integers to generate.
        min_value (int): The minimum value for the random numbers. Defaults to 1.
        max_value (int): The maximum value for the random numbers. Defaults to 100.

    Returns:
        list[int]: A list of n random integers between min_value and max_value.
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")
    if n < 0:
        raise ValueError("Input 'n' cannot be negative.")

    if min_value > max_value:
        raise ValueError(f"min_value {min_value} is greater than max_value {max_value}.")

    numbers = [random.randint(min_value, max_value) for _ in range(n)]
    return numbers

def main():
    """
    Demonstrate the usage of the generate_random_numbers function.
    """
    print(generate_random_numbers(10))

if __name__ == '__main__':
    main()
```