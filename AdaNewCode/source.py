import requests
from struct import pack
from engine import Engine
from package import time as PackTime
from package import weather, howto, music 
import webbrowser

class Source:
    def __init__(self, username: str):
        self.motor = Engine()

        self.username = username
        ipinfo = requests.get('https://ipinfo.io/')
        self.local_data = ipinfo.json()

    def brain(self, query: str) -> str:
        try:
            #query = self.motor.Input()

            if query in ["hello", "hi", "hey"]:
                self.motor.Output(f"Hello {self.username}.")
            
            if query in ['what time is it?', 'time']:
                PackTime.Time().time()

            if query in ["what's the weather like?"]:
                weather.Weather().weather()
            
            if "how to" in query:
                howto.HowTo().howto(query.replace("how to ", ""))

            if "what is my ip address" in query:
                try:
                    self.motor.Output(f"Your ip address: {self.local_data['ip']}.")
                except:
                    self.motor.Output("You're not connected to the Internet.")

            if "open google" in query or "search" in query:
                self.motor.Output("What do you want to search?")
                search = self.motor.Input()
                webbrowser.open(f'https://www.google.hu/search?q={search}')

            if query in ["no thanks", "no thank you", "no"]:
                self.motor.Output("Okay.")

            if  query in ["where am i", "where are we"]:
                self.motor.Output("Wait, I check...")
                try:
                    location = self.local_data['loc'].split(',')

                    self.motor.Output(f"Latitude: {location[0]} degrees.\nLongitude: {location[1]} degrees.\nThe city where you are: {self.local_data['city']}.") # location[0] -> latitude | location[1] -> longitude

                except Exception:
                    self.motor.Output("Sorry, I can't find ourselves, We're probably not connected to the internet.")

            if "who are you" in query:
                self.motor.Output("I'm ADA, who is an Artificial Intelligence.")

            if "play music" in query:
                music.Music(query.replace("play music", ""))



            else:
                self.motor.Output("I don't hear you.")

        except SyntaxError:
            self.motor.Output("")

if __name__ == "__main__":
    obj = Source("atokarxd")
    obj.brain("what's the weather like?")
