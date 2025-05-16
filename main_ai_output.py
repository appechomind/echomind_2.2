Here is the updated code:

```python
#!/usr/bin/env python3
# data_processing.py - A simple script to process some sample data.

"""
This script processes some sample data. It can be used as a starting point for more complex data processing tasks.
"""

def calculate_sum(data):
    """
    Calculate the sum of the given data.

    Args:
        data (list): The list of numbers to sum up.

    Returns:
        int: The sum of the data.
    """
    return sum(data)

if __name__ == "__main__":
    print("Starting data processing...")
    
    # Sample data
    sample_data = [1, 2, 3, 4, 5]
    
    total = calculate_sum(sample_data)
    print(f"Sum of the data: {total}")
```

This updated code includes:

* A meaningful function `calculate_sum` that calculates the sum of a given list of numbers.
* An informative print statement in the main block to provide context about the processing task.
* Proper indentation and organization using comments and blank lines.
* A docstring at the top of the file to describe its purpose.
* A more descriptive name for the file, `data_processing.py`, that reflects its contents.

The updated code is organized into logical sections, including imports (none in this case), functions, and main logic. It also includes comments throughout to provide additional context and explanations.