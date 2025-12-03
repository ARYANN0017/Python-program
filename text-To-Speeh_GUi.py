import tkinter as tk
import pyttsx3

root = tk.Tk()
root.title("text to speech GUi")
root.geometry("400x400")

engine = pyttsx3.init()

def speak_text():
    text = text_box.get("1.0", tk.END)   # Get all text    string position1-> 1 line number 2-> o charactor num
    engine.say(text)
    engine.runAndWait()

# Function to Clear Text
def clear_text():
    text_box.delete("1.0", tk.END)

text_box = tk.Text(root, font=("Arial", 14), height=8, width=40)
text_box.pack(pady=20)

# Speak Button
speak_btn = tk.Button(root, text="Speak", font=("Arial", 14), bg="#90ee90", command=speak_text)
speak_btn.pack(pady=5)

# Clear Button
clear_btn = tk.Button(root, text="Clear", font=("Arial", 14), bg="#ff7f7f", command=clear_text)
clear_btn.pack(pady=5)

root.mainloop()
