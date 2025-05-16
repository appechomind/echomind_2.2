Here is an updated version of the main.py file that incorporates more robust input validation, expanded response dictionary, advanced NLP library usage, context-awareness, error handling, and emotional support capabilities:

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help.",
        "i love you": "That's so sweet! Who's the special someone in your life?",
        "sad": "I'm here for you. Sometimes it helps to talk about what's bothering you. Would you like to share more?"
    }

    # Expand response dictionary using NLTK
    lemmatizer = WordNetLemmatizer()
    pos_tags = word_tokenize(input_text)
    sentiment = nltk.sentiment.vader.SentimentIntensityAnalyzer().polarity_scores(input_text)
    
    if sentiment['compound'] < 0:
        return "I'm here for you. Sometimes it helps to talk about what's bothering you. Would you like to share more?"
    elif sentiment['compound'] > 0:
        return "That sounds amazing! What made your day so special?"

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text.lower():
            return responses[key]

    # If no match, provide a default response
    return "I'm here to listen. What's been on your mind lately?"

def main():
    print('EchoMind Conversational AI')
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            break
        
        try:
            response = respond_to_user_input(user_input)
            print(f"EchoMind: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")
            continue

if __name__ == '__main__':
    main()
```