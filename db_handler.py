from peewee import *
from database.pokeball_model import *
from database.blacklist_model import *
from database.cooldown_model import *
from database.spank_model import *


class DBHandler:

    def __init__(self):
        self.db = SqliteDatabase("bot_db.db")
        self.db.connect()

    def dump_data_manually(self):
        # method used by me for dumping into database things stored in txt files in previous bot version
        self.db.create_tables([Pokeball, Master, Cooldown, Blacklist, Spank])
        spankUser = []
        spankCounter = []
        file = open("database/counters.txt", "r")
        for line in file:
            separate = line.split(" ")
            spankUser.append(separate[0])
            spankCounter.append(int(separate[1]))
        file.close()
        file = open("database/blacklist.txt", "r")
        blacklist = []
        for line in file:
            separate = line.split("\n")
            blacklist.append(separate[0])
        file.close()
        file = open("database/mistrz_pokemon.txt", "r")
        master_pokemon = file.read()
        file.close()
        file = open("database/cooldowns.txt", "r")
        cooldowns = []
        for line in file:
            separate = line
            cooldowns.append(separate)
        file.close()
        file = open("database/pokeball.txt", "r")
        poke = []
        for line in file:
            separate = line
            poke.append(separate)
        file.close()
        for index, element in enumerate(spankUser):
            Spank.create(user=spankUser[index],  counter=spankCounter[index])
        for element in blacklist:
            Blacklist.create(user=element)
        Master.create(name=master_pokemon)
        Cooldown.create(function='pokeball', value=cooldowns[0])
        Cooldown.create(function='spank', value=cooldowns[1])
        Cooldown.create(function='insult', value=cooldowns[2])
        Pokeball.create(name='masterball', chance=poke[0])
        Pokeball.create(name='greatball', chance=poke[1])
        Pokeball.create(name='mythic', chance=poke[2])
        Pokeball.create(name='greatcatch', chance=poke[3])
        Pokeball.create(name='regularcatch', chance=poke[4])
        self.get_blacklist()

    def get_blacklist(self):
        query = Blacklist.select()
        for user in query:
            print(user.user)

    @staticmethod
    def isnt_on_blacklist(user):
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Blacklist.select().where(Blacklist.user == user)
        db.close()
        if query.scalar() is None:
            return True
        else:
            return False

    @staticmethod
    def get_spank_counter(us):
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Spank.select().where(Spank.user == us)
        db.close()
        if query.scalar()is None:
            Spank.create(user=us, counter=1)
            return 1
        else:
            print(query[0].counter)
            query[0].counter = query[0].counter + 1
            query[0].save()
            return query[0].counter

    @staticmethod
    def get_pokemon_master():
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Master.select()
        db.close()
        return query[0].name

    @staticmethod
    def set_pokemon_master(user):
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Master.select()
        query[0].name = user
        query[0].save()
        db.close()

    @staticmethod
    def get_cooldowns():
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Cooldown.select()
        temp_dict = {}
        for element in query:
            temp_dict[element.function] = element.value
        db.close()
        return temp_dict

    @staticmethod
    def get_pokeball_settings():
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Pokeball.select()
        temp_dict = {}
        for element in query:
            temp_dict[element.name] = element.chance
        db.close()
        return temp_dict

    @staticmethod
    def get_ranking():
        db = SqliteDatabase("bot_db.db")
        db.connect()
        napis = "Wyniki! "
        query = Spank.select().order_by(Spank.counter.desc())
        if len(query) > 10:
            for i in range(10):
                napis += str(i + 1) + ". " + query[i].user + " - " + str(query[i].counter) + " klapsów!    "
        else:
            for i in range(len(query)):
                napis += str(i + 1) + ". " + query[i].user + " - " + str(query[i].counter) + " klapsów!    "
        db.close()
        return napis

    @staticmethod
    def get_most_spanked():
        db = SqliteDatabase("bot_db.db")
        db.connect()
        query = Spank.select().order_by(Spank.counter.desc())
        db.close()
        return query[0].user, query[0].counter


if __name__ == '__main__':
    handle = DBHandler()
    print(handle.dump_data_manually())
