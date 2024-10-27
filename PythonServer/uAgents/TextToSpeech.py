from gtts import gTTS
import os
from playsound import playsound



def outputText(text):

    language='en'
    output=gTTS(text=text, lang=language, slow=False)
    output.save("output.mp3")
    playsound("output.mp3", True)
