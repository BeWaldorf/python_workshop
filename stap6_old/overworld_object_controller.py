import pygame
from overworld_object_model import OverworldObjectModel
from overworld_object_view import OverworldObjectView

class OverworldObjectController():
    obj_model:  OverworldObjectModel
    obj_view:   OverworldObjectView
    
    def __init__(self) -> None:
        # self.window = window
        pass
    
    def _make_mv(self) -> None:
        pass
    
    def obj_tick(self, fps, window: pygame.Surface) -> None:
        self.obj_model.logic_loop(fps)
        surf, rect = self.obj_model.get_surface_rect_tuple()
        self.obj_view.draw_loop(window, surf, rect)
    

    def is_loopable(self) -> bool:
        return self.obj_model.is_loopable()