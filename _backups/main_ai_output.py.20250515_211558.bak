Here is the updated code:

```
def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help."
    }

    # Add error handling for unexpected inputs
    try:
        input_text = input_text.lower()
    except AttributeError:
        log("Unexpected input type")
        return "I didn't understand that. Can you rephrase?"

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text:
            return responses[key]

    # If no match, provide a default response
    return "I'm here to listen. What's been on your mind lately?"

def main():
    print('EchoMind Conversational AI')
    user_input = input("You: ")
    while user_input:
        response = respond_to_user_input(user_input)
        print(f"EchoMind: {response}")
        user_input = input("You: ")

if __name__ == '__main__':
    main()
```

This updated code includes:

* Error handling for unexpected inputs by catching `AttributeError` and providing a default response.
* Input validation to ensure that the user input is not empty or null before processing it.
* A `main` function that demonstrates the app's conversational AI capabilities by accepting user input, processing it through the `respond_to_user_input` function, and printing a response. The conversation continues until the user stops entering input.

This updated code aligns better with the EchoMind app vision by providing emotional support through conversational AI.