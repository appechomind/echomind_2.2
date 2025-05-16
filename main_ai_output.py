Here's an updated version of your code that incorporates some of the suggestions:

```Python
# Auto-generated script to generate random numbers and visualize them
import random
import matplotlib.pyplot as plt

def generate_random_numbers(amount):
    return [random.randint(0, 100) for _ in range(amount)]

def visualize_random_numbers(numbers):
    plt.hist(numbers, bins=20)
    plt.xlabel('Random Number')
    plt.ylabel('Frequency')
    plt.title('Distribution of Random Numbers')
    plt.show()

def main():
    print('Welcome to the Auto-generated Script!')
    amount = int(input('How many random numbers would you like to generate? '))
    
    try:
        if amount > 0:
            numbers = generate_random_numbers(amount)
            visualize_random_numbers(numbers)
        else:
            print('You must enter a positive integer.')
            
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        
if __name__ == '__main__':
    main()
```

This code:

1. Asks for user input to generate random numbers.
2. Uses matplotlib to visualize the generated numbers in a histogram.
3. Adds error handling using try-except blocks.

Note that I've used some basic Python concepts like functions, conditional statements, and exception handling.