import pygame
from
from
from 

class TerrainController(  ):
    # Global variables:
    
    # Constructor:
    def __init__(self, window: pygame.Surface, x: int, y: int, size: tuple[int, int], terrain_type: str = "Grass",is_master: bool = False):
        if is_master:
            self.obj_model = 
            self._is_master = 
            return
        
        super().__init__(window)
        self._make_mv(x, y, size)
        self.obj_view.draw_object(self.obj_model.get_block_sprite(terrain_type), self.obj_model.get_coords())
    
    # Private methods:
    def _make_mv(self, x, y, size) -> None:
        pass
        
    # Public methods:
    def get_terrain_coords(self) -> list[list[int]]:
        pass
    
    def obj_tick(self) -> None:
        pass