# E-N-G-I-N-E
import pyttsx3 # download
import speech_recognition as sr # download

import time

class Engine:

    def __init__(self):
        self.motor = pyttsx3.init()
        voice = self.motor.getProperty('voices')
        self.motor.setProperty('voices', voice[len(voice) - 1].id)

    # Output Voice
    def Output(self, audio: str) -> str:
        self.motor.say(audio)
        print(audio)
        self.motor.runAndWait()

    # Input Voice
    def Input(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=10, phrase_time_limit=6)

        try:
            print("processing...")
            query = r.recognize_google(audio, language="en-US")
            print(f"User: {query}")

        except Exception:
            #self.Output("I didn't hear you right, please tell me again")
            return None
        #query = query.lower()
        return query.lower()

    def HIO(self, audio: str) -> str:
        # This is Output
        self.Output(audio)

        # This is Input
        self.Input()
        

if "__main__" == __name__:
    obj = Engine()
    while True:
        obj.Output("I love you")
        time.sleep(2)
