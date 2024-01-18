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
import recognize
import threading
from speak import speakStop
recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('rate',175)
recognizer.dynamic_energy_threshold = False
recognizer.dynamic_energy_threshold = .5
if __name__ == '__main__':
    while True:
        try:
            words = recognize.command()
            if 'quit' in words:
                engine.stop()
                break
            if 'titan' in words:
                words = words.replace('titan','')
                if 'wikipedia' in words:
                    try:
                        words = words.replace('search wikipedia for', '')
                        result = wikipedia.summary(words,sentences = 2)
                        speakStop(result)
                    except wikipedia.exceptions.DisambiguationError:
                        speakStop('Please be more specific')
                    except wikipedia.exceptions.PageError:
                        speakStop('The subject asked for is not in Wikipedia')                 
                elif 'search google for ' in words:
                    words = words.replace('search google for ', '')
                    base_url = "http://www.google.com/?q="
                    final_url = base_url + words.replace(' ','+')
                    webbrowser.open(final_url)
                    time.sleep(3)
                    speakStop('Searching google for ' + words)
                    keyboard.press_and_release('enter')
                elif 'open' in words:
                    words = words.replace(' open ','')
                    LinksAndApps.openLinkorApp(words)
                elif 'time' in words:
                    speakStop(time.strftime("%I:%M %p"))
                elif 'date' in words:
                    speakStop(datetime.date.today())
                elif 'shut down computer' in words:
                    speakStop('Are you sure?')
                    engine.runAndWait()
                    words = recognize.command()
                    if 'yes' in words:
                        os.system("shutdown /s /t 1")
                    else:
                        speakStop('Aborted')
                stop.onWord()
                engine.runAndWait()
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error")


