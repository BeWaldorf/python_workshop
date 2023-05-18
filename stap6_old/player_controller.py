import pygame
from overworld_object_controller import OverworldObjectController
from player_model import PlayerModel
from player_view import PlayerView

class PlayerController(OverworldObjectController):
    
    def __init__(self, x:int, y:int, size_wh: tuple[int, int]) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.size = size_wh
        self._make_mv()
        # self.obj_view.draw_object(self.obj_model.select_sprite("idle_left"),(x, y))
    
    
    def _make_mv(self) -> None:
        self.obj_model: PlayerModel = PlayerModel(self.x, self.y)
        self.obj_view: PlayerView  = PlayerView(self.size)
    
    def obj_tick(self, fps, window: pygame.Surface) -> None:
        self.obj_model.logic_loop(fps)
        self.obj_view.draw_loop(window, self.obj_model.select_sprite(self.obj_model.get_state()), self.obj_model.get_rect())
        super().obj_tick(fps, window)
        
    
    