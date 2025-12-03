import datetime
import tkinter as tk
from tkinter import scrolledtext

# Chatbot reply logic
def chat_reply(user_text):
    text = user_text.lower()

    if "hello" in text or "hi" in text:
        return "Hello! 👋 How can I help you today?"

    elif "how are you" in text:
        return "I'm doing great! Thanks for asking 😊"
    elif "niraj" in text:
        return "bolo sedh ! ram ram"
    elif "your name" in text:
        return "I'm your Python Chatbot 🤖"

    elif "i love you" in text:
        return "Aww, that's sweet! But I'm just a bot 😳💗"

    elif "joke" in text:
        return "Why don't programmers like nature? Too many bugs! 🐛😂"

    elif "where do you live" in text:
        return "I live inside your computer 💻😄"

    elif "are you human" in text:
        return "No, I'm an AI bot but I understand humans 😉"

    elif "who are you" in text:
        return "I'm a simple chatbot built with Python!"

    elif "motivate me" in text:
        return "Believe in yourself! You can do anything 💪🔥"

    elif "study" in text:
        return "Focus for 1 hour. No distractions. Let's go! 📚"

    elif "life advice" in text:
        return "Stay consistent. Small steps create big results ✨"

    elif "python" in text:
        return "Python is awesome! Simple, powerful, fast to learn 😎"

    elif "help me code" in text:
        return "Sure! Tell me what you want to build 🧑‍💻"

    elif "dance" in text:
        return "I would dance, but I don't have legs 💃🤖"

    elif "sing" in text:
        return "La la la... 🎶 okay enough singing 😂"

    elif "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}"
    elif "day" in text:
        now = datetime.datetime.now().strftime("%A")
        return f"The current day is {now}"

    elif "date" in text:
        today = datetime.date.today().strftime("%d %B %Y")
        return f"Today's date is {today}"

    elif "bye" in text or "exit" in text:
        return "Goodbye! Take care 😊"

    else:
        return "Sorry, I didn’t understand that. Try again!"


# Function when Send button is clicked
def send_message():
    user_msg = entry_box.get()
    if user_msg.strip() == "":
        return

    chat_window.insert(tk.END, "\nYou: " + user_msg, "user")
    entry_box.delete(0, tk.END)

    bot_reply = chat_reply(user_msg)
    chat_window.insert(tk.END, "\nBot: " + bot_reply, "bot")

    chat_window.yview(tk.END)

    if user_msg == "exit":
        root.after(500, root.destroy)


# Setup GUI window
root = tk.Tk()
root.title("WhatsApp Chat Box (Python)")
root.geometry("420x550")
root.config(bg="#ECE5DD")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_window.tag_config("user", foreground="green")
chat_window.tag_config("bot", foreground="blue")

entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.pack(padx=10, pady=5, fill=tk.X)

entry_box.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send 📩", font=("Arial", 14),
                        bg="#25D366", fg="white", command=send_message)
send_button.pack(pady=5)

root.mainloop()
