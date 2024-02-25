"""This Class is responsible for loading assets."""
from arcade import Sprite, Sound, Texture, load_texture
from constants import SPRITE_PATH

def load_sprite(sprite_name: str, center_x: float=0, center_y: float=0) -> Sprite:
    """Function used to create a sprite at the given x and y co-ordinates
    
    Args:
        sprite_name (str): The name of the sprite.
        center_x (float): The x position for the sprite
        center_y (float): The y position for the sprite
        
    Returns:
        Sprite"""
    
    return Sprite("./Assets/Sprites/" + sprite_name + ".png", center_x=center_x, center_y=center_y)

def get_idle_texture(sprite_name:str) -> Texture:
    """Function used to get the Idle texture for a sprite.
     
    Args:
        sprite_name (str): The name of the sprite to get the idle texture for
        
    Returns:
        Texture"""
    
    return load_texture(f"{SPRITE_PATH}{sprite_name}.png")

def get_sprite_textures(texture_path: str) -> list:
    """Function used to load the animated textures.
    
    Args:
        texture_path (str): The path to the textures.
        
    Returns:
        list: List of textures for animating"""

    dance_textures = []
    for i in range(4):
        texture = load_texture(f"./Assets/Sprites/{texture_path}/{texture_path}{i}.png")
        dance_textures.append(texture)

    return dance_textures

def load_sound(sound_name:str) -> Sound:
    """Function used to load a sound!
    
    Args:
        sound_name (str): The name of the sound to load.
        
    Returns:
        Sound"""
    
    return Sound("./Assets/Sounds/" + sound_name)

def load_resource_sound(sound_name:str) -> Sound:
    """Function used to load a sound provided as a built in resource.
    
    Args:
        sound_name (str): The name of the sound to load.
        
    Returns: 
        Sound"""
    
    return Sound(":resources:sounds/" + sound_name)