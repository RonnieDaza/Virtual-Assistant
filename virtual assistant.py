import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("voice", voices[1].id)
voices = engine.getProperty("voices")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                talk(command)
    except:
        pass
    return command
