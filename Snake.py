from arcade import Sprite, SpriteList
from spriteLoader import load_sprite
from constants import *

class Snake:
    def __init__(self):
        self.body = SpriteList()
        self.setup()

    def setup(self):
        """Responsible for setting up the Snake class."""

        self.head = load_sprite(PLAYER_HEAD, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 32)
        # self.mid = load_sprite(PLAYER_BODY, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.tail = load_sprite(PLAYER_TAIL, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.body.extend([self.head, self.tail])

    def draw(self):
        """Method responsible for the drawing of the snake body."""

        self.body.draw()

    def update(self):
        """Method responsible for the update of the snake body."""

        self.body.update()

