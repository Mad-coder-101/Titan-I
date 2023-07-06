import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import googlesearch
import webbrowser
import LinksAndApps
import stop
import os
import time
import datetime
import keyboard
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
                    try:
                        words = words.replace('search wikipedia for', '')
                        result = wikipedia.summary(words,sentences = 2)
                        engine.say(result)
                    except wikipedia.exceptions.DisambiguationError:
                        engine.say('Please be more specific')                 
                elif 'search google for ' in words:
                    words = words.replace('search google for ', '')
                    base_url = "http://www.google.com/?q="
                    final_url = base_url + words.replace(' ','+')
                    webbrowser.open(final_url)
                    time.sleep(3)
                    keyboard.press_and_release('enter')
                elif 'open' in words:
                    words = words.replace(' open ','')
                    LinksAndApps.openLinkorApp(words)
                elif 'time' in words:
                    engine.say(time.strftime("%I:%M %p"))
                elif 'date' in words:
                    engine.say(datetime.date.today())
                stop.pause()
                engine.runAndWait()
                

        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error")