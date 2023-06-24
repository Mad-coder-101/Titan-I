import speech_recognition as sr
import pyttsx3
import wikipedia
import googlesearch
import webbrowser
import LinksAndApps
import os
recognizer = sr.Recognizer()
engine = pyttsx3.init()
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
                    wikipedia.search(words)
                elif 'Google' in words:
                    words = words.replace('search google for', '')
                    googlesearch.search(words)
                elif 'open' in words:
                    words = words.replace(' open ','')
                    LinksAndApps.openLinkorApp(words)
                    print(words)
                
            else:
                continue
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error")


