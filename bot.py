from networking import MyNetworking
from interactions import Interactor
from functions.iq import *
import time

class Bot:

    def __init__(self):
        self.networking = MyNetworking()
        self.networking.join_room()
        self.socket = self.networking.get_socket()
        self.channel = self.networking.get_channel()
        self.interactor = Interactor()
        self.last_time = time.time()

    def send_info(self):
        if time.time() - 60 > self.last_time:
            self.send_msg("Filip jest najlepszy!")
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
            user = self.interactor.get_user(line)
            message = ""
            message = self.interactor.get_message(line)
            print(user + " typed: " + message)
            self.look_for_cmd(user, message)


    def send_msg(self, message):
        self.networking.send_message(message)

    def check_iq(self, user, message):
        if "!iq\r" in message:
            temp_msg = user + ' ma ' + Iq.get_iq() + ' IQ.'
            self.send_msg(temp_msg)

    def look_for_cmd(self, user, message):
        self.check_iq(user, message)

