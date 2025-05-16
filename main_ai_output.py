Here is the updated code:
```
import logging
import os

logging.basicConfig(level=logging.INFO)

def main():
    print(f"Auto-created {os.path.basename(__file__)} - a Python script for machine learning and data analysis")

if __name__ == "__main__":
    main()
```