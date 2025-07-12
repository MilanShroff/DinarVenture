import random
import datetime

print("DV06AI00020")

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello!! How can I help you today!?"

    elif "how are you?" in user_input:
        return "I am doing very well!"

    elif "what are you?" in user_input:
        return "I am a rule-based chatbot!! My name is ChatBuddy!!"

    elif "time" in user_input:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."

    elif "weather" in user_input:
        return "I'm not connected to the internet, but let's pretend that it's always sunny in here!"

    elif "joke" in user_input:
        jokes = [
            "Why did the computer show up at work late? It had a hard drive!",
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the chatbot cross the road? To get to the other side of the query!"
        ]
        return random.choice(jokes)
    else:
        return "I'm sorry!! I am unable to help!!"

print("ChatBuddy: Hi! I'm ChatBuddy. Type 'bye' to exit.")

while True:
    user_text = input("You: ")
    response = chatbot_response(user_text)
    print("ChatBuddy:", response)

    if "bye" in user_text.lower() or "goodbye" in user_text.lower():
        break
