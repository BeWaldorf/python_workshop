import pygame
from overworld_object_controller import OverworldObjectController
from player_model import PlayerModel

class PlayerController(OverworldObjectController):
    
    def __init__(self, window:pygame.Surface,  x:int, y:int) -> None:
        super().__init__(window)
        self._make_mv(window, x, y)
    
    
    def _make_mv(self, window, x, y) -> None:
        pass
    
    def obj_tick(self, fps: int, keys, objects) -> None:
        pass