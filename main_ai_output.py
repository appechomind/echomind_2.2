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
    return "I'm here to listen. What's been on your mind lately?"

def process_user_input():
    user_input = input("You: ")
    try:
        user_input_string = str(user_input)
        response = respond_to_user_input(user_input_string)
        print(f"EchoMind: {response}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    while True:
        process_user_input()
```

This updated code includes:

* A separate `process_user_input` function that handles user input, error handling and prints the response.
* Error handling to catch any unexpected inputs or exceptions.
* An infinite loop to continue processing user input until the program is stopped.
* Renamed `input_text` to `user_input_string` for better clarity.
* Removed redundant parentheses in some places.