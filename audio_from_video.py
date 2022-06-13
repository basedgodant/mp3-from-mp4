import sys
from moviepy.editor import *

video = VideoFileClip(sys.argv[1]) # video file name in current dir
audio = video.audio
audio.write_audiofile(sys.argv[2]) # new audio file name writes to current dir (must create name)
