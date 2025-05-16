Here's an example of how you could improve the print statement:

```python
import colorful

def generate_report():
    try:
        with open("report.txt", "w") as report_file:
            report_file.write("This is a auto-generated report.")
    except IOError:
        print(f"{colorful.red('Error:')} Unable to create report file.")

print(f"{colorful.green('Auto-created main.py')}")
```

Note that this code includes error handling, proper formatting, and adds functionality by generating a report.