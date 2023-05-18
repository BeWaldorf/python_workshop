import pygame
from overworld_object_model import OverworldObjectModel

class TerrainModel(OverworldObjectModel):
    current_x: int = 0
    current_y: int = 0
    _is_masterblock: bool = None
    terrain_coords:list[list[int]] = []
        
    def __init__(self, x: int, y: int, is_master:bool = False):
        if is_master:
            self._is_masterblock = is_master
            self.terrain_coords = self._get_Terrain_coords()
            return
        self.current_x = x
        self.current_y = y
        super().__init__(self.current_x, self.current_y, "Terrain")
    
    def get_block_sprite(self, type: str) -> pygame.Surface:
        block = self.select_sprite(type)
        self.image = block
        return pygame.transform.scale2x(block)

    def _get_floor_coords(self) -> list[list[int]]:
        world_length, world_height = self.WORLD_SIZE
        coords = []
        for x_coord in range(-world_length // self.BLOCK_SIZE, (world_length * 2) // self.BLOCK_SIZE ):
            coord = [x_coord * self.BLOCK_SIZE, world_height - self.BLOCK_SIZE]
            coords.append(coord)
        return coords
    
    def get_terrain_coords(self) -> list[list[int]]:
        if self._is_masterblock:
            return self.terrain_coords
        return None
    
    def logic_loop(self):
        self.update()