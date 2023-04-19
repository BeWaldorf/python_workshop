
from pygame.sprite import Sprite
from pygame import Surface
from pygame import SRCALPHA

class OverworldObjectModel(Sprite):
    WIDTH = HEIGHT = NAME = SOURCEFOLDER_PATH = None
    current_x = current_y = rectangle = None
    def __init__(self, x, y, rectangle):
        super().__init__()
        self.rectangle = rectangle
        self.current_x = x
        self.current_y = y
    
    def get_coords(self) -> tuple:
        coords = (self.current_x, self.current_y)
        return coords
    
    def set_coords(self,x = None, y = None) -> None:
        if x != None:
            self.current_x = x
        if y != None:
            self.current_y = y
    
    def get_size_wh(self) -> tuple:
        size = (self.WIDTH, self.HEIGHT)
        return size