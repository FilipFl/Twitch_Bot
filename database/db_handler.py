from peewee import *

class DBHandler:

    def __init__(self):
        self.db = SqliteDatabase("bot_db.db")
        self.db.connect()