from peewee  import *

class Cooldown(Model):
    function = CharField()
    value = IntegerField()

    class Meta:
        database = SqliteDatabase("bot_db.db")




