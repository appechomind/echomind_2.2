Here's the updated code:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Auto-generated file %s', __file__)
```

This code now uses Python's built-in `logging` module instead of `print`, which provides more control over log levels and formatting. The logger is configured to log messages at the INFO level, and it logs a message with the auto-generated file name and path.