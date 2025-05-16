Here is the updated code:

```
import re
import random
from nltk.sentiment import SentimentIntensityAnalyzer

def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": ["Hello there! How are you feeling today?", "Hi! It's great to chat with you. What's on your mind?"],
        "hi": ["Hi! It's great to chat with you. What's on your mind?", "Hey! I'm here to listen. What's been on your mind lately?"],
        "thanks": ["You're welcome! I'm happy to help.", "No problem at all. That's what friends are for."]
    }

    # Define some advanced responses
    advanced_responses = {
        r"how are you": ["I'm just an AI, but I'm doing well, thanks! How about you?", "I'm feeling quite chatty today, thanks for asking!"],
        r"what's new": ["Not much, just hanging out. What about you?", "Just the usual - learning and improving my conversational skills."],
    }

    # Check if the input matches a response
    for key in responses:
        if re.match(key.lower(), input_text.lower()):
            return random.choice(responses[key])

    # Check if the input matches an advanced response
    for pattern, responses_list in advanced_responses.items():
        if re.match(pattern, input_text):
            return random.choice(responses_list)

    # If no match, provide a default response
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(input_text)
    if sentiment['compound'] > 0:
        return "I'm here to listen. What's been on your mind lately?"
    elif sentiment['compound'] < 0:
        return "Sorry to hear that. Is there anything I can do to help?"
    else:
        return "I'm here to chat. What's on your mind?"

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    user_input = input("You: ")
    response = respond_to_user_input(user_input)
    print(f"EchoMind: {response}")
```