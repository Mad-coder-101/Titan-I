import tkinter as tk
import moviepy.editor as mp
root = tk.Tk()
bar_stay = tk.PhotoImage('pinkbluebar.png')
bar_leave = tk.Video('bar_fade.mp4')
blob = tk.Video('blob.blob.mp4')
def start():
    bar_stay.pack()

def command_start():
    bar_stay.destroy()
    bar_leave.pack()
    
def command_speak():
    bar_leave.destroy()
    blob.pack()
