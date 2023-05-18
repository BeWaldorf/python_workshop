import pygame
from overworld_model    import OverworldModel
from overworld_view     import OverworldView


class OverworldController():
    width: int
    heigth: int
    window: pygame.Surface
    clock : pygame.time.Clock
    
    
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock) -> None:
        self.window         = window
        self.width          = window.get_width()
        self.height         = window.get_height()
        self.world_model    = OverworldModel(window, self.width, self.height)
        self.world_view     = OverworldView(self.window)
        self.world_view.draw_brackground(self.window, "Blue.png")
        self.world_view.draw_terrain(self.world_model.terrain)
        
        self.clock = clock
        
    
    def game_loop(self) -> bool:
        self.clock.tick(self.world_model.FPS)
        state: bool = self.world_model.logic_loop()
        self.world_view.draw_loop(self.world_model.trap)
        pygame.display.update()
        return state
        