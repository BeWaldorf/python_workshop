import pygame
from overworld_object_model import OverworldObjectModel
from overworld_object_view import OverworldObjectView

class OverworldObjectController():
    obj_model:  OverworldObjectModel
    obj_view:   OverworldObjectView
    
    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
    
    def _make_mv(self) -> None:
        pass
    
    def obj_tick(self):
        self.obj_model.logic_loop()
        self.obj_view.draw_loop()
    
    def is_loopable(self) -> bool:
        return self.obj_model.is_loopable()