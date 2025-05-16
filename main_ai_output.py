Here is the updated code:

```Python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_average_grade(grades):
    """
    Calculate the average grade from a list of grades.
    
    Args:
        grades (list): A list of integers representing student grades.
        
    Returns:
        float: The average grade.
    """
    return sum(grades) / len(grades)

def main():
    grades = [85, 92, 78, 95, 88]
    average_grade = calculate_average_grade(grades)
    
    logger.info(f"Average grade: {average_grade:.2f}%")

if __name__ == "__main__":
    main()
```

In this updated code:

1. **Make it useful**: I added a practical task (calculating the average grade) that demonstrates a specific problem-solving technique.
2. **Improve maintainability**: I followed PEP 8 guidelines for naming conventions, comments, and docstrings to enhance code readability.
3. **Consider using logging instead of printing**: I used Python's built-in logging module (`logging`) to log messages with a higher level of control and customization.
4. **Add meaningful content**: The script now calculates the average grade from a list of grades, making it more meaningful and useful.

Feel free to modify or extend this code further!