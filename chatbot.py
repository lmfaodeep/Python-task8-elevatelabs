print("🤖 Hello! I am ChatBot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["hi", "hello"]:
        print("ChatBot: Hello! How can I help you today?")
    elif "your name" in user_input:
        print("ChatBot: I'm a simple rule-based chatbot built using Python.")
    elif "how are you" in user_input:
        print("ChatBot: I'm just code, but I'm running perfectly! 😊")
    elif "bye" in user_input:
        print("ChatBot: Goodbye! Have a great day.")
        break
    elif "thanks" in user_input or "thank you" in user_input:
        print("ChatBot: You're welcome!")
    else:
        print("ChatBot: I'm not sure how to respond to that. Try asking something else.")
