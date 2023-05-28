import pygame
from overworld_object_controller import OverworldObjectController
from player_model import PlayerModel
from player_view import PlayerView

class PlayerController(OverworldObjectController):
    
    def __init__(self, window:pygame.Surface,  x:int, y:int) -> None:
        super().__init__(window)
        self._make_mv(window, x, y)
    
    
    def _make_mv(self, window, x, y) -> None:
        self.obj_model: PlayerModel = PlayerModel(x, y)
        self.obj_view: PlayerView  = PlayerView(window, self.obj_model.get_size_wh())
    
    def obj_tick(self, fps: int, keys, objects) -> None:
        self.obj_model.logic_loop(fps, keys, objects)
        
    
    