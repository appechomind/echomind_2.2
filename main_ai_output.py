Here is the updated code:

```
def respond_to_user_input(input_text):
    # Convert input text to lowercase for case-insensitive matching
    input_text = input_text.lower()

    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help."
    }

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text:
            return responses[key]

    # If no match, provide a default response and ask follow-up questions
    return "I'm here to listen. What's been on your mind lately?"

def main():
    print('EchoMind Conversational AI')
    
    try:
        user_input = input("You: ")
        response = respond_to_user_input(user_input)
        print(f"EchoMind: {response}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```

This updated code includes:

* Case-insensitive matching for user input to improve the conversational AI capabilities.
* A `try-except` block in the `main()` function to handle potential errors and provide a more robust experience.
* The `respond_to_user_input` function has been extracted into its own separate function, which can be used as a starting point for improving the conversational flow by incorporating more advanced natural language processing techniques.