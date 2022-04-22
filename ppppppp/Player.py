import models
from pygame import mixer
from tkinter import filedialog
import os
from mutagen.mp3 import MP3


class Player:
    def __init__(self):
        mixer.init()
        self.mymodel=models.Model()

    def get_db_status(self):
        return self.mymodel.get_db_status()

    def close_player(self):
        mixer.music.stop()
        self.mymodel.close_db_connection()

    def set_volume(self,volume_level):
        mixer.music.set_volume(volume_level)

    def add_songs(self):
        song_path=filedialog.askopenfilenames(title="select your song.." ,filetypes=[("mp3 file","*.mp3")])
        song_name = []
        if song_path is None:
            return
        else:
            for i in song_path:
                j=os.path.basename(i)
                song_name.append(j)
                self.mymodel.add_song(j,i)
        return song_name

    def remove_song(self,song_name):
        self.mymodel.remove_song(song_name)

    def get_song_length(self,song_name):
        self.song_path=self.mymodel.get_song_path(song_name)
        self.audio_info=MP3(self.song_path)
        song_length=self.audio_info.info.length
        return song_length

    def play_song(self):
        mixer.quit()
        mixer.init(frequency=self.audio_info.info.sample_rate)
        mixer.music.load(self.song_path)
        mixer.music.play()

    def stop_song(self):
        mixer.music.stop()

    def pause_song(self):
        mixer.music.pause()

    def unpause_song(self):
        mixer.music.unpause()

    def add_song_to_favourites(self,song_name):
        song_path=self.mymodel.get_song_path(song_name)
        result=self.mymodel.add_song_to_favourites(song_name,song_path)
        return result

    def load_song_from_favourites(self):
        result=self.mymodel.load_song_from_favourites()
        return result,self.mymodel.song_dict

    def remove_song_from_favourites(self,song_name):
        result=self.mymodel.remove_song_from_favourites(song_name)
        return result

    def get_song_count(self):
        return len(self.mymodel.song_dict)



