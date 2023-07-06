from PIL import Image , ImageTk

from PIL import GifImagePlugin

import tkinter as tk
 
root = tk.Tk()
imageObject = Image.open("bar.gif")

print(imageObject.is_animated)

print(imageObject.n_frames)

 

# Display individual frames from the loaded animated GIF file

for frame in range(0,imageObject.n_frames):

    fr = imageObject.seek(frame)

    make = ImageTk.PhotoImage(fr)

    img = tk.Image(make)

    img.pack()

tk.mainloop()