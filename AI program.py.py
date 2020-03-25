import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import microphone

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")   

    speak("I am bigs bee sir. Please tell me how may help you")
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.microphone as source:
        print("listening.....!")
        r.adjust_for_ambient_noise(source) #reduce noise
        audio = r.listen(source)
        print(r.recognize_google(audio)) #to print voice into text

    try:
        print("Recognizition....")
        query = sr.Recognize_google(audio, Language='en-in')
        print("User said: {}. format(query)")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"   
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtplib.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('s.utkarsharunbhardwaj@gmail.com', 'your-password')
    server.sendmail('s.utkarsharunbhardwaj@gmail.com', to, content)
    server.closed()

if __name__ == "__main__":
 wishMe()
   