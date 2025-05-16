Here is the updated code:

```
def generate_random_numbers(n):
    import random
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers

numbers = generate_random_numbers(10)
print(numbers)

if __name__ == '__main__':
    print('Auto-created main.py')
```