import pygame
from

class TerrainModel(  ):
    # Global variables:
    current_x: int = 0
    current_y: int = 0
    _is_masterblock: bool = None
    terrain_coords:list[list[int]] = []
    
    # Constructor:
    def __init__(self, x: int, y: int, is_master:bool = False):
        if is_master:
            self._is_masterblock = is_master
            self.terrain_coords = self._get_Terrain_coords()
            return
        self.current_x = x
        self.current_y = y
        super().__init__(self.current_x, self.current_y, "Terrain")
    
    # Private methods:
    def _get_floor_coords(self) -> list[list[int]]:
        world_width, world_height = self.WORLD_SIZE
        coords = []
        for x_coord in     :
        
        
        return coords
    
    # Public methods:
    def get_block_sprite(self, type: str) -> pygame.Surface:
        pass
    
    def get_terrain_coords(self) -> list[list[int]]:
        pass
    
    def logic_loop(self):
        pass
