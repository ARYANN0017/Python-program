import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # 0 = male, 1 = female
engine.setProperty("fast", 1.0 ) #slow and fast
engine.setProperty("volume",1.0) #max volume
msg= input("Enter your message: ")
engine.say(msg)
engine.runAndWait()

