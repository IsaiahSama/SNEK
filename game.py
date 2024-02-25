"""This will be the entry point of the game"""
import arcade
from arcade import View
from constants import *

class MenuView(View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()

        arcade.draw_text("SNEK!!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, font_size=60, anchor_x='center')
        arcade.draw_text("Click to begin!", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.3, font_size=20, anchor_x='center')

    def on_mouse_press(self):
        print("I've been clicked!")

class GameView(View):
    def __init__(self):
        super().__init__()

        self.player_list = arcade.SpriteList()
        self.fruit_list = arcade.SpriteList()



if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()