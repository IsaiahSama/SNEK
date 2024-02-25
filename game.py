"""This will be the entry point of the game"""
import arcade
from arcade import View
import arcade.key
from constants import *
from Snake import Snake
from assetLoader import load_sprite, load_sound, load_resource_sound
from random import randrange


click_sound = load_resource_sound(CLICK)

class MenuView(View):
    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)


    def on_draw(self):
        self.clear()

        arcade.draw_text("SNEK!!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, font_size=60, anchor_x='center')
        arcade.draw_text("Click to begin!", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.4, font_size=20, anchor_x='center')
        arcade.draw_text("Press M to toggle your fellas.", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.2, font_size=14, anchor_x='center')

    def on_mouse_press(self, *args):
        click_sound.play()
        game_view = GameView()
        self.window.show_view(game_view)

class GameView(View):
    def __init__(self):
        super().__init__()
        self.window.set_update_rate(1/2)
        self.main_sound = load_sound(MAIN_GAME)
        self.eat_sound = load_resource_sound(NOM)
        self.lose_sound = load_resource_sound(LOSE)
        self.main_player = None
        self.setup()

    def setup(self):
        """This method is used to set up the game with everything we will need to start."""
        self.score = 0
        self.player = Snake()
        self.fruit = load_sprite(FRUIT, randrange(TILE_X) * SIZE + (SIZE // 2), randrange(TILE_Y) * SIZE + (SIZE // 2))

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

        hit_list = arcade.check_for_collision(self.player.head, self.fruit)
        if hit_list:
            self.fruit.kill()
            self.fruit = load_sprite(FRUIT, randrange(SCREEN_WIDTH), randrange(SCREEN_HEIGHT))
            self.player.add_body()
            self.eat_sound.play()

        self.stay_in_bounds()

        hit_list = arcade.check_for_collision_with_list(self.player.head, self.player.body)
        if hit_list:
            self.game_over()

    def game_over(self):
        """This method is used to run the game over sequence."""
        if self.main_player and self.main_sound.is_playing(self.main_player):
            self.main_sound.stop(self.main_player)

        self.lose_sound.play()
        game_over = GameOverView()
        game_over.setup(self.player.snek_size)
        self.window.show_view(game_over)

    def stay_in_bounds(self):
        """Method used to ensure the player stays in bounds."""
        if self.player.head.center_x < 0:
            self.player.head.center_x = SCREEN_WIDTH - (SIZE // 2)
        if self.player.head.center_x > SCREEN_WIDTH:
            self.player.head.center_x = SIZE // 2
        if self.player.head.center_y < 0:
            self.player.head.center_y = SCREEN_HEIGHT - (SIZE // 2)
        if self.player.head.center_y > SCREEN_HEIGHT:
            self.player.head.center_y = SIZE // 2


    def on_key_press(self, key: int, modifiers: int):
        if key in (arcade.key.W, arcade.key.UP):
            self.current_direction = "UP" 
        elif key in (arcade.key.A, arcade.key.LEFT):
            self.current_direction = "LEFT" 
        elif key in (arcade.key.S, arcade.key.DOWN):
            self.current_direction = "DOWN" 
        elif key in (arcade.key.D, arcade.key.RIGHT):
            self.current_direction = "RIGHT" 
        elif key == arcade.key.M:
            if self.main_player and self.main_sound.is_playing(self.main_player):
                self.main_sound.stop(self.main_player)
                self.player.all_my_fellas(False)
            else:
                self.main_player = self.main_sound.play(loop=True)
                self.player.all_my_fellas(True)

class GameOverView(View):
    def setup(self, score: int):
        """Method used to setup the game over view"""
        self.score = score

    def on_show_view(self):
        arcade.set_background_color(arcade.color.RED_BROWN)

    def on_draw(self):
        self.clear()

        arcade.draw_text("You have fallen.", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.7, font_size=40, anchor_x='center')
        arcade.draw_text(f"Your size: {self.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.3, font_size=20, anchor_x='center')
        arcade.draw_text("Click to play again!", SCREEN_WIDTH // 2, SCREEN_HEIGHT * 0.5, anchor_x='center')

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        click_sound.play()
        game_view = GameView()
        self.window.show_view(game_view)

if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()