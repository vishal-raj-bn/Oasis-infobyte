import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Listen for a voice command and return it as text."""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat, please?")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return None

def tell_time():
    """Tell the current time."""
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    speak(f"The time is {current_time}")

def tell_date():
    """Tell today's date."""
    today = datetime.date.today()
    speak(f"Today's date is {today.strftime('%B %d, %Y')}")

def search_web(query):
    """Search the web using the default browser."""
    speak(f"Searching the web for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def process_command(command):
    """Process the voice command."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "search" in command:
        query = command.replace("search", "").strip()
        search_web(query)
    else:
        speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    speak("How can I help you today?")
    while True:
        command = listen()
        if command:
            process_command(command)
        if command == "exit" or command == "quit":
            speak("Goodbye!")
            break
