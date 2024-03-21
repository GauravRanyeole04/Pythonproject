import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests


print('Loading your AI personal assistant')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[1].id')


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print("Recognizing...")
            print(f"user said : {statement}\n")

        except Exception as e:
            speak("hey, please say that again")
            return "None"
        return statement


if __name__ == "__main__":

    wishMe()

    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if "bye" in statement or "ok bye" in statement or "ok stop here" in statement:
            speak('your personal assistant is shutting down,Good bye')
            print('your personal assistant is shutting down,Good bye')
            break



        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(10)

        elif 'open insta' in statement or 'instagram' in statement :
            webbrowser.open_new_tab("https://www.instagram.com")
            speak("instagram is open now")
            time.sleep(10)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(10)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(10)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"] != "404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'whats is the time' in statement or 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am G-one version 1 point O your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by harshal daud ganesh tirsule and gaurav ranyeole")
            print("I was built by harshal daud, ganesh tirsule and gaurav ranyeole")

        elif "open stackoverflow" in statement or "stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(10)

        elif 'open newspaper' in statement:
            news = webbrowser.open_new_tab("https://indianexpress.com")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(10)

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(10)

        elif 'ask' in statement or 'give answer' in statement or 'question' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "play a song" in statement or "song" in statement:
            speak("which song do you want to listen")
            p = sr.Recognizer()
            with sr.Microphone() as source:
                p.pause_threshold =1
                audio = p.listen(source)
            song = p.recognize_google(audio, language='en-in')
            print(f"you are said : {song}\n")
            webbrowser.open_new_tab(song)
            speak("This is special for you")
            time.sleep(15)

time.sleep(3)











