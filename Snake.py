from arcade import Sprite, SpriteList
from spriteLoader import load_sprite
from constants import *

DIRECTIONS = {
    "UP": (0, 32),
    "DOWN": (0, -32), 
    "LEFT": (-32, 0),
    "RIGHT": (32, 0)
}
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

        self.direction = "UP"

    def draw(self):
        """Method responsible for the drawing of the snake body."""

        self.body.draw()

    def move_body(self):
        """Method responsible for moving the SNEK"""
        self.head.change_x = DIRECTIONS[self.direction][0]
        self.head.change_y = DIRECTIONS[self.direction][1]
        

    def update(self, dt: float, dir: str="UP"):
        """Method responsible for the update of the snake body.
        
        Args:
            dt (float): Delta time [Time since last called]
            dir (str): The direction snake is currently headed based on keys pressed."""
        
        self.direction = dir
        self.move_body()
        self.body.update()

