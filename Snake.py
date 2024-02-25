from arcade import Sprite, SpriteList
from assetLoader import load_sprite # Deprecated
from assetLoader import get_sprite_textures
from constants import *

# Tuple: change_x, change_y, angle
DIRECTIONS = {
    "UP": (0, 32, 0),
    "DOWN": (0, -32, 180), 
    "LEFT": (-32, 0, 90),
    "RIGHT": (32, 0, 270)
}

class SnakePart(Sprite):
    """Class used to represent a part of the snake <--->"""

    def __init__(self, filename: str, center_x: float=0, center_y:float=0, start_frame:int=0):
        super().__init__(f"{SPRITE_PATH}{filename}.png", center_x=center_x, center_y=center_y)
        self.cur_texture = start_frame
        self.textures = get_sprite_textures(filename+"_dance")

class Snake:
    def __init__(self):
        self.body = SpriteList()
        self.fellas = False
        self.setup()

    def setup(self):
        """Responsible for setting up the Snake class."""
        self.snek_size = 2
        self.head = SnakePart(PLAYER_HEAD, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 32, start_frame=0)

        self.tail = SnakePart(PLAYER_TAIL, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, start_frame=2)

        self.body.extend([self.head, self.tail])

        self.direction = "UP"

        self.last_pos = tuple()

    def all_my_fellas(self):
        """Method used to toggle all my fellas!!!"""
        if not self.fellas:
            pass

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
        self.update_animation()

    def update_animation(self):
        """Method used to update the animation if fellas is active."""

        if not self.fellas: return

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

    def get_start_frame(self) -> int:
        """Gets the appropriate start frame for textures based on how many parts are in the body."""

        return 0 if len(self.body) % 2 else 2

    def add_body(self):
        """Method used to add a body part to the Snek"""

        new_body_part = SnakePart(PLAYER_BODY, start_frame=self.get_start_frame())
        self.set_new_part_position(new_body_part)
        self.body.append(new_body_part)
        
        new_tail = SnakePart(PLAYER_TAIL, start_frame=self.get_start_frame())
        self.tail.kill()
        self.tail = new_tail

        self.set_new_part_position(self.tail)
        self.body.append(self.tail)
        self.snek_size += 1
