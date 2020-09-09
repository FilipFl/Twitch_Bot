from networking import MyNetworking
from interactions import Interactor


class Bot:

    def __init__(self):
        self.networking = MyNetworking()
        self.networking.join_room()
        self.socket = self.networking.get_socket()
        self.channel = self.networking.get_channel()
        self.interactor = Interactor()

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

