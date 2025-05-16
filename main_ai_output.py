Here's the updated code:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            logger.info(f"Read {filename} successfully: {data}")
            return data
    except FileNotFoundError:
        logger.error(f"{filename} not found")
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")

def main():
    filename = "example.txt"
    try:
        data = read_data(filename)
        print(f"The contents of {filename} are: {data}")
    except Exception as e:
        logging.error(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```

This code adds meaningful functionality by reading a file and printing its content. It also uses Python's built-in `logging` module to log messages, which can be useful for debugging and monitoring purposes. The code includes error handling using try-except blocks to catch potential errors.