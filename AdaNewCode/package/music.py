import imp
from re import search
from urllib import parse, request
from engine import Engine
from youtube_dl import YoutubeDL
from os import chdir, listdir, rename
from pygame import init as PyGameInit
from pygame.mixer import init as PyMusicInit
from pygame.mixer import music as PyMusic


class Music:
    def __init__(self, music_name):
        self.motor = Engine()

        self.music_name = music_name

    def _download(self):
        ydl_options = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'outtmpl': '~/Desktop/Chaos/AdaNewCode/deletefile/%(title)s.%(ext)s',
            'audioformat': 'mp3',
            'noplaylist': True,
            'nocheckcertificate': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        query_string = parse.urlencode({'search_query': self.music_name})
        html_content = request.urlopen('https://www.youtube.com/results?' + query_string)
        video_id = search(r'/watch\?v=(.{11})', html_content.read().decode())
        url = 'https://www.youtube.com/watch?v=' + video_id.group(1)

        # Youtube download
        with YoutubeDL(ydl_options) as ydl:
            ydl.download([url])

        chdir('deletefile/music')
        for f in listdir(): # Egy listában lévő nem odaillő szók kiszedése
            self.music_name = str(f).replace('official', '').replace('lyrics', '').replace('video', '').replace('music','').replace('(  )', '').replace('( )', '').replace('()', '').replace(' - ', '-').replace(' ', '-').lower().replace('ó', 'O').replace('á', 'A').replace('ő', 'L').replace('ö', 'K').replace('é', 'E').replace('í','I').replace('ü', 'Z').replace('ű', 'M').replace('ú', 'N')
            rename(f, self.music_name)
        
    def play_music(self):
        PyGameInit()
        PyMusicInit()
        file = r'~/Desktop/Chaos/AdaNewCode/deletefile/{name}'.format(name = self.music_name)
        PyMusic.load(file)
        PyMusic.play()
    
    def other_functions_music(self, query):
        if "elég lesz" in query:
            PyMusic.stop()
        
        if "állítsd meg" in query:
            PyMusic.pause()
        
        if "indíthatód" in query:
            PyMusic.unpause()

    def app_sound_controll(self, percentage):
        PyMusic.set_volume(percentage)