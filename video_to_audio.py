import moviepy.editor as mv
from tkinter.filedialog import *

vid = askopenfilename()
video = mv.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("demo.mp3")

print("print----")