import speech_recognition as sr
import pyttsx3
import pywhatkit

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
                command = command.replace("Alexa", "")
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        

run_alexa()