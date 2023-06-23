import speech_recognition as sr
import pyttsx3
import wikipedia
import googlesearch
recognizer = sr.Recognizer()
engine = pyttsx3.init()
recognizer.dynamic_energy_threshold = False
recognizer.dynamic_energy_threshold = .5
recognizer.set_output_format("audio")
if __name__ == '__main__':
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source,timeout=None)
        try:
            words = recognizer.recognize_google(audio)
            if 'quit' in words:
                engine.stop()
                break
            if 'Titan' in words:
                engine.say('Hello, how can I help you?')
                engine.runAndWait()

            else:
                continue
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error")


