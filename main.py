import time

from gtts import gTTS, lang
import pyttsx3
from pygame import mixer

def play_mp3(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

def text2speech(text):
    speech = gTTS(text=text, lang='en', slow=False)
    file_output = "test.mp3"
    speech.save(file_output)
    # time.sleep(10)
    play_mp3(file_output)

def text2speech2(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

text2speech2("This is my first trial.")
text2speech("This is my first trial.")
print (lang.tts_langs())