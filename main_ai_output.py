Here is the updated code:

```
# main.py
import logging

def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help."
    }

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text.lower():
            return responses[key]

    # If no match, provide a default response
    return "I'm here to listen. What's been on your mind lately?"

def handle_user_input(input_text):
    try:
        response = respond_to_user_input(input_text)
        print(f"EchoMind: {response}")
    except Exception as e:
        logging.error("Error handling user input:", e)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    print('EchoMind Conversational AI')
    
    while True:
        try:
            user_input = input("You: ")
            handle_user_input(user_input)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
```

This updated code includes:

* A `handle_user_input` function that accepts a string as input, processes it through the `respond_to_user_input` function, and handles any errors that might occur during execution.
* A logging mechanism to log any error messages that occur during the app's execution.
* A main loop that continues to accept user input until the user decides to exit by pressing Ctrl+C.

This updated code aligns better with the EchoMind app vision by providing a more robust and user-friendly conversational AI experience.