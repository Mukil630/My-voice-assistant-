import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Text-to-Speech Engine Init
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            # timeout=5 (wait 5 sec max), phrase_time_limit=5 (max duration)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("I didn't hear anything.")
            return ""
    try:
        # Better recognition for Indian accent (or change to 'ta-IN' for Tamil)
        command = r.recognize_google(audio, language='en-IN')
        print(f"You said: {command}")
    except:
        speak("Sorry, I didn't catch that.")
        return ""
    return command.lower()

def run_assistant():
    greet()
    while True:
        command = take_command()

        if 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")

        elif 'your name' in command:
            speak("I’m your assistant. You can name me if you want.")

        elif 'stop' in command or 'exit' in command:
            speak("Goodbye maplaa!")
            break

        elif command:
            speak("Sorry, I’m still learning. Try something else.")

# Run the assistant
run_assistant()
