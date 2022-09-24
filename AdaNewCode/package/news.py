import requests
import engine

class News:
    def __init__(self) -> None:
        self.motor = engine.Engine()

    def news(self):
        main_page = requests.get('http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=3015867c23f24be48fe65b9f024d0444').json()

        articles = main_page["articles"]

        head = []

        day = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']

        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            text = f"today's {day[i]} news is: {head[i]}"
            self.motor.Output(text, end='\n')