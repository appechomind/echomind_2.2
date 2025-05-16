Here is the updated code:

```Python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    filename='app.log', 
                    filemode='a')

def print_message():
    message = 'Auto-created main.py'
    try:
        logging.info(message)
    except Exception as e:
        logging.error(f"Error: {str(e)}")

if __name__ == "__main__":
    print_message()
```

In this updated code, I have added error handling using a try-except block and used Python's built-in `logging` module to log messages. The logging level is set to INFO, but you can adjust it according to your needs.