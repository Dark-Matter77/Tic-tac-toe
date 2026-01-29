import speech_recognition as sr
import webbrowser
import pyttsx3
import music_Library
import requests
from gtts import gTTS
import pygame
import os
import pyjokes as pj






recognizer = sr.Recognizer()
engine = pyttsx3.init()
news_api = "sk_28c5d3b30317dda80a4731021bee4d296461f4751358142f"
# Set your ElevenLabs API key as an environment variable named ELEVEN_API_KEY before running this script.
# For example, in PowerShell: $env:ELEVEN_API_KEY = "your_api_key_here"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
 

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("http://instagram.com")
    elif "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif "joke" in c.lower():
        joke = pj.get_joke()
        speak(joke)
    elif c.lower().startswith("play"):
        song = c.lower().split(" ", 1)[1] if len(c.lower().split(" ")) > 1 else ""
        link = music_Library.get_song_link(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn't find the song '{song}'.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])

    else:
        # Let openAI handle the request
        pass


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()


        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Ya")
                # listen for command 
                with sr.Microphone() as source:
                    print("Javris Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
