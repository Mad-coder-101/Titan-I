import speech_recognition as sr
import pyttsx3
import wikipedia
import googlesearch
import webbrowser
import LinksAndApps
import os
import time
import datetime
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',175)
recognizer.dynamic_energy_threshold = False
recognizer.dynamic_energy_threshold = .5
if __name__ == '__main__':
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source,timeout=None)
        try:
            global words
            words = recognizer.recognize_google(audio).lower()
            if 'quit' in words:
                engine.stop()
                break
            if 'titan' in words:
                words = words.replace('titan','')
                if 'wikipedia' in words:
                    words = words.replace('search wikipedia for', '')
                    result = wikipedia.search(words,sentences = 5)
                    engine.say(result)                 
                elif 'search google for ' in words:
                    words = words.replace(' search google for ', '')
                    webbrowser.open_new_tab(f"https://www.google.com / search?&q ={words}")
                elif 'open' in words:
                    words = words.replace(' open ','')
                    LinksAndApps.openLinkorApp(words)
                elif 'time' in words:
                    engine.say(time.strftime("%I:%M %p"))
                elif 'date' in words:
                    engine.say(datetime.date.today())
                engine.runAndWait()
            else:
                continue

        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error")