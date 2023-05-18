import pygame

from overworld_object_controller import OverworldObjectController
from overworld_model    import OverworldModel
from overworld_view     import OverworldView
from terrain_controller import TerrainController
from player_controller  import PlayerController

class OverworldController():
    width: int
    heigth: int
    window: pygame.Surface
    
    
    def __init__(self, window: pygame.Surface) -> None:
        self.window         = window
        self.width          = window.get_width()
        self.height         = window.get_height()
        self.world_model    = OverworldModel(self.width, self.height)
        self.world_view     = OverworldView(self.window)
        self.world_view.draw_brackground(self.window, "Blue.png")
        self.world_view.draw_terrain(self.world_view.window, self.world_model.terrain)
        self.world_view.draw_loop(window, self.world_model.player)
        pygame.display.update()
        
        
    
    
    def game_loop(self) -> bool:
        state: bool = self.world_model.logic_loop(self.world_view.window)
        self.world_view.draw_loop(self.world_view.window, self.world_model.player)
        return state
        