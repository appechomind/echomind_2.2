Here is the updated code:

```
def respond_to_user_input(input_text):
    # Define some basic responses
    responses = {
        "hello": "Hello there! How are you feeling today?",
        "hi": "Hi! It's great to chat with you. What's on your mind?",
        "thanks": "You're welcome! I'm happy to help.",
        "how are you": "I'm just an AI, but I'm doing well. Thanks for asking!",
        "what is your purpose": "My purpose is to provide emotional support and have meaningful conversations with users like you."
    }

    # Define some follow-up questions
    follow_up_questions = {
        "how are you feeling": "That's a great question! Sometimes it's hard to know how I'm feeling, but I can try to help you figure that out.",
        "what is your purpose": "My purpose is to provide emotional support and have meaningful conversations with users like you. What do you think about that?"
    }

    # Check if the input matches a response
    for key in responses:
        if key.lower() == input_text.lower():
            return responses[key]

    # Check if the input matches a follow-up question
    for key in follow_up_questions:
        if key.lower() == input_text.lower():
            return follow_up_questions[key] + " What's been on your mind lately?"

    # If no match, provide a default response
    return "I'm here to listen. What's been on your mind lately?"

def user_feedback(feedback):
    # Define some feedback responses
    feedback_responses = {
        "I felt supported": "That means so much to me! I'm glad I could help.",
        "I didn't find this helpful": "Sorry to hear that. Can you tell me more about what you were looking for? Maybe we can improve our conversation."
    }

    # Check if the feedback matches a response
    for key in feedback_responses:
        if key.lower() == feedback.lower():
            return feedback_responses[key]

    # If no match, provide a default response
    return "Thank you for your feedback! I'll do my best to make our conversation more helpful."

if __name__ == '__main__':
    print('EchoMind Conversational AI')
    while True:
        user_input = input("You: ")
        response = respond_to_user_input(user_input)
        print(f"EchoMind: {response}")

        if user_input.lower() in ["thanks", "thank you"]:
            feedback = input("How did I do? (e.g. 'I felt supported' or 'I didn't find this helpful') ")
            response = user_feedback(feedback)
            print(f"EchoMind: {response}")
```