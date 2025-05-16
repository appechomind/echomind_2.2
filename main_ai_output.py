Here is the improved code:

```python
import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info('Auto-generated main.py script started')

    try:
        user_input = input("Enter your name: ")
        print(f"Hello, {user_input}!")
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    main()
```

I added basic error handling using a try-except block and used the `logging` module to log information at different levels. I also kept the original message about the script being auto-generated, but moved it inside the logging call for better readability and separation of concerns.