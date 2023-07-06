import keyboard
import pyttsx3
def pause():
    if keyboard.is_pressed('esc'):
        engine.stop()
