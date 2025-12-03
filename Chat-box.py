import random #just for random choice replies use--

def chat_reply(text_user):
    text = text_user.lower()

    if "hello" in text or "hi" in text:
        replies=[
            "How are you?",
            "yes! how can i help you Today!?",
            "hye what are you doing?"
        ]
        return random.choice(replies)
    elif "how are you?" in text:
        return "I'm fine, thank you!"
    elif "how are you doing" in text:
        return "I'm fine, thank you!"
    elif "what is your name" in text:
        return "mY name is AK"
    else:
        return "sorry, I don't understand you"

print("chat Bot is Redy  ! type exit to exit")

while True:
    user= input("You:")

    if user == "exit":
        break

    replay = chat_reply(user)
    print("Bot:",replay)