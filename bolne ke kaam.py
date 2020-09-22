import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
a = str(input("Enter the words or things that you want the system to speak:\n"))
speak(a)