import os
import webbrowser
import pyttsx3
engine = pyttsx3.init()
def openLinkorApp(words):
    if words == 'chess':
        webbrowser.open_new('https://lichess.org/')
        engine.say('Opening Chess')
    elif words == 'youtube':
        webbrowser.open_new('https://www.youtube.com/')
        engine.say('Opening Youtube')
    elif words == 'github':
        webbrowser.open_new('https://github.com/Mad-Coder-101/')
        engine.say('Opening Github')
    elif words == 'gmail' or words == 'mail':
        webbrowser.open_new('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
        engine.say('Opening Mail')
    elif words == 'vs code' or words == 'visual studio code' or words == 'code':
        os.startfile("D:\Pranav\Python\VSCODE\Code.exe")
        engine.say('Opening V S Code')
    elif words == 'file explorer':
        os.startfile('Home')
        engine.say('Opening file explorer')
    engine.runAndWait()


