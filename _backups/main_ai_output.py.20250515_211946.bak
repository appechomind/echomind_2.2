Here is the updated code:

```
def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help.",
        "goodbye": "It was nice chatting with you. Take care!"
    }

    # Check if the input matches a response
    for key in responses:
        if key.casefold() == input_text.lower():
            return responses[key]

    # If no match, provide a default response
    return "I'm here to listen. What's been on your mind lately?"

def main():
    print('EchoMind Conversational AI')
    user_input = input("You: ")
    response = respond_to_user_input(user_input)
    print(f"EchoMind: {response}")

if __name__ == '__main__':
    main()
```

This code includes:

* A more comprehensive `respond_to_user_input` function that handles various responses and provides default responses for unknown inputs.
* The use of the `casefold()` method to make comparisons case-insensitive, making the code more robust against variations in user input (e.g., "Hello", "hello", or "hELLO").
* A separate `main` function to encapsulate the app's conversational AI capabilities and provide a clear entry point for the program.
* The use of f-strings for string formatting, which is a more modern and Pythonic way of formatting strings.