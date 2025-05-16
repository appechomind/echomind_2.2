Here is the updated code based on the goals:

```
import random
from textblob import TextBlob

def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": ["Hello there! How are you feeling today?", "Hi! It's great to chat with you. What's on your mind?"],
        "hi": ["Hi! It's great to chat with you. What's on your mind?", "Hey! I'm here to listen. What's been on your mind lately?"],
        "thanks": ["You're welcome! I'm happy to help.", "No problem at all! I'm always here to lend a listening ear."],
    }

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text.lower():
            return random.choice(responses[key])

    # If no match, provide a default response
    blob = TextBlob(input_text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.5:
        return "I'm so glad to hear that! I'm here for you whenever you need someone to talk to."
    elif sentiment < -0.5:
        return "I'm sorry to hear that. Remember, you're not alone and there's always hope for a better tomorrow."
    else:
        return "I'm here to listen. What's been on your mind lately?"

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    while True:
        user_input = input("You: ")
        response = respond_to_user_input(user_input)
        print(f"EchoMind: {response}")
```

This updated code includes:

* A `respond_to_user_input` function that accepts a string as input and returns a meaningful response based on the user's sentiment.
* A dictionary of basic responses to common phrases like "hello", "hi", and "thanks".
* An `if __name__ == '__main__':` block that demonstrates the app's conversational AI capabilities by accepting user input, processing it through the `respond_to_user_input` function, and printing a response.
* The code uses natural language processing (NLP) to analyze the sentiment of the user's input and respond accordingly.