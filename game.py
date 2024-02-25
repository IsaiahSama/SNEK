"""This will be the entry point of the game"""
import arcade
from arcade import View
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

        self.setup()

    def setup(self):
        """This method is used to set up the game with everything we will need to start."""

        self.player = load_sprite(PLAYER_HEAD, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.fruits = arcade.SpriteList()

        fruit = load_sprite(FRUIT, randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT))

        self.fruits.append(fruit)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        self.player.draw()
        self.fruits.draw()

    def on_update(self):
        self.player.update()
        self.fruits.update()

if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()