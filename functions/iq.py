import random

class Iq:

    @staticmethod
    def get_iq():
        iq = random.randint(-1,200)
        return str(iq)