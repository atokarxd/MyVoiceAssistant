import imp
from engine import Engine
import datetime
import time

class Time:
    def __init__(self):
        self.motor = Engine()

    def time(self):
        hour = int(datetime.datetime.now().hour)
        tt = time.strftime("%H:%M ")

        if hour >= 0 and hour <= 12:
            data = f"Good morning, {tt}."
        elif hour >= 12 and hour <= 18:
            data = f"Good afternoon, {tt}."
        else:
            data = f"Good evening, {tt}."
        self.motor.Output(data)
        return data

