from functions.interactions import Interactor
import sys
import random
sys.path.append("../")
from db_handler import *

class Spanking:

    @staticmethod
    def SpankIt(spanker, channel, fnc):
        while True:
            rand_user = Interactor.random_user(channel)
            if rand_user == channel:
                if Interactor.random_user(channel) == channel:
                    break
                else:
                    continue
            if rand_user == 'erag0rn':
                if Interactor.random_user(channel) == 'erag0rn':
                    break
                else:
                    continue
            if DBHandler.isnt_on_blacklist(rand_user):
                break

        counter = DBHandler.get_spank_counter(rand_user)

        if counter == 1:
            fnc(spanker + " właśnie dał klapsa " + rand_user + ". Witamy w rodzince bdsm ;) Kreygasm ")
        else:
            randomint = random.randint(1, 30)
            if randomint < 10:
                fnc(spanker + " właśnie dał klapsa " + rand_user + ". To już " + str(counter) + " klaps tego użytkownika! Kappa ")
            elif 9 < randomint < 20:
                fnc(spanker + " sklapsował " + rand_user + ". Po " + str(
                    counter) + " klapsie na pewno musi być czerwony!")
            else:
                fnc(spanker + " przełożył przez kolano " + rand_user + " i dał w pupkę. To " + str(
                    counter) + " klaps. Niech puchnie równo! SwiftRage ")

