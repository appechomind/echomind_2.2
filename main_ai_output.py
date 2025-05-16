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

def main():
    print('EchoMind Conversational AI')
    user_input = input("You: ").strip().lower()
    response = respond_to_user_input(user_input)
    print(f"EchoMind: {response}")

if __name__ == '__main__':
    main()

```

Note that I added the `strip()` method to remove any whitespace from the user's input, and also converted the input text to lowercase to ensure case-insensitive matching with the responses dictionary keys.