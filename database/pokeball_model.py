from peewee import *


class Pokeball(Model):

    name = CharField()
    chance = IntegerField()

    class Meta:
        database = SqliteDatabase("bot_db.db")


class Master(Model):

    name = CharField()

    class Meta:
        database = SqliteDatabase("bot_db.db")