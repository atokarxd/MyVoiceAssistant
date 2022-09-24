from engine import Engine
from pywikihow import search_wikihow

class HowTo:
    def __init__(self):
        self.motor = Engine()

    def howto(self, text: str) -> str:
        query = text

        how_to = search_wikihow(query, 1)
        #assert len(how_to) == 1
        data = how_to[0].summary

        self.motor.Output(data)
        return data
