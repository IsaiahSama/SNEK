"""This will be the entry point of the game"""
import arcade
from arcade import View
import arcade.key
from constants import *
from Snake import Snake
from spriteLoader import load_sprite
from random import randrange

class MenuView(View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_text("SNEK!!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, font_size=60, anchor_x='center')
        arcade.draw_text("Click to begin!", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.3, font_size=20, anchor_x='center')

    def on_mouse_press(self, *args):
        game_view = GameView()
        self.window.show_view(game_view)

class GameView(View):
    def __init__(self):
        super().__init__()
        self.window.set_update_rate(1/2)
        self.setup()

    def setup(self):
        """This method is used to set up the game with everything we will need to start."""
        self.score = 0
        self.player = Snake()
        self.fruit = load_sprite(FRUIT, randrange(TILE_X) * SIZE, randrange(TILE_Y) * SIZE)

        self.current_direction = self.player.direction

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        self.player.draw()
        self.fruit.draw()

        arcade.draw_text(f"Size: {self.player.snek_size}", 10, SCREEN_HEIGHT - 20 )

    def on_update(self, dt:float):
        self.player.update(dt, self.current_direction)
        self.fruit.update()

        hit_list = arcade.check_for_collision(self.player.body[0], self.fruit)
        if hit_list:
            self.fruit.kill()
            self.fruit = load_sprite(FRUIT, randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT))
            self.player.add_body()

    def on_key_press(self, key: int, modifiers: int):
        if key in (arcade.key.W, arcade.key.UP):
            self.current_direction = "UP" 
        elif key in (arcade.key.A, arcade.key.LEFT):
            self.current_direction = "LEFT" 
        elif key in (arcade.key.S, arcade.key.DOWN):
            self.current_direction = "DOWN" 
        elif key in (arcade.key.D, arcade.key.RIGHT):
            self.current_direction = "RIGHT" 

if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()