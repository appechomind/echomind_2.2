Here is the updated code:

```
def generate_random_numbers(n: int) -> list[int]:
    """
    Generates a list of n random integers between 1 and 100.
    
    Args:
        n (int): The number of random numbers to generate
    
    Returns:
        A list of random integers
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    import random
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers

numbers = generate_random_numbers(10)
print(numbers)

if __name__ == '__main__':
    print('Auto-created main.py')
```