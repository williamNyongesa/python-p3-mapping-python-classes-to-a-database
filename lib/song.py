import sqlite3

CONNECT = sqlite3.connect('music.db')
CURSOR = CONNECT.cursor()

class Song:
    def __init__(self, name, album, id = None):
        self.id = id
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE 
        IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
        )"""
        CURSOR.execute(sql)
        CONNECT.commit()

    def save(self):
        sql = """INSERT INTO songs (name, album) VALUES (?, ?)"""
        CURSOR.execute(sql, (self.name, self.album))
        CONNECT.commit()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)  
        song.save() 
        song.id = CURSOR.lastrowid
        return song  

