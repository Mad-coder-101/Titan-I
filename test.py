import wikipedia, pyttsx3
engine = pyttsx3.init()
result = wikipedia.summary('Desktop Computer',sentences = 2)
engine.say(result)
engine.runAndWait()