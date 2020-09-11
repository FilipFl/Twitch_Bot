from peewee import *


class Spank(Model):
    user = CharField()
    counter = IntegerField()

    class Meta:
        database = SqliteDatabase("bot_db.db")
