import speech_recognition as sr

def command():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.dynamic_energy_threshold = .5
    with sr.Microphone() as source:
            audio = recognizer.listen(source,timeout=None)
    words = recognizer.recognize_google(audio).lower()
    print(words)
    return words
