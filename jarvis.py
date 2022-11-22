from mimetypes import init
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5') # use to take the voice
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',  voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening") 

    speak("hi, I am Zira mam. Please, tell me how mai I help You?") 

def takeCommand():
    ''' it takes microphone input
    returns string output
    '''  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Listening...")
        query = r.recognize_google(audio, lang='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        # print(e)
        print("Say that again, Please...")
        return "None"
    return query

if __name__ == "__main__":
    # speak("Sushant is a gentleman")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

