Here is the updated code:

```
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
    if input_text.isalpha():  # added validation to ensure user input is a valid string
        return "I'm here to listen. What's been on your mind lately?"
    else:
        print("Error: I didn't understand that. Can you rephrase your question?")  # added error handling

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    while True:
        try:
            user_input = input("You: ")
            response = respond_to_user_input(user_input)
            print(f"EchoMind: {response}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
```

This updated code includes:

* Added validation to ensure that the user input is a valid string using the `isalpha()` method.
* Added error handling by printing an error message and asking the user to rephrase their question if no match is found in the `responses` dictionary.
* Wrapped the main loop in a `try-except` block to catch the `KeyboardInterrupt` exception and allow the user to exit the program using Ctrl+C.