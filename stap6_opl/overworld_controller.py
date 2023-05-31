import pygame
from overworld_model    import OverworldModel
from overworld_view     import OverworldView

class OverworldController():
    # Global variables:
    width: int
    heigth: int
    window: pygame.Surface
    clock : pygame.time.Clock
    
    # Constructor:
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock) -> None:
        self.window         = window
        self.width          = window.get_width()
        self.height         = window.get_height()
        self.world_model    = OverworldModel(window, self.width, self.height)
        self.world_view     = OverworldView(self.window)
        self.world_view.draw_brackground(self.window, "Pink.png")
        
        self.world_view.draw_terrain(self.world_model.terrain)
        
        self.clock = clock
    
    # Private methods:
    def _collision_array_builder(self) -> list[pygame.sprite.Sprite]:
        models_to_test = []
        for contr in self.world_model.object_controllers:
            contr.obj_model.update()
            models_to_test.append(contr.obj_model)
        return models_to_test
    
    # Public methods:
    def game_loop(self) -> bool:
        self.clock.tick(self.world_model.FPS)
        state: bool = self.world_model.logic_loop(self._collision_array_builder())
        self.world_view.draw_loop( self.world_model.trap, self.world_model.terrain, "Pink.png")
        pygame.display.update()
        return state
        