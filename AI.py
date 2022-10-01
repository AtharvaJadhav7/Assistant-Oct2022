from ast import main
from datetime import datetime
import re
from threading import main_thread
from tkinter import mainloop
import webbrowser
import pyttsx3
import datetime
import speech_recognition as speech
import wikipedia
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning!")
        speak("How may I help you?")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
        speak("How may I help you?")

    elif hour>=17 and hour < 21:
        speak("Good Evening!")
        speak("How may I help you?")

    elif hour>=21 and hour <24:
        speak("Good Night!")
        speak("How may I help you?")

    elif hour>=0 and hour <2:
        speak("It's very late! you should sleep now.")

    
def takeCommand():
    s=speech.Recognizer()
    with speech.Microphone() as source:
        speak("Listening")
        print("Listening")
        s.pause_threshold=1.0
        s.energy_threshold=400
        audio = s.listen(source)

    try:
        print("Recognizing...")
        query = s.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        # print(e)

        print("Can you say that again....")
        return "None"
    return query

if __name__ == "__main__":
    speak("Hi! This is zira.")
    wishMe() 
    while True:
        query = takeCommand().lower()
        
        if 'shut down' in query:
            break
        
        if 'shutdown' in query:
            break

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to Wikipedia")
            print(results)
            speak(results)


        elif 'web' in query:
            query = query.replace("web","")
            webbrowser.open(query)

        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'time' in query:
            if 'what' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")



    