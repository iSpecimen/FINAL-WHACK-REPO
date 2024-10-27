import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def recordInput():
    while (True):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2)

                audio2=r.listen(source2)
                MyText= r.recognize_google(audio2)

                return MyText
        except:
            return None



