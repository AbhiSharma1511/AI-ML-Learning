import pyttsx3

#  set engine properties for voice and rate
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} ({voice.languages})")
engine.setProperty('voice', voices[1].id)



def speak(text):
    engine.say(text)
    engine.runAndWait()


while True:
    engine.say("Hello, how can I assist you today?")


speak()