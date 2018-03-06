import os
import moviepy.editor as mp
from os import listdir


for f in listdir('./video'):
    name = f.split('.')[0]
    clip = mp.VideoFileClip('./video/{}'.format(f))
    clip.audio.write_audiofile('./audio/{}.mp3'.format(name))


