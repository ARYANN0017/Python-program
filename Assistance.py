import datetime   #for date and time
import webbrowser    # for youtube..
import pyttsx3   #text o Speech
import speech_recognition as sr    #microphone & text
import urllib.parse    #convert my world in google search link
import time   #delay(alaram)
import threading  #run alaram in bg
import songplaylist   #song file import

engine = pyttsx3.init()
engine.setProperty("rate", 180)    #speed 180 to talk
engine.setProperty("volume", 1.0)   # 1.0  volumn full

def speak(audio):   #this make assistant say anything
    engine.say(audio)
    engine.runAndWait()  #when you speeck hello  asssistant said hello
speak("hye i'm Your personal assistant")

def listen():
    r = sr.Recognizer()   #create an object in python library!
    with sr.Microphone() as source: #open microphone
        #with is not close itself that is my use file open and close itself
        print("Listening...")  #show msg terminal
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language="en-in")  # send my voice and convert to text
        print("You said:", query)
        return query.lower()
    except:
        return ""


def alaram(alaram_time):
    speak(f"Alarm set for {alaram_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alaram_time:
            speak(f"Wake up! yaar {current_time}")
            break
        time.sleep(1)

def set_reminder(reminder_time, reminder_msg):
    speak(f"Reminder set for {reminder_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        if current_time == reminder_time:
            print("🔔 REMINDER:", reminder_msg)
            speak(f"Reminder! {reminder_msg}")
            break
        time.sleep(20)

def run_in_background(func, *args):
    t = threading.Thread(target=func, args=args)
    t.daemon = True   # ensures thread closes when program ends
    t.start()


def set_notification(notification_msg):
    speak("Notification set for " + notification_msg)

    while True:
        current_time = datetime
while True:
    # command = input("you: ").lower()
    command = listen()

    if "wake up" in command:
        speak("I am awake now. How can I help you?")
    elif "hello" in command:
        speak("how can i help you")
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"time is {time}")
    elif "date" in command:
        date = datetime.datetime.now().strftime("%m/%d/%Y")
        speak(f"date is {date}")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "wikipedia" in command:
        speak("searching wikipedia...")

    elif "play" in command:
        song_name = command.replace("play", "").strip()

        if song_name in songplaylist.song:
            speak(f"Playing {song_name}")
            webbrowser.open(songplaylist.song[song_name])
        else:
            speak("Sorry, song not found in your playlist")



    elif "details" in command or "details of me" in command:
        speak("Searching your details on Google...")

        # Replace  NAME
        my_name = "Aryan Koradiya"

        query = urllib.parse.quote(my_name)   #converts your text into a URL-safe format  "" space % etc
        url = f"https://www.google.com/search?q={query}"

        webbrowser.open(url)
        speak("Here are the search results for your name.")

    elif "set alarm for" in command:
        try:
            # extract time example: "set alarm for 8:30"
            words = command.split("for")[-1].strip()         #split for last items baki nu remove
            alarm_time = datetime.datetime.strptime(words, "%H:%M").strftime("%H:%M")

            # Run alarm in background thread
            alarm_thread = threading.Thread(target=alaram, args=(alarm_time,))
            alarm_thread.start()

            print("your alarm time is ", alarm_time)

        except:
            speak("Please say a valid time like 8:30 or 18:20")

    elif "set reminder for" in command:
        try:
            words = command.split("for")[-1].strip()
            reminder_time = datetime.datetime.strptime(words, "%H:%M").strftime("%H:%M")
            speak(f"Reminder set for {reminder_time}")
        except:
            speak("Please say a valid time like 8:30 or 18:20")

    elif "bye" in command:
        speak("bye have A nice daY bYE byE!")
        break

    else:
        if "bye" in command:
            speak("bye have A nice daY bYE byE!")




