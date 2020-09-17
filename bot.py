from networking import MyNetworking
from functions.interactions import Interactor
from functions.iq import *
from db_handler import *
from functions.spank import Spanking
import time

class Bot:

    def __init__(self):
        self.networking = MyNetworking()
        self.networking.join_room()
        self.socket = self.networking.get_socket()
        self.channel = self.networking.get_channel()
        self.last_time = time.time()
        self.last_message = None
        self.last_user = None
        self.info = True
        self.cooldowns = DBHandler.get_cooldowns()
        self.user_cooldowns = {}
        self.running = True

    def send_info(self):
        if time.time() - 180 > self.last_time:
            if self.info:
                self.send_msg("Aktualny Mistrz Pokemon: " + DBHandler.get_pokemon_master())
            else:
                user, counter = DBHandler.get_most_spanked()
                self.send_msg("Najczęściej klapsowanym użytkownikiem jest " + user + "! Na pupkę zebrał aż " +
                              str(counter) + " klapsów!")
            self.info = not self.info
            self.last_time = time.time()

    def listen_chat(self):
        readbuffer = ""
        readbuffer = readbuffer + self.socket.recv(1024).decode()
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()
        for line in temp:
            if "PING :tmi.twitch.tv" in line:
                self.socket.send(bytes("PONG :tmi.twitch.tv\r\n", "UTF-8"))
                continue
            self.last_user = Interactor.get_user(line)
            self.last_message = Interactor.get_message(line)
            print(self.last_user + " typed: " + self.last_message)
            self.look_for_cmd()

    def send_msg(self, message):
        self.networking.send_message(message)

    def check_iq(self):
        if "!iq\r" in self.last_message:
            temp_msg = self.last_user + ' ma ' + Iq.get_iq() + ' IQ.'
            self.send_msg(temp_msg)

    def check_ranking(self):
        if "!ranking\r" in self.last_message:
            self.send_msg(DBHandler.get_ranking())

    def check_spank(self):
        if"!klaps\r" in self.last_message:
            print(self.user_cooldowns)
            if self.check_cooldown('spank'):
                print(self.user_cooldowns)
                Spanking.SpankIt(self.last_user, self.channel, self.send_msg)

    def check_cooldown(self, function):
        if self.last_user in self.user_cooldowns:
            if function in self.user_cooldowns[self.last_user]:
                if time.time() - self.cooldowns[function] > self.user_cooldowns[self.last_user][function]:
                    self.user_cooldowns[self.last_user][function] = time.time()
                    return True
                else:
                    return False
            else:
                self.user_cooldowns[self.last_user][function] = time.time()
                return True
        else:
            self.user_cooldowns[self.last_user] = {}
            self.user_cooldowns[self.last_user][function] = time.time()
            return True

    def check_end(self):
        if"!koniecpsot\r" in self.last_message and self.last_user == 'erag0rn':
            self.running = False

    def guiless(self):
        while True:
            self.listen_chat()

    def look_for_cmd(self):
        self.check_iq()
        self.check_ranking()
        self.check_spank()
        self.check_end()


if __name__ == '__main__':
    bot = Bot()
    bot.guiless()
