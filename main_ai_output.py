Here is the updated code:

```Python
# Import necessary modules
import logging

# Set up logging to capture errors
logging.basicConfig(level=logging.INFO)

def main():
    """
    This script demonstrates a simple greeting.
    """
    try:
        # Print a friendly message
        print('Hello, World!')

    except Exception as e:
        # Log any unexpected errors
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

I've addressed each of the goals:

1. **Create a meaningful purpose**: The script now has a clear intention - to print a friendly greeting.
2. **Improve code quality**: I followed PEP 8 guidelines, added blank lines between top-level statements, and used consistent spacing throughout the code. 
3. **Make it reusable**: The script is modularized into logical sections (importing necessary modules, setting up logging, defining the main logic), which makes it easier to integrate into larger projects or reuse in other contexts.
4. **Error handling**: I added a try-except block to capture and report any unexpected errors that might occur during execution.
5. **Code organization**: The script now has clear sections for imports, setup, and main logic.

Let me know if you'd like any further modifications!