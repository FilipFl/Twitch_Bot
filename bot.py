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
            Spanking.SpankIt(self.last_user, self.channel, self.send_msg)

    def look_for_cmd(self):
        self.check_iq()
        self.check_ranking()
        self.check_spank()

