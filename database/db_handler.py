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
        self.db.create_tables([Pokeball, Master, Cooldown, Blacklist, Spank])
        spankUser = []
        spankCounter = []
        file = open("counters.txt", "r")
        for line in file:
            separate = line.split(" ")
            spankUser.append(separate[0])
            spankCounter.append(int(separate[1]))
        file.close()
        file = open("blacklist.txt", "r")
        blacklist = []
        for line in file:
            separate = line.split(" ")
            blacklist.append(separate[0])
        file.close()
        file = open("mistrz_pokemon.txt", "r")
        master_pokemon = file.read()
        file.close()
        file = open("cooldowns.txt", "r")
        cooldowns = []
        for line in file:
            separate = line
            cooldowns.append(separate)
        file.close()
        file = open("pokeball.txt", "r")
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

    def is_on_blacklist(self, user):
        query = Blacklist.select().where(Blacklist.user == user)
        if query.scalar() is not None:
            return True
        else:
            return False

    def get_spank_counter(self, us):
        query = Spank.select().where(Spank.user == us)
        if query.scalar()is None:
            Spank.create(user=us, counter=1)
            return 1
        else:
            return query[0].counter

    def get_pokemon_master(self):
        query = Master.select()
        return query[0].name

    def set_pokemon_master(self, user):
        query = Master.select()
        query[0].name = user
        query[0].save()

    def get_cooldowns(self):
        query = Cooldown.select()
        temp_dict = {}
        for element in query:
            temp_dict[element.function] = element.value
        return temp_dict

    def get_pokeball_settings(self):
        query = Pokeball.select()
        temp_dict = {}
        for element in query:
            temp_dict[element.name] = element.chance
        return temp_dict


if __name__ == '__main__':
    handle = DBHandler()
    print(handle.get_pokeball_settings())
