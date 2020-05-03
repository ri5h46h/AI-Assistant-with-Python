import os 
import pyttsx #pip install pyttsx , you can also install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import random
import smtplib
import pyaudio


print("Initialising AI Assistant")

engine = pyttsx.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
         speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am your AI desktop assistant version 1.2, designed in Python version 3.7.7. Tell me How May I Help You")

def takeCommand():
    #It takes mic input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    
    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()




        
if __name__ == "__main__":
    speak("Initializing AI Assistant")
    wishMe()
    while True:  #can place if 1: or 2: etc.
     
        query = takeCommand().lower()

        #logic for executing tasks based on query 

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak (results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.in")
        
        elif 'open google' in query:
            webbrowser.open("www.google.co.in")

        elif 'play music' in query:
            speak('Okay, playing music')
            print('Okay, playing music')
            music_dir = "T:\\awantika songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\uday_\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'email' in query:
            try:
                speak("What should I send in E-mail")
                content = takeCommand()
                to = "receiversemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")
                print("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send this E-mail at the moment, there might be a bug in my program")
                print("Sorry, I am unable to send this E-mail at the moment, there might be a bug in my program")

        elif 'quit' in query:
            exit()  # This will close your AI Assistant

        elif "name age" in query:
            speak("Your name is Rishabh Narayan and you are 16 years old")
