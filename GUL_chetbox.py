import tkinter as tk
from tkinter import scrolledtext

# Chatbot logic
def chatbot_reply(user_text):
    text = user_text.lower()

    if "hello" in text:
        return "Hi! How can I help you today?"
    elif "how are you" in text:
        return "I'm good! What about you?"
    elif "your name" in text:
        return "I'm a Python Chatbot 😊"
    else:
        return "I didn't understand that. Try again!"

# When Send button is clicked
def send_message():
    user_input = entry_box.get()
    chat_window.insert(tk.END, "You: " + user_input + "\n")
    entry_box.delete(0, tk.END)

    reply = chatbot_reply(user_input)
    chat_window.insert(tk.END, "Bot: " + reply + "\n\n")

# Main window
root = tk.Tk()
root.title("Chat Box (Python)")
root.geometry("400x500")

# Chat area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry box
entry_box = tk.Entry(root, font=("Arial", 14))
entry_box.pack(padx=10, pady=5, fill=tk.X)

# Send button
send_btn = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_btn.pack(pady=5)

root.mainloop()
