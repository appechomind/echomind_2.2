Here's the updated code:

```
import random

class EchoMind:
    def __init__(self):
        self.emotions = {
            'happy': "I'm thrilled you're feeling happy!",
            'sad': "Sorry to hear that. Would you like to talk about it?",
            'angry': "Whoa, I sense some frustration! Can we find a way to address it?"
        }

    def respond_to_user_input(self, input_text):
        if any(emotion in input_text.lower() for emotion in self.emotions.keys()):
            return random.choice([self.emotions[emotion] for emotion in self.emotions.keys()])
        elif 'help' in input_text.lower():
            return "I'm here to help! What do you need assistance with?"
        else:
            return "I'm here to listen. What's been on your mind lately?"

    def process_user_input(self):
        user_input = input("You: ")
        try:
            response = self.respond_to_user_input(user_input)
            print(f"EchoMind: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    echo_mind = EchoMind()
    print('EchoMind Conversational AI')
    while True:
        echo_mind.process_user_input()