import os
import random
import rich
from enum import Enum


class Fields:
    MAIN = 'map'
    RADAR = 'radar'
    WEIGHT = 'weight'


class BaseColors(Enum):
    RED = '\033[1;93m'
    BLUE = '\033[0;34m'
    YELLOW = '\033[1;93m'
    YELLOW2 = '\033[1;35m'
    RESET_COLOR = '\033[0m'
    MISS = '\033[0;37m'


class Color(BaseColors):
    def __init__(self):
        pass

    def get_color_text(self, text, color):
        return self.color + text + self.RESET_COLOR


def main():
    players = [
        Player(name='Username', is_ai=False, auto_ship=True, skill=1),
        Player(name='IQ180', is_ai=True, auto_ship=True, skill=1)
    ]

    game = Game()

    while True:
        game.get_status()




if __name__ == '__main__':
    main()
