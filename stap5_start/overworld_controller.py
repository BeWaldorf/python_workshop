import pygame
from overworld_model    import OverworldModel
from overworld_view     import OverworldView

class OverworldController():
    # Global variables:
    width: int
    heigth: int
    window: pygame.Surface
    
    # Constructor:
    def __init__(self, window: pygame.Surface) -> None:
        self.window         = window
        self.width          = window.get_width()
        self.height         = window.get_height()
        self.world_model    = OverworldModel(self.width, self.height)
        self.world_view     = OverworldView(self.window)
        self.world_view.draw_brackground(self.window, "Pink.png")
        
    
    # Private methods:
    def _collision_array_builder(self) -> list[list[pygame.sprite.Sprite]]:
        models_to_test = []
        
        
        return models_to_test
    
    # Public methods:
    def game_loop(self) -> bool:
        
        state: bool = self.world_model.logic_loop()
        self.world_view.draw_loop( "Pink.png", )
        pygame.display.update()
        return state
        