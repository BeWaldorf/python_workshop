import pygame
from overworld_model    import OverworldModel
from overworld_view     import OverworldView

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
        self.world_view.draw_brackground(self.window, "Pink.png")
    
    def game_loop(self) -> bool:
        state: bool = self.world_model.logic_loop()
        self.world_view.draw_loop()
        pygame.display.update()
        return state
        