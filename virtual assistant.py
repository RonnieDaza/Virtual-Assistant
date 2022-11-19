import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)
    elif "Who is" in command:
        person = command.replace("Who is", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif "Date" in command:
        talk("Sorry, I have a headache.")
    elif "Are you single?" in command:
        talk("I am in a relationship.")
    elif "Joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("Please say the command again.")

while True:
    run_alexa()