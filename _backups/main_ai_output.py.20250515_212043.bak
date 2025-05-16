Here is the updated code:

```
def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help.",
        "how are you": "I'm just a bot, but I'm feeling pretty good! Thanks for asking.",
        "what's up": "Not much, just waiting for someone to talk to. How about you?"
    }

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text.lower():
            return responses[key]

    # If no match, provide a default response with some emotional support
    return "I'm here to listen. What's been on your mind lately? Don't worry, everything will be okay."

    # Consider using natural language processing (NLP) libraries like NLTK or spaCy to improve the chatbot's understanding of user input

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    try:
        user_input = str(input("You: "))
        response = respond_to_user_input(user_input)
        print(f"EchoMind: {response}")
    except Exception as e:
        print(f"Error: {e}")

```

This updated code includes:

* A `respond_to_user_input` function that accepts a string as input and returns a meaningful response.
* A dictionary of basic responses to common phrases like "hello", "hi", and "thanks".
* An `if __name__ == '__main__':` block that demonstrates the app's conversational AI capabilities by accepting user input, processing it through the `respond_to_user_input` function, and printing a response.
* Error handling using try-except blocks to handle unexpected input types or errors that might occur during processing.