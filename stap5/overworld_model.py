import pygame
from terrain_controller import TerrainController

class OverworldModel():
    width: int
    height: int
    window: pygame.Surface
    
    def __init__(self, window, width: int, height: int) -> None:
        self.width = width
        self.height = height
        terrain_master = TerrainController(None, None, None, None, None, True)
        terrain_coords = terrain_master.get_terrain_coords()
        self.terrain = self._create_terrain(window, terrain_coords)
    
    def set_window(self, window: pygame.Surface) -> None:
        self.window = window
    
    def logic_loop(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True
    
    def _create_terrain(self, window, coords: list[list[int]]) -> list[TerrainController]:
        blocks =  []
        for coord in coords:
            x = coord[0]
            y = coord[1]
            new_block = TerrainController(window, x, y, (96,96))
            blocks.append(new_block)
        return blocks