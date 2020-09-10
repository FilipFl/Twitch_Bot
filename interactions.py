import json
import urlfetch
import time

class Interactor:

    def __init__(self):
        pass

    def get_user(self, line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    def get_message(self, line):
        separate = line.split(":", 2)
        message = separate[2]
        return message

    def random_user(self, channel):
        response = urlfetch.get("https://2g.be/twitch/randomviewer.php?channel=" + channel)
        random_user = ""
        buf = str(response.content)
        buf = buf.split("'")
        random_user = buf[1]
        random_user = random_user[:-1:]
        return random_user

    def get_chatters(self):
        response = urlfetch.get('https://tmi.twitch.tv/group/user/leon_official/chatters')
        data = json.load(response)
        chatters_list = []
        for element in data['chatters'].keys():
            for x in data['chatters'][element]:
                chatters_list.append(x)
        return chatters_list



if __name__ == '__main__':
    interact = Interactor()
