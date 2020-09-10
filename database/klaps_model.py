from peewee import *


class Klaps(Model):
    user = CharField()
    counter = IntegerField()

    class Meta:
        database = SqliteDatabase("bot_db.db")
