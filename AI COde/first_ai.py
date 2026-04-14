import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't catch that")
        return ""

def open_apps(command):
    if "chrome" in command:
        speak("Opening Chrome")
        os.system("C:\\Users\\Public\\Desktop\\Google Chrome.lnk")

    elif "code" in command:
        speak("Opening VS Code")
        os.system("code")

def tell_time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time}")

def tell_date():
    date = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today is {date}")

while True:
    command = listen()

    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "time" in command:
        tell_time()

    elif "date" in command:
        tell_date()

    elif "open" in command:
        open_apps(command)

    elif "stop" in command or "exit" in command:
        speak("Goodbye boss!")
        break