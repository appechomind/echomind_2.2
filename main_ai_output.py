Here's the updated code:
```python
def temperature_converter(celsius):
    """
    Converts Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        if celsius < -273.15:  # Kelvin scale starts at absolute zero
            print("Error: Temperature cannot be below absolute zero.")
        else:
            fahrenheit = temperature_converter(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
```
I've added the following improvements:

1. **Reusable function**: Extracted the temperature conversion calculation into a separate `temperature_converter` function.
2. **Error handling and edge cases**: Added error handling to deal with unexpected inputs (e.g., non-numeric input) or exceptions (e.g., negative temperatures below absolute zero).
3. **Readability and formatting**: Improved indentation, spacing, and commenting to make the code easier to read.

Note that I've also renamed the script to `temperature_converter.py` as suggested, but you can rename it to whatever makes sense for your project.