Here is the updated code:

```python
"""
Main entry point for the application.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Print a message on startup."""
    logger.info('Auto-created main.py')

if __name__ == '__main__':
    main()
```

Changes made:
- Added a docstring to provide context about the file's purpose.
- Imported and configured Python's built-in `logging` module instead of using `print`.
- Defined a `main` function that prints the message on startup, following PEP 8 naming conventions.
- Used an `if __name__ == '__main__':` block to ensure that the `main` function is only executed when this file is run directly (i.e., not when it's imported as a module by another script).