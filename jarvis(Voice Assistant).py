import pyttsx3
import speech_recognition as sr 
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import random

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good AFternoon!")
    else:
        speak("Good evening!")

    speak("I am Jarvis Aryan Sir , How may I help you today")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recongining....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"

    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("Acoording to Wikipedia")
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening google")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Opening stackoverflow")

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is{strtime}")

        elif 'stop' in query:
            break
        
        elif 'visual studio code' in query:
            codepath="C:\\Users\\Aryan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak('opening VS code')

        elif 'play music' in query:
            music_dir="K:\\YOUFACE\\MUSIC"
            songs =os.listdir(music_dir)
            x=random.randint(0,21)
            os.startfile(os.path.join(music_dir, songs[x]))