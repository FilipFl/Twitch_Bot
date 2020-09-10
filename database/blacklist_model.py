from peewee import *


class Blacklist(Model):

    user = CharField()

    class Meta:
        database = SqliteDatabase("bot_db.db")