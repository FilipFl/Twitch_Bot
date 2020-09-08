from PySide2.QtWidgets import QMessageBox
import socket
import string
import os


class MySocket:

    def __init__(self):
        self.host = "irc.chat.twitch.tv"
        self.port = 6667
        self.identity = None
        self.password = None
        self.channel = None
        self.s = socket.socket()
        self.s.connect((self.host, self.port))
        if self.get_config():
            self.s.send(("PASS " + self.password + "\r\n").encode())
            self.s.send(("NICK " + self.identity + "\r\n").encode())
            self.s.send(("JOIN #" + self.channel + "\r\n").encode())

    def get_config(self):
        if os.path.exists("./data/settings.txt"):
            f = open("./data/settings.txt", "r")
            read = f.readlines()
            self.password = read[0]
            self.identity = read[1]
            self.channel = read[2]
            f.close()
            return True
        else:
            error_info = QMessageBox()
            error_info.setWindowTitle("Error!")
            error_info.setText("No settings directory")
            error_info.setStandardButtons(QMessageBox.Ok)
            error_info.exec_()
            return False

    def get_socket(self):
        return self.s

    def send_message(self, message):
        temp_message = "PRIVMSG #" + self.channel + " :" + message
        self.s.send((temp_message + "\r\n").encode())
        print("Sent: " + temp_message)

    def join_room(self):
        read_buffer = ""
        loading = True
        while loading:
            read_buffer = read_buffer + self.s.recv(1024).decode()
            temp = str.split(read_buffer, "\n")
            read_buffer = temp.pop()
            for line in temp:
                print(line)
                loading = self.loading_complete(line)
        self.send_message("Successfully joined chat")

    def loading_complete(self, line):
        if ("End of /NAMES list" in line):
            return False
        else:
            return True

