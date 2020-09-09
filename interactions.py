import json
import urlfetch


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
        print(random_user)
        return random_user