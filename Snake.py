from arcade import Sprite, SpriteList
from assetLoader import load_sprite
from constants import *

# Tuple: change_x, change_y, angle
DIRECTIONS = {
    "UP": (0, 32, 0),
    "DOWN": (0, -32, 180), 
    "LEFT": (-32, 0, 90),
    "RIGHT": (32, 0, 270)
}
class Snake:
    def __init__(self):
        self.body = SpriteList()
        self.setup()

    def setup(self):
        """Responsible for setting up the Snake class."""
        self.snek_size = 2
        self.head = load_sprite(PLAYER_HEAD, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 32)

        self.tail = load_sprite(PLAYER_TAIL, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.body.extend([self.head, self.tail])

        self.direction = "UP"

        self.last_pos = tuple()

    def draw(self):
        """Method responsible for the drawing of the snake body."""

        self.body.draw()

    def move_head(self, new_direction):
        """Method responsible for moving the SNEK's head
        
        Args:
            new_direction (str): The new direction for the head to move in"""
        prev_angle = self.head.angle

        self.head.change_x = DIRECTIONS[new_direction][0]
        self.head.change_y = DIRECTIONS[new_direction][1]
        self.head.angle = DIRECTIONS[new_direction][2]

        self.last_pos = (self.head.center_x, self.head.center_y, prev_angle)
        self.direction = new_direction

    def move_body(self):
        """Method responsible for moving the SNEK's body"""

        for body_part in self.body[1:]:
            last_pos = self.last_pos
            self.last_pos = body_part.center_x, body_part.center_y, body_part.angle
            body_part.center_x = last_pos[0]
            body_part.center_y = last_pos[1]
            body_part.angle = last_pos[2]


    def update(self, dt: float, dir: str="UP"):
        """Method responsible for the update of the snake body.
        
        Args:
            dt (float): Delta time [Time since last called]
            dir (str): The direction snake is currently headed based on keys pressed."""
        
        self.move_head(dir)
        self.body.update()
        self.move_body()

    def set_new_part_position(self, sprite:Sprite):
        """Method used to position a body part using the last item of the body SpriteList
        
        Args:
            sprite (Sprite): The sprite to position.
            
        Returns:
            Sprite: The positioned sprite."""
        
        previous_part = self.body[-1]
        sprite.center_x = previous_part.center_x + DIRECTIONS[self.direction][0]
        sprite.center_y = previous_part.center_y + DIRECTIONS[self.direction][0]
        sprite.angle = DIRECTIONS[self.direction][2]


    def add_body(self):
        """Method used to add a body part to the Snek"""

        new_body_part = load_sprite(PLAYER_BODY)
        self.set_new_part_position(new_body_part)
        
        self.tail.kill()
        self.tail = load_sprite(PLAYER_TAIL)

        self.body.append(new_body_part)

        self.set_new_part_position(self.tail)
        self.body.append(self.tail)
        self.snek_size += 1
