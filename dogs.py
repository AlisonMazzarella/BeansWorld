# Basic arcade program 
#Dog tries to catch objects it likes -- treats, birds
#Avoids touching object it hates -- leash, shots

# Imports
import arcade
import random
import os

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Beans World"
RADIUS = 150

#Pixels 
VIEWPORT_MARGIN = 220 

#More Constants
PLAYER_SCALING = 0.5
TREAT_SCALING = 0.25
BIRDS_SCALING = 0.25
SHOT_SCALING = 0.15
LEASH_SCALING = 0.35 


class Treat(arcade.Sprite):
    """
    This class represents the objects on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the object
        self.center_y -= 1

        # See if the object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Birds(arcade.Sprite):
    """
    This class represents the objects on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the object
        self.center_y -= 1

        # See if the object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Shot(arcade.Sprite):
    """
    This class represents the objects on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the object
        self.center_y -= 1

        # See if the object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class Leash(arcade.Sprite):
    """
    This class represents the objects on our screen. It is a child class of
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):

        # Reset the object to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20,
                                         SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):

        # Move the object
        self.center_y -= 1

        # See if the object has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()

class BeansWorld(arcade.Window):
    """ Main application class. """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE): 
        """ Initializer """

        #Call parent class 
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #Set directory 
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #Background image 
        self.background = None 

        #Sprite list
        self.player_list = None 
        self.treat_list = None
        self.bird_list = None
        self.shot_list = None
        self.leash_list = None 

        #Player information 
        self.player_sprite = None
        self.score = 0
        self.score_text = None

        #Mouse cursor 
        self.set_mouse_visible(False) 

        #Set background color 
        arcade.set_background_color(arcade.color.BUBBLES)

    def on_key_press(self, symbol, modifiers): 
        """ Handle user keyboard input. 
        Q. Quit the game
        P: Pause/Unpause the game """

        #Quit
        if symbol == arcade.key.Q:
            arcade.close_window()

        #Pause/Unpause
        if symbol == arcade.key.P:
            self.paused = not self.paused
      
    def setup(self):
        """ Set up the game and initialize the variables. """

        #Background 
        self.background = arcade.load_texture("images/dog_park.jpg")

        #Sprites
        self.player_list = arcade.SpriteList()
        self.treat_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.shot_list = arcade.SpriteList()
        self.leash_list = arcade.SpriteList()

        #Player
        self.score = 0 
        self.player_sprite = arcade. Sprite("images/dog.png", PLAYER_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50 
        self.player_list.append(self.player_sprite)

        for i in range(8):

            #Create object distance
            treat = Treat("images/treat.png", TREAT_SCALING)
            bird = Birds("images/bird.png", BIRDS_SCALING)
            shot = Shot("images/shot.png", SHOT_SCALING)
            leash = Leash("images/leash.png", LEASH_SCALING)

            #Object positions
            treat.center_x = random.randrange(SCREEN_WIDTH)
            treat.center_y = random.randrange(SCREEN_HEIGHT)

            bird.center_x = random.randrange(SCREEN_WIDTH)
            bird.center_y = random.randrange(SCREEN_HEIGHT)

            shot.center_x = random.randrange(SCREEN_WIDTH)
            shot.center_y = random.randrange(SCREEN_HEIGHT)

            leash.center_x = random.randrange(SCREEN_WIDTH)
            leash.center_y = random.randrange(SCREEN_HEIGHT)

            #Add objects to lists
            self.treat_list.append(treat)
            self.bird_list.append(bird)
            self.shot_list.append(shot)
            self.leash_list.append(leash)

    def on_draw(self):
        """ Render the screen. """

        #Clear anything already on screen
        self.clear()

        #Background
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        #Draw sprites
        self.treat_list.draw()
        self.bird_list.draw()
        self.shot_list.draw()
        self.leash_list.draw()
        self.player_list.draw()

        #Text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called whenever the mouse moves. """

        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic. """

        #Update sprites
        self.treat_list.update()
        self.bird_list.update()
        self.shot_list.update()
        self.leash_list.update()

        #Collision
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.treat_list)
        hit_list_2 = arcade.check_for_collision_with_list(self.player_sprite, self.bird_list)
        hit_list_3 = arcade.check_for_collision_with_list(self.player_sprite, self.shot_list)
        hit_list_4 = arcade.check_for_collision_with_list(self.player_sprite, self.leash_list)

        #Score
        for treat in hit_list: 
            treat.remove_from_sprite_lists()
            self.score += 100

        for bird in hit_list_2: 
            bird.remove_from_sprite_lists()
            self.score += 50

        for shot in hit_list_3: 
            shot.remove_from_sprite_lists()
            self.score -= 10

        for leash in hit_list_4: 
            leash.remove_from_sprite_lists()
            self.score -= 20

def main():
        """ Main function. """

        window = BeansWorld(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        fun_sound = arcade.load_sound("fun.wav")
        arcade.play_sound(fun_sound)
        window.setup()
        arcade.run()

if __name__ == "__main__":
        main()
        
