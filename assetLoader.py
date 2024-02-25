"""This Class is responsible for loading assets."""
from arcade import Sprite, Sound

def load_sprite(sprite_name: str, center_x: float=0, center_y: float=0) -> Sprite:
    """Function used to create a sprite at the given x and y co-ordinates
    
    Args:
        sprite_name (str): The name of the sprite.
        center_x (float): The x position for the sprite
        center_y (float): The y position for the sprite
        
    Returns:
        Sprite"""
    
    return Sprite("./Assets/Sprites/" + sprite_name, center_x=center_x, center_y=center_y)

def load_sound(sound_name:str) -> Sound:
    """Function used to load a sound!
    
    Args:
        sound_name (str): The name of the sound to load."""
    
    return Sound("./Assets/Sounds/" + sound_name)