import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import openai

# 💡 Add your OpenAI API key here
openai.api_key = ""
# 🔊 Text-to-Speech Engine Init
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
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
    try:
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was an error with the speech service.")
        return ""

def ask_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("Error from GPT:", e)
        return "Sorry, I couldn't get a response from GPT."

def run_assistant():
    greet()
    while True:
        command = take_command()
        if not command:
            continue
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The time is {time}")
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
        elif 'stop' in command or 'exit' in command:
            speak("Goodbye!")
            break
        elif command:
            # 🌟 Fallback: Use GPT to respond
            response = ask_gpt(command)
            print("GPT:", response)
            speak(response)

# ▶️ Run it!
if __name__ == "__main__":
    run_assistant()
