"""This Class is responsible for loading sprites."""
from arcade import Sprite

def load_sprite(sprite_name: str, center_x: float, center_y: float) -> Sprite:
    """Function used to create a sprite at the given x and y co-ordinates"""
    
    return Sprite("./Assets/Sprites/" + sprite_name, center_x=center_x, center_y=center_y)