import os
import time
from datetime import datetime
from playsound import playsound
import pyttsx3
import cv2 as cv
from pathlib import Path


engine = pyttsx3.init()
engine.setProperty('rate', 145)# FAST BUT CLEAR
engine.setProperty('volume', 1.0) #MAX IS 1

#set up the audio files
root_dir =os.path.abspath('.')
gunfire_path = os.path.join(root_dir, 'gunfire.wav')
tone_path = os.path.join("root_dir", 'tone.wav')

#set up the casacdes for face dection
Path= "C:/Pyhton372/Lib/site-packages/cv2/data/"
face_cascade = cv.CascadeClassifier(Path +
                                       'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(Path + 'haarcascade_eye.xml')
#corridor img
os.chdir('corridor_5')
contents = sorted(os.listdir())
#detect faces and fires or disables
for image in contents:
    print(f"\nMotion dected...{datetime.now()}")
    discarge_weapon = True
    engine.say("You have entered an active fire zone.\
               Stop and face the gun immediatly.\
               When you hear the tone, you have 5 seconds to pass.")
