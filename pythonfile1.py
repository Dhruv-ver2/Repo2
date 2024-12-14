import pyttsx3 as py
engine=py.init("sapi5")
voices=engine.getProperty("voices")

engine.setProperty("voice",voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello boss,how are you")    
