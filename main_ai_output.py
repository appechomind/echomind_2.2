Here is the updated code:

```Python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def get_response_from_dict(input_text, responses):
    for key in responses:
        if key.lower() == input_text.lower():
            return responses[key]

def handle_user_input(user_input, responses):
    try:
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(user_input)
        
        if sentiment['compound'] > 0.5: 
            response = get_response_from_dict(user_input, responses)
            if response is None:
                return "I'm here to listen. What's been on your mind lately?"
            else:
                return response
        elif sentiment['compound'] < -0.5: 
            return "I'm sorry to hear that. Would you like to talk about it?"
        else:
            response = get_response_from_dict(user_input, responses)
            if response is None:
                return "That's okay! Sometimes we just need someone to listen."
            else:
                return response
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I didn't understand that."

def main():
    print('EchoMind Conversational AI')
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help.",
        "good": "That's great! What makes it good?",
        "bad": "I'm sorry to hear that. How can I help?"
    }
    
    while True:
        user_input = input("You: ")
        if not isinstance(user_input, str):
            print("Invalid input. Please enter a string.")
            continue
        response = handle_user_input(user_input, responses)
        print(f"EchoMind: {response}")

if __name__ == '__main__':
    main()
```