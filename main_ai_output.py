Here is the updated code:

```
import datetime

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Auto-generated {__file__} file, created at {now}")

if __name__ == "__main__":
    main()
```

This code is more meaningful and includes a timestamp when the script was generated.