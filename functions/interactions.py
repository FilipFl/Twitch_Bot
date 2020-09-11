import json
import urlfetch
import time


class Interactor:

    @staticmethod
    def get_user(line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user

    @staticmethod
    def get_message(line):
        separate = line.split(":", 2)
        message = separate[2]
        return message

    @staticmethod
    def random_user(channel):
        response = urlfetch.get("https://2g.be/twitch/randomviewer.php?channel=" + channel)
        random_user = ""
        buf = str(response.content)
        buf = buf.split("'")
        random_user = buf[1]
        random_user = random_user[:-1:]
        return random_user

    @staticmethod
    def get_chatters(channel):
        response = urlfetch.get('https://tmi.twitch.tv/group/user/' + channel + '/chatters')
        data = json.load(response)
        chatters_list = []
        for element in data['chatters'].keys():
            for x in data['chatters'][element]:
                chatters_list.append(x)
        return chatters_list



if __name__ == '__main__':
    interact = Interactor()
