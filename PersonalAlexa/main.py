import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes
import datetime
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()

# Adjusting voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
    except Exception as e:
        print(e)
        return "error"
    return command.lower()


def run_alexa():
    talk('Hello! I am your virtual assistant. How can I help you today?')

    while True:
        command = take_command()
        print(command)

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            try:
                info = wikipedia.summary(person, sentences=1)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk(f"Multiple results found. Please specify: {e.options[:3]}")
            except wikipedia.exceptions.PageError:
                talk(f"Sorry, I couldn't find any information on {person}.")
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime('%B %d, %Y')
            talk(f'Today is {current_date}')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'goodbye' in command or 'stop' in command:
            talk('Goodbye! It was a pleasure assisting you.')
            break
        else:
            talk('Please say the command again.')


if __name__ == "__main__":
    run_alexa()
