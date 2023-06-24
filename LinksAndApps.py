import os
def openLinkorApp(words):
    if words == 'chess':
        webbrowser.open('https://lichess.org/')
    elif words == 'youtube':
        webbrowser.open('https://www.youtube.com/')
    elif words == 'github':
        webbrowser.open('https://github.com/Mad-Coder-101/')
    elif words == 'mail' or 'gmail':
        webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')
    elif words == 'vs code' or 'visual studio code' or 'code':
        os.startfile("D:\Pranav\Python\VSCODE\Code.exe")


