from pygame import display
from pygame import image
from pygame import transform
from pygame import Surface
from pygame import Rect
from pygame import SRCALPHA
from os import listdir
from os.path import isfile, join

class Level1View():
    def __init__(self, caption, size_wh):
        display.set_caption(caption)
        self.screen_width, self.screen_height = size_wh 
        # self.asset_folder = asset_folder
        
        self.window = display.set_mode((self.screen_width, self.screen_height))
        
    
    def draw_level(self, background, bg_image, player, objects, offset_x):
        for tile in background:
            self.window.blit(bg_image, tile)

        for obj in objects:
            obj.draw(self.window, offset_x)

        player.draw(self.window, offset_x)

        display.update()
    
    def generate_background(self, name):
        background_image = image.load(join("assets", "Background", name))
        _, _, width, height = background_image.get_rect()
        tiles = []

        for column in range(self.screen_width // width + 1):
            for row in range(self.screen_height // height + 1):
                position = (column * width, row * height)
                tiles.append(position)

        return tiles, background_image
    