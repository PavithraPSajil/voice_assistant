import pyttsx3
import datetime
import webbrowser
import os
import random

# Initialize voice engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Welcome message
speak("Hello! I am your smart assistant.")

# Joke list
jokes = [
    "Why do programmers hate nature? Too many bugs.",
    "Why was the computer cold? It forgot to close windows.",
    "Why did Python go to school? To improve its class."
]

# Main loop
while True:

    command = input("You: ").lower()

    # Greetings
    if "hello" in command or "hi" in command:
        speak("Hello! How are you?")

    # Fine response
    elif "fine" in command or "good" in command:
        speak("That's great!")

    # Assistant name
    elif "your name" in command:
        speak("I am your Python smart assistant.")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    # Date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}")

    # How are you
    elif "how are you" in command:
        speak("I am doing great!")

    # Open YouTube
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    # Open Google
    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    # Open ChatGPT
    elif "open chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")

    # Search Google
    elif "search" in command:

        query = command.replace("search", "")

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        speak(f"Searching for {query}")

    # Open Notepad
    elif "open notepad" in command:
        os.startfile("notepad.exe")
        speak("Opening Notepad")

    # Open Calculator
    elif "open calculator" in command:
        os.system("calc")
        speak("Opening Calculator")

    # Tell joke
    elif "joke" in command:
        speak(random.choice(jokes))

    # Play music
    elif "play music" in command:
        music = "C:\\Users\\Public\\Music"
        os.startfile(music)
        speak("Opening Music Folder")

    # Shutdown computer
    elif "shutdown" in command:
        speak("Shutting down computer")
        os.system("shutdown /s /t 5")

    # Restart computer
    elif "restart" in command:
        speak("Restarting computer")
        os.system("shutdown /r /t 5")

    # Exit assistant
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        break

    # Unknown commands
    else:
        speak("Sorry, I don't understand that yet.")