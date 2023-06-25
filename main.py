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
                    result = wikipedia.search(words,sentences = 5)
                    engine.say(result)
                    engine.runAndWait()
                    
                elif 'Google' in words:
                    words = words.replace('search google for', '')
                    result = googlesearch.search(words)
                    print('ok')
                elif 'open' in words:
                    words = words.replace(' open ','')
                    LinksAndApps.openLinkorApp(words)
                
            else:
                continue
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error")


