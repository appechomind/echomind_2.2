Here is the updated code:

```
def respond_to_user_input(input_text):
    try:
        # Define some basic responses
        responses = {
            "hello": "Hello there! How are you feeling today?",
            "hi": "Hi! It's great to chat with you. What's on your mind?",
            "thanks": "You're welcome! I'm happy to help.",
            "sad": "I'm so sorry to hear that. Would you like to talk about what's going on?",
            "anxious": "I sense some anxiety there. Would you like me to offer some calming phrases?"
        }

        # Check if the input matches a response
        for key in responses:
            if key.lower() == input_text.lower():
                return responses[key]

        # If no match, provide a default response
        return "I'm here to listen. What's been on your mind lately?"

    except Exception as e:
        print(f"Error: {str(e)}")
        return "Sorry, I didn't understand that. Can you try again?"

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    while True:
        user_input = input("You: ")
        response = respond_to_user_input(user_input)
        print(f"EchoMind: {response}")
```

This updated code includes:

* A `try-except` block in the `respond_to_user_input` function to catch any exceptions and provide a default error message.
* Added some emotional support responses for "sad" and "anxious" inputs.
* The `if __name__ == '__main__':` block now runs an infinite loop, allowing users to continue chatting with EchoMind.
* This code aligns better with the EchoMind app vision by providing emotional support through conversational AI.