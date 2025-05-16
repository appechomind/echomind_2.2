Here is the updated code:

```
def generate_random_numbers(n: int) -> list:
    """Generate a list of random numbers with a specified length."""
    import random
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input 'n' must be a positive integer.")

    return [random.randint(1, 100) for _ in range(n)]


if __name__ == '__main__':
    numbers = generate_random_numbers(10)
    print(numbers)
```