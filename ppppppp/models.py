from cx_Oracle import *
from traceback import *


class Model:
    def __init__(self):
        self.song_dict = {}
        self.db_status = True
        self.conn = None
        self.cur = None
        try:
            self.conn = connect("Mouzikka/music@127.0.0.1/xe")
            self.cur = self.conn.cursor()
        except DatabaseError:
            self.db_status = False
            print(format_exc())

    def get_db_status(self):
        return self.db_status

    def close_db_connection(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

    def add_song(self, song_name, song_path):
        self.song_dict[song_name] = song_path

    def get_song_path(self, song_name):
        print(self.song_dict)
        return self.song_dict[song_name]

    def remove_song(self, song_name):
        self.song_dict.pop(song_name)

    def search_song_in_favourites(self, song_name):
        self.cur.execute("select song_name from myfavourites where song_name=:1", (song_name,))
        song_tuple = self.cur.fetchone()
        if song_tuple is None:
            return False
        else:

            return True

    def add_song_to_favourites(self, song_name, song_path):
        is_song_present = self.search_song_in_favourites(song_name)
        if is_song_present:
            return "Song already present in your favourites"
        self.cur.execute("select max(song_id) from myfavourites")
        last_song_id = self.cur.fetchone()[0]
        next_song_id = 1
        if last_song_id is not None:
            next_song_id = last_song_id + 1
        self.cur.execute("insert into myfavourites values(:1,:2,:3)", (next_song_id, song_name, song_path))
        self.conn.commit()
        return "Song added to your favourites"

    def load_song_from_favourites(self):
        self.cur.execute("select song_name,song_path from myfavourites")
        song_present = False
        for song_name, song_path in self.cur:
            self.song_dict[song_name] = song_path
            song_present = True
        if song_present==True:
            return "List populated from favourites"
        else:
            return "No songs present in your favourites"

    def remove_song_from_favourites(self, song_name):
        self.cur.execute("delete from myfavourites where song_name=:1",(song_name,))
        count=self.cur.rowcount
        if count ==0:
            return "song not present in your favourites"
        else:
            #self.song_dict.pop(song_name)
            self.conn.commit()
            return "song deleted fromm your favourite"




